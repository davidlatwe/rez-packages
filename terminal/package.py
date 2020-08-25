
early = globals()["early"]


name = "terminal"

version = "1.0.0"

description = "Terminal"

tools = [
    "terminal",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]


@early()
def rez_core():
    import subprocess

    location = subprocess.check_output(
        [
            "rez-env",
            "rezcore",
            "--",
            "python",
            "-c",
            "import os;print(os.environ['REZ_CORE_BIN_PATH'])"
        ],
        universal_newlines=True
    )

    return location.strip()


def commands():
    env = globals()["env"]
    this = globals()["this"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")

    env.REZ_CORE_BIN_PATH = this.rez_core
