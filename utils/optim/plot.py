from plotting_utils import plotter
import os
import sys
import importlib



def get_snbo_path(root, test_problem, strategy):
    sys.path.append(root)

    output = None

    for _d in os.listdir(root):
        module_loc = '{}.config'.format(_d)

        importlib.util.spec_from_file_location(module_loc)
        experiment = importlib.import_module(module_loc).method_args

        if experiment["problem_name"] != test_problem:
            continue

        if experiment["model"][0] == "gp":
            if strategy == "None":
                assert output is None
                output = _d

        if experiment["model"][0] == "gp_slacked":
            q_dicts = experiment["model"][1]["q_dicts"]
            if len(q_dicts) != 1:
                continue
            if list(q_dicts.items())[0][0] == "q_init-0.25":
                if strategy == "Constant":
                    assert output is None
                    output = _d
            if list(q_dicts.items())[0][0] == "q-0.25":
                if strategy == "Concentration":
                    assert output is None
                    output = _d

    return os.path.join(root, output)

plotter(
    {
        "ConcentrationNew": [os.path.join(root_gpmp, test_problem_gpmp, "Concentration"),('orange', 'dashed')],
        "ConstantNew": [os.path.join(root_gpmp, test_problem_gpmp, "Constant"), ('blue', 'dashed')],
        "NoneNew": [os.path.join(root_gpmp, test_problem_gpmp, "None"), ('green', 'dashed')],
        "Concentration": [get_snbo_path(root_snbo, test_problem_snbo, "Concentration"), ('orange', 'solid')],
        "Constant": [get_snbo_path(root_snbo, test_problem_snbo, "Constant"), ('blue', 'solid')],
        "None": [get_snbo_path(root_snbo, test_problem_snbo, "None"), ('green', 'solid')],
    },
    306,
    test_problem_snbo,
    100,
)