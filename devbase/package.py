
name = "devbase"

description = "Development package/repository root path setup"

version = "1.0.0"


requires = [
    "device-*",
]


def commands():
    env = globals()["env"]
    resolve = globals()["resolve"]
    root = ""

    if "device" in resolve:
        device = str(resolve.device.version)

        if device == "studio.expdav":
            root = r"C:\Users\davidlatwe.lai\pipeline"

        elif device == "david.macair":
            root = "/Users/davidlatwe/PycharmProjects"

    env.OZARK_DEV_ROOT = root
