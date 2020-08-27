
name = "commonmark"

description = "Python parser for the CommonMark Markdown spec"

version = "0.9.1"

requires = []

variants = []


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
