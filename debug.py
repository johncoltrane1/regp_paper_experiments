import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

root = "C:\\Users\\PETIT\\data\\run_2024_03_23\\results\\EI\\rosenbrock10"

strategies = ["Constant", "Concentration", "Spatial", "None"]

n_runs = 30
n0 = 30

def data_getter(root, strategy, i, file_name):
    path = os.path.join(root, strategy, "debugging_{}".format(i), file_name)
    return np.load(path)

def plot_data(data, palette, strategy):
    medians = np.quantile(data, 0.5, axis=0)

    plt.plot(data.min(0), '--', color=palette[strategy], alpha=0.3)
    plt.plot(data.max(0), '--', color=palette[strategy], label=strategy+" (min/max)", alpha=0.3)
    plt.fill_between(list(range(data.min(0).shape[0])), data.min(0), data.max(0), color=palette[strategy], alpha=0.3)
    plt.plot(medians, 'o', markersize=2, label=strategy + " (med.)", color=palette[strategy])

palette = {"Constant": "r", "Concentration": "b", "Spatial": "k", "None": "green"}

plt.figure()

file_name = "cond_K_array.npy"
for strategy in strategies:
    data = []
    for i in range(n_runs):
        data.append(data_getter(root, strategy, i, file_name))

    data = np.array(data)

    plot_data(data, palette, strategy)

plt.legend()
plt.semilogy()
plt.title("Conditioning")
plt.show()


plt.figure()

file_name = "covparam_array.npy"
for strategy in strategies:
    data = []
    for i in range(n_runs):
        data.append(data_getter(root, strategy, i, file_name))

    data = np.array(data)
    data = data[:, :, 1:]

    data_plot = np.exp((- data).min(2))

    plot_data(data_plot, palette, strategy)

plt.legend()
plt.semilogy()
plt.title("Rho min")
plt.show()

plt.figure()

file_name = "t0_array.npy"
for strategy in ["Constant", "Concentration", "Spatial"]:
    data = []
    for i in range(n_runs):
        data.append(data_getter(root, strategy, i, file_name))

    data = np.array(data)

    data_plot = data

    plot_data(data_plot, palette, strategy)

plt.legend()
plt.semilogy()

plt.title("t0")

plt.show()

plt.figure()

file_name = "t0_array.npy"
for strategy in ["Constant", "Concentration", "Spatial"]:
    data = []
    for i in range(n_runs):
        t0 = data_getter(root, strategy, i, file_name)
        zi = np.load(os.path.join(root, strategy, "data_{}.npy".format(i)))[:, -1]

        datum = []
        for j in range(300):
            datum.append(
                (zi[:(n0 + j)] <= t0[j]).mean()
            )

        data.append(datum)

    data = np.array(data)

    data_plot = data

    plot_data(data_plot, palette, strategy)

plt.legend()
plt.semilogy()

plt.title("Frac. of points below t0")

plt.show()

plt.figure()

file_name = "t_array.npy"
for strategy in ["Constant", "Concentration", "Spatial"]:
    data = []
    for i in range(n_runs):
        data.append(data_getter(root, strategy, i, file_name))

    data = np.array(data)

    data_plot = data

    plot_data(data_plot, palette, strategy)

plt.legend()
plt.semilogy()

plt.title("t")

plt.show()

plt.figure()

file_name = "t_array.npy"
for strategy in ["Constant", "Concentration", "Spatial"]:
    data = []
    for i in range(n_runs):
        t = data_getter(root, strategy, i, file_name)
        zi = np.load(os.path.join(root, strategy, "data_{}.npy".format(i)))[:, -1]

        datum = []
        for j in range(300):
            datum.append(
                (zi[:(n0 + j)] <= t[j]).mean()
            )

        data.append(datum)

    data_plot = np.array(data)

    plot_data(data_plot, palette, strategy)

plt.legend()
plt.semilogy()

plt.title("Frac. of points below t")

plt.show()

####

plt.figure()

file_name = "t_array.npy"
strategy = "Constant"

data = []
for i in range(n_runs):
    t = data_getter(root, strategy, i, file_name)
    zi = np.load(os.path.join(root, strategy, "data_{}.npy".format(i)))[:, -1]

    datum = []
    for j in range(300):
        datum.append(
            (zi[:(n0 + j)] <= t[j]).mean()
        )

    plt.plot(datum)

plt.legend()
plt.semilogy()

plt.title("Frac. of points below t")

plt.show()

####

plt.figure()

file_name = "loo_tcrps_array.npy"
strategy = "Constant"

data = []
for i in range(n_runs):
    datum = data_getter(root, strategy, i, file_name)
    plt.plot(datum)

plt.legend()
plt.semilogy()

plt.title("LOO-tCRPS")

plt.show()

####

plt.figure()

file_name = "loo_tcrps_list_array.npy"
strategy = "Constant"

data = []
for i in range(n_runs):
    datum = data_getter(root, strategy, i, file_name)
    plt.plot(datum[:, 0], "k-")
    plt.plot(datum[:, -1], "b-")

plt.semilogy()

plt.title("LOO-tCRPS")

plt.show()

