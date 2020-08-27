
name = "pysftp"

description = "A friendly face on SFTP"

version = "0.2.9"

requires = [
    "paramiko-1.17+",
]

variants = [
    ["python-3"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
