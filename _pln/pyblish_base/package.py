
early = globals()["early"]


name = "pyblish_base"

description = "Test-driven content creation, see http://pyblish.com"


@early()
def __payload():
    from earlymod import util
    return util.git_build_clone(
        url="https://github.com/MoonShineVFX/pyblish-base.git",
        branch="master",
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
]

requires = [
    # Dependencies
    "python",
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
    env.PYTHONPATH.prepend("{root}")
