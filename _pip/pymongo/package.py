
name = "pymongo"

description = "Python driver for MongoDB <http://www.mongodb.org>"

version = "3.11.0"

requires = []

variants = [
    ["os-*", "python-*"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
