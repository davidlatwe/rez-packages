
name = "houdini"

version = "18.0.416"
 
description = "SideFX Houdini"

_data = {
    # Allzpark
    "label": "Houdini",
    "icon": "{root}/resources/icon.svg"
}

tools = [
    "houdinifx",
]


private_build_requires = ["rezutil-1"]
build_command = "python -m rezutil build {root}"


def commands():
    env = globals()["env"]
    system = globals()["system"]

    env.HOUDINI_VERSION = str(env.REZ_HOUDINI_VERSION)

    if system.platform == "windows":
        env.HOUDINI_LOCATION = "C:/Program Files/Side Effects Software/"\
                               "Houdini {env.HOUDINI_VERSION}"

    elif system.platform == "linux":
        pass

    elif system.platform == "osx":
        pass

    env.PATH.append("{env.HOUDINI_LOCATION}/bin")
