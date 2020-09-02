
early = globals()["early"]
late = globals()["late"]


name = "avalon"

description = "The safe post-production pipeline"

_data = {
    "label": "Avalon",
    "icon": "{root}/res/icons/ico/avalon.ico"
}


@early()
def __payload():
    import os
    from earlymod import util

    def get_version(data):
        import subprocess
        data["version"] = subprocess.check_output(
            ["python", "setup.py", "--version"],
            universal_newlines=True,
            cwd=data["repo"],
        ).strip()

    local = {
        "path": os.path.sep.join([os.environ["MY_DEVS"], "avalon-core"]),
        "tag": "localdev",
    }
    remote = {
        "url": "https://github.com/MoonShineVFX/avalon-core.git",
        "branch": "production",
        "tag": "91e31cac94cb814d4829c5ba26b0e53dde8f3d7d",
    }
    return util.git_payload(
        local=local,
        remote=remote,
        callbacks=[get_version]
    )


@early()
def version():
    data = globals()["this"].__payload

    version_str = data["version"]
    branch_name = data["branch"]

    major, minor, patch = version_str.split(".")
    return "%s-%s.%s.%s" % (branch_name, major, minor, patch)


@early()
def authors():
    data = globals()["this"].__payload
    return data["authors"]


@late()
def tools():
    in_context = globals()["in_context"]
    # Avalon tools
    _tools = [
        "loader",
    ]

    if in_context():
        context = globals()["context"]
        for pkg in context.resolved_packages:
            if getattr(pkg, "is_project_admin", False):
                _tools.append("manager")
                break

    return _tools


requires = [
    # Dependencies
    "house",
    "pymongo",
    "Qt.py",
]


private_build_requires = ["rezutil-1"]


@early()
def build_command():
    data = globals()["this"].__payload
    return "python -m rezutil build {root} --quiet".format(
        root=data["repo"],
    )


def pre_commands():
    env = globals()["env"]

    # (NOTE) convert it into `list` or it will always return True when
    #   checking __contains__.
    #   >>> "anything" in env.keys()
    #   True
    #   >>> "anything" in list(env.keys())
    #   False
    #
    current_env_keys = list(env.keys())

    env.AVALON_SESSION_SCHEMA = "avalon-core:session-3.0"
    session_v3_required = [
        "AVALON_PROJECTS",
        "AVALON_PROJECT",
        "AVALON_CONFIG",
    ]
    for key in session_v3_required:
        if key not in current_env_keys:
            env[key] = "__placeholder__"


# Set up environment
def commands():
    env = globals()["env"]
    resolve = globals()["resolve"]
    env.PYTHONPATH.prepend("{root}")

    # MongoDB
    env.AVALON_MONGO = "{env.HOUSE_PIPELINE_MONGO}"
    env.AVALON_DB = "avalon"
    env.AVALON_TIMEOUT = 5000

    # DCC App Setup
    if "maya" in resolve:
        env.PYTHONPATH.append("{root}/setup/maya")
        env.AVALON_APP = "maya"
        env.AVALON_APP_NAME = "maya"

    if "houdini" in resolve:
        env.HOUDINI_SCRIPT_PATH.append("{root}/res/houdini")
        env.AVALON_APP = "houdini"
        env.AVALON_APP_NAME = "houdini"

    if "nuke" in resolve:
        env.NUKE_PATH.append("{root}/setup/nuke/nuke_path")
        env.AVALON_APP = "nuke"
        env.AVALON_APP_NAME = "nuke"


def post_commands():
    import os
    env = globals()["env"]

    # (NOTE) convert it into `list` or it will always return True when
    #   checking __contains__.
    #   >>> "anything" in env.keys()
    #   True
    #   >>> "anything" in list(env.keys())
    #   False
    #
    current_env_keys = list(env.keys())

    # Startup workdir
    required = [
        "AVALON_PROJECTS",
        "AVALON_PROJECT",
        "AVALON_APP",
    ]
    if all(k in current_env_keys for k in required):
        env.AVALON_WORKDIR = os.path.sep.join([
            "{env.AVALON_PROJECTS}",
            "{env.AVALON_PROJECT}",
            "Avalon",
            "_Lobby",
            "{env.AVALON_APP}",
        ])
