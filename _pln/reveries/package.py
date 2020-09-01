
early = globals()["early"]


name = "reveries"

description = "Avalon post-production pipeline configuration module"


@early()
def __payload():
    import os
    from earlymod import util
    local = {
        "path": os.path.sep.join([os.environ["MY_DEVS"], "reveries-config"]),
        "tag": "localdev",
    }
    remote = {
        "url": "https://github.com/MoonShineVFX/reveries-config.git",
        "branch": "production",
        "tag": "0ad0c6d00fcefa71a7473ffabd4c6138ac23a536",
    }
    return util.git_payload(
        local=local,
        remote=remote,
    )


@early()
def version():
    data = globals()["this"].__payload

    version_str = "1.0.1"  # (TODO) add version query
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
    "house",
    "avalon",
    "avalon_sftpc",
    "pyblish_qml",
]


private_build_requires = ["rezutil-1"]


@early()
def build_command():
    data = globals()["this"].__payload
    return "python -m rezutil build {root} --quiet".format(
        root=data["repo"],
    )


# Set up environment
def commands():
    env = globals()["env"]
    env.PYTHONPATH.prepend("{root}")

    # Config
    env.AVALON_CONFIG = "reveries"
    env.CONFIG_ROOT = "{root}"

    # Deadline
    env.AVALON_DEADLINE = "{env.HOUSE_PIPELINE_DEADLINE}"
    env.AVALON_DEADLINE_AUTH = "{env.HOUSE_PIPELINE_DEADLINE_AUTH}"
    env.AVALON_DEADLINE_APP = "{env.HOUSE_PIPELINE_DEADLINE_APP}"
