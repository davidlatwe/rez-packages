
early = globals()["early"]


name = "reveries"

description = "Avalon post-production pipeline configuration module"


@early()
def __payload():
    from earlymod import util
    return util.git_build_clone(
        url="https://github.com/MoonShineVFX/reveries-config.git",
        branch="production",
    )


@early()
def version():
    import subprocess
    data = globals()["this"].__payload

    version_str = "1.0.1"  # (TODO) add version query
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
    "house",
    "avalon",
    "avalon_sftpc",
    "pyblish_qml",
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

    # Config
    env.AVALON_CONFIG = "reveries"
    env.CONFIG_ROOT = "{root}"

    # Deadline
    env.AVALON_DEADLINE = "{env.HOUSE_PIPELINE_DEADLINE}"
    env.AVALON_DEADLINE_AUTH = "{env.HOUSE_PIPELINE_DEADLINE_AUTH}"
    env.AVALON_DEADLINE_APP = "{env.HOUSE_PIPELINE_DEADLINE_APP}"
