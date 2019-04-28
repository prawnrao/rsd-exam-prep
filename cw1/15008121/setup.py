from setuptools import setup, find_packages


setup(
    name="alchemist",
    version="0.1.1",
    packages=find_packages(exclude=['*tests']),
    install_requires=["argparse", "pyyaml"],
    author="Pranav Rao",
    author_email="zcappra@ucl.ac.uk",

    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]
    }
)
