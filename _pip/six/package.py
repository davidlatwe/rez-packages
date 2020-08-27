
name = "six"

description = "Python 2 and 3 compatibility utilities"

version = "1.15.0"

requires = []

variants = []


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
