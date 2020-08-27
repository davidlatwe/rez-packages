
name = "python_dotenv"

description = "Add .env support to your django/flask apps in " \
              "development and deployments"

version = "0.14.0"

requires = []

variants = []


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
