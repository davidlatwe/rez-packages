
name = "vscode"

uuid = "repository.dev.vscode"

version = "latest"

description = "Code editing. Redefined. Free. Built on open source. "\
              "Runs everywhere."

authors = ["Microsoft"]

tools = [
    "vscode",
]

variants = [
    ["platform-*"],
]

build_command = False


def commands():
    system = globals()["system"]
    env = globals()["env"]
    alias = globals()["alias"]

    if system.platform == "windows":
        env.PATH.prepend(r"C:\Program Files\Microsoft VS Code\bin")

    elif system.platform == "osx":
        raise NotImplementedError

    elif system.platform == "linux":
        raise NotImplementedError

    else:
        print("Unknown platform: %s" % system.platform)

    alias("vscode", "code")
