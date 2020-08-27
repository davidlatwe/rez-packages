
name = "pynacl"

description = "Python binding to the Networking and Cryptography (NaCl) library"

version = "1.4.0"

requires = [
    "cffi-1.4.1+",
    "six",
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
