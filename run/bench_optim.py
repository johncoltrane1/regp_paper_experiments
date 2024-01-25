import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
import gpmp as gp
import gpmpcontrib as gpc
import gpmpcontrib.optim.expectedimprovement as ei
import lhsmdu
import sys
import os
import gpmpcontrib.optim.test_problems as test_problems
import traceback

assert gp.num._gpmp_backend_ == "torch", "{} is used, please install Torch.".format(gp.num._gpmp_backend_)

# Settings default values and types for different options
env_options = {
    "OUTPUT_DIR": ("output", str),
    "N_ITERATIONS": (300, int),
    "SLURM_ARRAY_TASK_ID": (None, int),
    "N_RUNS": (1, int),
    "PROBLEM": ("goldsteinprice", str),
    "N0_OVER_D": (3, int),
    "STRATEGY": ("None", str),
    "Q_STRATEGY": (0.25, float),
    "CRIT_OPT_METHOD": ("SLSQP", str),
    "RELAXED_INIT": ("flat", str),
    "FTOL": (1e-06, float),
    "GTOL": (1e-05, float),
    "EPS": (1e-08, float),
    "MAXFUN": (15000, int),
    "MAXITER": (15000, int),
    "N_SMC": (1000, int),
    "MH_STEPS": (5, int),
    "SMC_METHOD": ("step_with_possible_restart", str),
}


# Initialization Function
def initialize_optimization(env_options):
    options = {}
    crit_optim_options = {}
    ei_options = {"mh_params": {}}
    # Loop through the environment options
    for key, (default, value_type) in env_options.items():
        value = os.getenv(key, default)
        if value is not None:
            if key == "CRIT_OPT_METHOD":
                # Add to crit_optim_options
                crit_optim_options["method"] = value_type(value)
            elif key in [
                "RELAXED_INIT",
                "FTOL",
                "GTOL",
                "EPS",
                "MAXFUN",
                "MAXITER",
            ]:
                # Add to crit_optim_options
                crit_optim_options[key.lower()] = value_type(value)
            elif key == "SLURM_ARRAY_TASK_ID" and value is not None:
                idx_run_list = [value_type(value)]
            elif key == "N_RUNS" and "SLURM_ARRAY_TASK_ID" not in os.environ:
                idx_run_list = list(range(value_type(value)))
            elif key == "STRATEGY":
                options["threshold_strategy"] = value

                # Check if Q_STRATEGY is set, use its value if available, otherwise use default
                options["q_strategy_value"] = float(
                    os.getenv("Q_STRATEGY", env_options["Q_STRATEGY"][0])
                )

            elif key == "Q_STRATEGY":
                continue  # Handled with STRATEGY
            elif key in [
                "MH_STEPS",
            ]:
                ei_options["mh_params"][key.lower()] = value_type(value)
            elif key in [
                "N_SMC",
                "SMC_METHOD",
            ]:
                ei_options[key.lower()] = value_type(value)
            else:
                # Add to options directly
                options[key.lower()] = value_type(value)

    # Set crit_optim_options in options
    if crit_optim_options:
        options["crit_optim_options"] = crit_optim_options
    if ei_options:
        options["ei_options"] = ei_options

    problem = getattr(test_problems, options["problem"])

    return problem, options, idx_run_list


# --------------------------------------------------------------------------------------
problem, options, idx_run_list = initialize_optimization(env_options)

# Initialize storage
xi_records = []
history_records = []

# Repetition Loop
for i in idx_run_list:
    ni0 = options["n0_over_d"] * problem.input_dim
    xi = gp.misc.designs.scale(
        np.array(lhsmdu.sample(problem.input_dim, ni0, randomSeed=None).T),
        problem.input_box,
    )

    if options["threshold_strategy"] == "None":
        model = gpc.Model_ConstantMeanMaternpML(
            "GP_bench_{}".format(options["problem"]),
            output_dim=problem.output_dim,
            covariance_params={"p": 2},
        )
    else:
        model = gpc.Model_ConstantMeanMaternp_reGP(
            {"strategy": options["threshold_strategy"] , "level": options["q_strategy_value"] , "n_init": ni0},
            "reGP_bench_{}".format(options["problem"]),
            crit_optim_options=options["crit_optim_options"],
            output_dim=problem.output_dim,
            covariance_params={"p": 2},
        )

    eialgo = ei.ExpectedImprovement(problem, model, options=options["ei_options"])
    eialgo.force_param_initial_guess = True

    eialgo.set_initial_design(xi=xi)

    # Optimization loop
    for step_ind in range(options["n_iterations"]):
        print(f"\niter {step_ind}")

        # Run a step of the algorithm
        try:
            eialgo.step()
        except gp.kernel.NonInvertibleInitCovMat as e:
            print("Aborting: {}".format(e))
            #print(traceback.format_exc())
            break

    # endfor

    # Store the history of observations
    history_records.append(eialgo.zi)
    xi_records.append(eialgo.xi)

    # Prepare output directory
    i_output_path = os.path.join(options["output_dir"], "data_{}.npy".format(str(i)))

    # Save data
    np.save(i_output_path, np.hstack((eialgo.xi, eialgo.zi)))
