from argparse import ArgumentParser
from math import sin, cos
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

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


def calculate_coords(parent, size, angular_step, left):
    """ This function calculates the coordinates for the next branch.
    """
    if left:
        daughter_branch = {
            'x': parent['x'] + size * sin(parent['angle'] -
                                          angular_step),
            'y': parent['y'] + size * cos(parent['angle'] -
                                          angular_step),
            'angle': parent['angle'] - angular_step
        }
    else:
        daughter_branch = {
            'x': parent['x'] + size * sin(parent['angle'] +
                                          angular_step),
            'y': parent['y'] + size * cos(parent['angle'] +
                                          angular_step),
            'angle': parent['angle'] + angular_step
        }
    return daughter_branch


def plotting(branch, new_branches):
    """This function plots the new generation of branches after the
    coordinates have been calculated.
    """
    plt.plot([branch['x'], new_branches[-2]['x']],
             [branch['y'], new_branches[-2]['y']])
    plt.plot([branch['x'], new_branches[-1]['x']],
             [branch['y'], new_branches[-1]['y']])


def run(branch_reduction, generations, branching_angle,
        branch_size, plot=True):
    """This function runs the entire simulation.
    """
    branches = [{
        'x': 0,
        'y': branch_size,
        'angle': 0
    }]
    origin_branch = [[0, 0], [branches[0]['x'], branches[0]['y']]]

    if plot:
        plt.plot(origin_branch[0], origin_branch[1])

    # This loop plots the successive generations of branches.
    i = 1
    while i <= generations:
        new_branches = []
        branch_size *= branch_reduction
        for branch in branches:
            new_branches.append(
                calculate_coords(branch, branch_size, branching_angle,
                                 True))
            new_branches.append(
                calculate_coords(branch, branch_size, branching_angle,
                                 False))
            if plot:
                plotting(branch, new_branches)
        branches = new_branches
        i += 1
    if plot:
        plt.savefig('tree.png')


if __name__ == "__main__":
    run(arguments.reduction, arguments.generations,
        arguments.angle, arguments.first)
