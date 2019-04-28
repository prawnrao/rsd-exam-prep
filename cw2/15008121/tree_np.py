from argparse import ArgumentParser
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
from numba import jit

parser = ArgumentParser(description="")
parser.add_argument('--reduction', '-r', default=0.6, type=float,
                    help="ratio of daughter and parent branch")
parser.add_argument('--generations', '-g', default=5, type=int,
                    help="number of generations of branches")
parser.add_argument('--angle', '-a', default=0.1, type=float,
                    help="branching angle of each successive"
                    + "generations")
parser.add_argument('--first', '-f', default=1, type=float,
                    help="sets the size of the first branch")

arguments = parser.parse_args()


@jit(nopython=True, cache=True)
def calculate_coords_and_plot(parent_branches, size, angular_step,
                              isLeft, plot=True):
    """ This function calculates the coordinates for the next branch
    and plots each generation of branches at once.
    """

    if isLeft:
        new_angles = parent_branches[:, 2] - angular_step
    else:
        new_angles = parent_branches[:, 2] + angular_step

    new_xs = parent_branches[:, 0] + size * np.sin(new_angles)
    new_ys = parent_branches[:, 1] + size * np.cos(new_angles)

    # if plot:
    #    plt.plot([parent_branches[:, 0], new_xs],
    #             [parent_branches[:, 1], new_ys])

    daughter_branches = np.dstack((new_xs, new_ys, new_angles))

    return daughter_branches


def run(branch_reduction, generations, branching_angle, branch_size,
        plot=True):
    """This function runs the entire simulation.
    """
    origin_branch = np.array([[0, 0], [0, branch_size]])

    if plot:
        plt.plot(origin_branch[0], origin_branch[1])

    branches = np.array((0, branch_size, 0), ndmin=2)
    i = 0
    while i < generations:
        branch_size *= branch_reduction

        left_branches = calculate_coords_and_plot(branches, branch_size,
                                                  branching_angle, True,
                                                  plot)
        right_branches = calculate_coords_and_plot(branches,
                                                   branch_size,
                                                   branching_angle,
                                                   False, plot)

        new_branches = np.append(left_branches[0], right_branches[0],
                                 axis=0)
        i += 1
        branches = new_branches

    if plot:
        plt.savefig("tree_np.png")


if __name__ == "__main__":
    run(arguments.reduction, arguments.generations,
        arguments.angle, arguments.first)
