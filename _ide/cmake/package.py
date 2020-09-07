
name = "cmake"

version = "3.18.2"

tools = [
    "cmake"
]

build_command = False


def commands():
    env = globals()["env"]
    env.PATH.prepend("C:/Program Files/CMake/bin")
