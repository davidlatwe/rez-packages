
early = globals()["early"]


name = "terminal"

version = "1.0.0"

description = "Terminal"

_data = {
    "label": "Terminal",
    "icon": "{root}/resources/terminal.svg"
}

requires = [
    "rez",
]

tools = [
    "terminal",
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]


@early()
def rez_bin_path():
    import subprocess

    # The stdout from `rez-env` may content outputs from rcfile
    # (bash startup script), so we add `tag` to extract the data
    # we need.
    # Noted that the rcfile output may not be observed from regular
    # `print(stdout)`, but `print(repr(stdout))` will.
    tag = ":::data:::"
    cmd = ("import os;"
           "print('%s' + os.environ['REZ_CORE_BIN_PATH'] + '%s')")
    tagged_cmd = cmd % (tag, tag)

    location = subprocess.check_output(
        [
            "rez-env",
            "rezcore",
            "--",
            "python",
            "-c",
            tagged_cmd
        ],
        universal_newlines=True
    )

    return location.split(tag)[1]


def commands():
    env = globals()["env"]
    this = globals()["this"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")

    env.REZ_CORE_BIN_PATH = this.rez_bin_path
