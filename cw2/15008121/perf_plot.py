import timeit
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def plot_perf():
    """Plots the performance of tree.py.
    """
    n = 1000
    i = 0
    max_generations = 10
    time_data = []
    generations = []

    while i <= max_generations:
        time_data.append(timeit.timeit(
            'run(0.6, {}, 0.1, 1, False)'.format(i),
            number=n, setup='from tree import run'))
        generations.append(i)
        i += 1

    plt.plot(generations, time_data, '-bx')
    plt.ylabel('Time taken for {} iterations (sec)'.format(n))
    plt.xlabel('Number of generations of branches')
    plt.savefig("perf_plot.png")
    plt.clf()


def plot_np_perf():
    """Plots the performance of tree_np.py.
    """
    n = 10000
    i = 0
    max_generations = 12
    time_data = []
    generations = []

    while i <= max_generations:
        time_data.append(timeit.timeit(
            'run(0.6, {}, 0.1, 1, False)'.format(i),
            number=n, setup='from tree_np import run'))
        generations.append(i)
        i += 1

    plt.plot(generations, time_data, '-rx', )
    plt.ylabel('Time taken for {} iterations (sec)'.format(n))
    plt.xlabel('Number of generations of branches')
    plt.legend
    plt.savefig('perf_comparison.png')


if __name__ == '__main__':
    plot_perf()
    plot_np_perf()
