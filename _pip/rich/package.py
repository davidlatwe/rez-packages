
name = "rich"

description = "Render rich text, tables, progress bars, " \
              "syntax highlighting, markdown and more to the terminal"

version = "6.0.0"

requires = [
    "colorama-0.4.0+<0.5.0",
    "commonmark-0.9.0+<0.10.0",
    "dataclasses-0.7+<0.8",
    "pygments-2.6.0+<3.0.0",
    "typing_extensions-3.7.4+<4.0.0",
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
