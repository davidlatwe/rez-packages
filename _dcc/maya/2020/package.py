
late = globals()["late"]


name = "maya"

version = "2020"

description = "Autodesk Maya 2020"


@late()
def tools():
    in_context = globals()["in_context"]

    _tools = [
        "maya",
        "mayapy",
    ]

    if in_context():
        context = globals()["context"]
        for pkg in context.resolved_packages:
            pipeline_tool = getattr(pkg, "pipeline_dcc_launcher", None)
            if pipeline_tool:
                _tools.insert(0, pipeline_tool)

    return _tools


build_command = False


def commands():
    system = globals()["system"]
    env = globals()["env"]

    env.MAYA_VERSION = "2020"

    if system.platform == "windows":
        env.MAYA_LOCATION = "C:/Program Files/Autodesk/Maya{env.MAYA_VERSION}"
        env.PATH.append("C:/Program Files/Common Files/Autodesk Shared/")
        env.PATH.append("C:/Program Files (x86)/Autodesk/Backburner/")

    elif system.platform == "linux":
        env.MAYA_LOCATION = "/usr/autodesk/maya{env.MAYA_VERSION}"

    elif system.platform == "osx":
        env.MAYA_LOCATION = "/Applications/Autodesk/maya{env.MAYA_VERSION}"\
                            "/Maya.app/Contents"
        env.DYLD_LIBRARY_PATH = "{env.MAYA_LOCATION}/MacOS"

    env.PATH.append("{env.MAYA_LOCATION}/bin")

    # Override some Maya default settings (optimization)
    # todo: These might need to be moved out to be left to company specific choices
    env.MAYA_DISABLE_CLIC_IPM = "Yes"
    env.MAYA_DISABLE_CIP = "Yes"
    env.MAYA_DISABLE_CER = "Yes"
    env.PYMEL_SKIP_MEL_INIT = "Yes"
    env.LC_ALL = "C"

    # Enable OpenGL in remote desktop
    env.MAYA_ALLOW_OPENGL_REMOTE_SESSION = "Yes"
