
early = globals()["early"]


name = "avalon"

description = "The safe post-production pipeline"

_data = {
    "icon": "{root}/resources/avalon.ico"
}


@early()
def __payload():
    from earlymod import util
    return util.git_build_clone(
        url="https://github.com/MoonShineVFX/avalon-core.git",
        branch="production",
    )


@early()
def version():
    import subprocess
    data = globals()["this"].__payload

    version_str = subprocess.check_output(
        ["python", "setup.py", "--version"],
        # Ensure strings are returned from both Python 2 and 3
        universal_newlines=True,
        cwd=data["repo"],
    ).strip()
    branch_name = subprocess.check_output(
        ["git", "branch", "--show-current"],
        universal_newlines=True,
        cwd=data["repo"],
    ).strip()

    major, minor, patch = version_str.split(".")
    return "%s-%s.%s.%s" % (branch_name, major, minor, patch)


@early()
def authors():
    from earlymod import util
    data = globals()["this"].__payload
    return util.git_authors(data["repo"])


tools = [
    "python -m avalon",
]

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
        # (TODO) How to make workdir ?
        #   Perhaps a project-lobby-like path where is on top of all assets ?
        #   Once get in DCC, workfile app take over, but workfile app still
        #   need .toml to do the job.
        env.AVALON_WORKDIR = ""
