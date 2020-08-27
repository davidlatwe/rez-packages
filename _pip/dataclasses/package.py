
name = "dataclasses"

description = "A backport of the dataclasses module for Python 3.6"

version = "0.7"

requires = []

variants = [
    ["python-3"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
