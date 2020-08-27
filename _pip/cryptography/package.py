
name = "cryptography"

description = "cryptography is a package which provides cryptographic " \
              "recipes and primitives to Python developers."

version = "3.1"

requires = [
    "!cffi==1.11.3",
    "cffi-1.8+",
    "six-1.4.1+"
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
