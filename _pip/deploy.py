
import os
import subprocess


root = os.path.dirname(__file__)

packages = [

    "pysftp",
    "paramiko",
    "bcrypt",
    "cryptography",
    "pynacl",
    "cffi",
    "six",
    "pycparser",

    "rich",
    "colorama",
    "commonmark",
    "dataclasses",
    "pygments",
    "typing_extensions",

    "pymongo",

    "python_dotenv",

]


def deploy(package, release=None):
    print("Deploying package %s ..." % package)

    if release:
        args = ["rez-release"]
    else:
        args = ["rez-build", "--install"]

    subprocess.check_call(args, cwd=os.path.join(root, package))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true",
                        help="Deploy to package releasing location.")

    opt = parser.parse_args()

    for pkg in reversed(packages):
        deploy(pkg, opt.release)
