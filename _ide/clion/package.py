
name = "clion"

uuid = "repository.dev.clion"

version = "latest"

description = "A Smart Cross-Platform IDE for C and C++"

authors = ["JetBrains"]

tools = [
    "clion",
]

variants = [
    ["platform-*"],
]

build_command = False


def commands():
    system = globals()["system"]
    env = globals()["env"]

    if system.platform == "windows":
        raise NotImplementedError
    elif system.platform == "osx":
        env.PATH.prepend("/Applications/CLion.app/Contents/MacOS")
    elif system.platform == "linux":
        raise NotImplementedError
    else:
        print("Unknown platform: %s" % system.platform)
