
early = globals()["early"]


name = "pyblish"

description = "Test-driven content creation, see http://pyblish.com"


@early()
def __payload():
    from earlymod import util

    def get_version(data):
        import subprocess
        data["version"] = subprocess.check_output(
            ["python", "setup.py", "--version"],
            universal_newlines=True,
            cwd=data["repo"],
        ).strip()

    return util.git_build_clone(
        url="https://github.com/pyblish/pyblish-base.git",
        branch="master",
        tag="1.8.7",
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
