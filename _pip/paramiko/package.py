
name = "paramiko"

description = "SSH2 protocol library"

version = "2.7.1"

requires = [
    "cryptography-2.5+",
    "bcrypt-3.1.3+",
    "pynacl-1.0.1+",
]

variants = []


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
