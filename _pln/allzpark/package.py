
early = globals()["early"]  # lint helper


name = "allzpark"

uuid = "repository.allzpark"

description = "Package-based application launcher for VFX and games " \
              "production"


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
        "path": os.path.sep.join([os.environ["MY_DEVS"], "allzpark"]),
        "tag": "localdev",
    }
    remote = {
        "url": "https://github.com/davidlatwe/allzpark.git",
        "branch": "dev",
        "tag": "1efe2b087d088ce8f1452d23bcc59021bfc092b4",
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


tools = [
    "allzpark",
    "park",  # alias of `allzpark`
]

requires = [
    "rez",
    "Qt.py",
    "python",
]


@early()
def build_command():
    import os
    data = globals()["this"].__payload
    os.environ["_GIT_CLONED_SRC_PATH"] = data["repo"]
    return "python {root}/rezbuild.py {install}"


def commands():
    env = globals()["env"]
    alias = globals()["alias"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib")

    alias("park", "allzpark")
