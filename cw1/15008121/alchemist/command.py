from argparse import ArgumentParser
import yaml
from alchemist.laboratory import Laboratory


def process():
    """
    """
    parser = ArgumentParser(description="")

    # optional argument, when passed the value True is stored.
    parser.add_argument('--reactions', '-r', action="store_true",
                        help="returns the number of reactions.")

    # mandatory argument, which holds the laboratory in a yaml file
    parser.add_argument('yaml_file', help="laboratory stored as a yaml"
                        + "file")

    arguments = parser.parse_args()

    dict_lab = yaml.load(open(arguments.yaml_file))

    # instantiates a new laboratory object using the dictionary from
    # the yaml_file arguemnet
    lab = Laboratory(dict_lab)

    if(arguments.reactions):
        print(lab.run_full_experiment(arguments.reactions))
    else:
        lab.run_full_experiment(arguments.reactions)
        print(yaml.dump({'lower': lab.lower, 'upper': lab.upper}))

if __name__ == '__main__':
    process()
