
name = "pycharm"

uuid = "repository.dev.pycharm"

version = "latest"

description = "The Python IDE for Professional Developers"

authors = ["JetBrains"]

_data = {
    "label": "PyCharm (CE)",
    "icon": "{root}/resources/pycharm.ico"
}

tools = [
    "project",
    "pycharm",
]

variants = [
    ["platform-*"],
]

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]


def commands():
    system = globals()["system"]
    alias = globals()["alias"]
    env = globals()["env"]

    if system.platform == "windows":
        env.PATH.prepend(r"C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.2\bin")

    elif system.platform == "osx":
        env.PATH.prepend("/Applications/PyCharm CE.app/Contents/MacOS")

    elif system.platform == "linux":
        raise NotImplementedError

    else:
        print("Unknown platform: %s" % system.platform)

    env.PATH.prepend("{root}/bin")

    # Set alias
    alias("charm", "pycharm")
