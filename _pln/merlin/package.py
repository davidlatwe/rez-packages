
late = globals()["late"]


name = "merlin"

description = "The magic man who makes Avalon, Rez and Allzpark works."

version = "1.0.0"

requires = [
    "ozark",
    "avalon",
]


private_build_requires = ["rezutil-1"]
build_command = "python -m rezutil build {root}"


def commands():
    env = globals()["env"]

    # Register location 'avalon' to mongozark
    env.REZ_CONFIG_FILE.append("{root}/config/rezconfig.py")

    # Merlin command line tools
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
    # Avalon application toml
    env.PATH.prepend("{root}/apps")
