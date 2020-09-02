
import os
import shutil
import identicon
import subprocess
from ozark import util as ozark_util
from avalon import api, io, inventory as inventory_io
from avalon.vendor import toml


def init():
    merlin_root = os.environ["REZ_MERLIN_ROOT"]
    template = os.path.join(merlin_root, "template", "profile.py")
    package_py = os.path.join(os.getcwd(), "package.py")
    if os.path.exists(package_py):
        print("package.py already exists in current directory.")
        return

    profile_name = os.path.basename(os.getcwd())

    with open(template, "r") as plate:
        lines = plate.read() % (profile_name, profile_name)
    with open(package_py, "w") as pkg_file:
        pkg_file.write(lines)

    res_dir = os.path.join(os.getcwd(), "resources")
    os.makedirs(res_dir)

    # toml
    for toml_name in [".config.toml", ".inventory.toml"]:
        toml_src = os.path.join(merlin_root, "template", toml_name)
        toml_dst = os.path.join(res_dir, toml_name)
        shutil.copy(toml_src, toml_dst)

    # generate identicon for profile
    icon_path = identicon.generate(profile_name)
    shutil.move(icon_path, os.path.join(res_dir, "icon.png"))

    # Open profile package with default editor for authoring
    subprocess.call([
        "idle",
        "-e",
        package_py,
    ])


def build(location=None):
    ozark_util.build(location)

    # write project config into avalon db
    #
    def _read(path):
        try:
            with open(path) as f:
                data = toml.load(f)
        except IOError:
            raise

        return data

    res_dir = os.path.join(os.getcwd(), "resources")

    project = os.path.basename(os.getcwd())
    config = _read(os.path.join(res_dir, ".config.toml"))
    inventory = _read(os.path.join(res_dir, ".inventory.toml"))

    io.install()
    api.Session["AVALON_PROJECT"] = project
    inventory_io.save(project, config, inventory)
