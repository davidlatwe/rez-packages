
name = "bcrypt"

description = "Modern password hashing for your software and your servers"

version = "3.2.0"

requires = [
    "six-1.4.1+",
    "cffi-1.1+",
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
