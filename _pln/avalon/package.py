
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
        "tag": "localdev",
        "path": os.path.sep.join([os.environ["OZARK_DEV_ROOT"],
                                  "avalon-core"]),
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


private_build_requires = ["devbase-1", "rezutil-1"]


@early()
def build_command():
    data = globals()["this"].__payload
    return "python -m rezutil build {root}".format(
        root=data["repo"],
    )


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
