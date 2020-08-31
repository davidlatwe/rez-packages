
early = globals()["early"]


name = "avalon_sftpc"

description = "Avalon SFTP Client, for uploading Avalon workfile or " \
              "representation to remote site via SFTP"


@early()
def __payload():
    from earlymod import util
    return util.git_build_clone(
        url="https://github.com/davidlatwe/avalon-sftpc.git",
        branch="master",
        tag="535ac3cf8362d633cf49227a388e04c99dfe3c69",
    )


@early()
def version():
    import subprocess
    data = globals()["this"].__payload

    version_str = "0.3.0"  # (TODO) add version query
    branch_name = data["branch"]

    major, minor, patch = version_str.split(".")
    return "%s-%s.%s.%s" % (branch_name, major, minor, patch)


@early()
def authors():
    data = globals()["this"].__payload
    return data["authors"]


tools = [
    "python -m avalon_sftpc --demo",
]

requires = [
    # Dependencies
    "avalon",
    "pysftp",
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
