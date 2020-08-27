
name = "cffi"

description = "Foreign Function Interface for Python calling C code."

version = "1.14.2"

requires = [
    "pycparser"
]

variants = [
    ["os-*", "python-*"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
