
include = globals()["include"]


name = "house"

version = "1.0.0"

description = "Studio/Site-wide production environment"

requires = [
    "python",
    "python_dotenv",
]


private_build_requires = ["rezutil-1"]
build_command = "python -m rezutil build {root} --ignore README.md"


@include("util")
def commands():
    import os
    util = globals()["util"]
    this = globals()["this"]
    env = globals()["env"]

    # Prepend env.PYTHONPATH into sys.path for later operation's
    # requirement
    util.sys_path_prepend(env)

    # Parse environment setup from .env, if exists
    env_file = os.path.join(this.root, ".env")
    if os.path.isfile(env_file):
        util.load_dotenv(file=os.path.join(this.root, ".env"),
                         env=env)
