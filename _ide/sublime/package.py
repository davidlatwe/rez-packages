
name = "sublime"

uuid = "repository.dev.sublime"

version = "latest"

description = "A sophisticated text editor for code, markup and prose"

authors = ["Sublime HQ Pty Ltd"]

tools = [
    "sublime",
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
        env.PATH.prepend(r"C:\Program Files\Sublime Text 3")

    elif system.platform == "osx":
        env.PATH.prepend("/Applications/Sublime Text.app/SharedSupport/bin")

    elif system.platform == "linux":
        raise NotImplementedError

    else:
        print("Unknown platform: %s" % system.platform)

    alias("sublime", "subl")
