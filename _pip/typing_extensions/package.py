
name = "typing_extensions"

description = "Backported and Experimental Type Hints for Python 3.5+"

version = "3.7.4.3"

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
