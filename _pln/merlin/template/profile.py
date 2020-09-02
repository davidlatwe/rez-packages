
import os
late = globals()["late"]


name = "%s"
version = "1.0.0"

_data = {
    # Allzpark
    "label": "%s",
    "icon": "{root}/resources/icon.png"
}

requires = [
    # pipeline
    "merlin",
    "reveries",
    # pipeline tools
    "~avalon",

    # Apps
    "~maya-2018|2020",

    # utils
    "~terminal-1",
]


@late()
def project_document():
    import os
    from pymongo import MongoClient
    this = globals()["this"]

    client = MongoClient(os.environ["AVALON_MONGO"])
    db = client[os.environ["AVALON_DB"]]
    col = db[this.name]

    return col.find_one({"type": "project"})


@late()
def project_inventory():
    this = globals()["this"]
    return this.project_document["data"]


@late()
def project_config():
    this = globals()["this"]
    return this.project_document["config"]


@late()
def is_project_admin():
    import getpass
    this = globals()["this"]
    admins = this.project_inventory.get("role", {}).get("admin", [])
    everyone = not admins
    assigned = getpass.getuser().lower() in admins
    return everyone or assigned


@late()
def roles():
    this = globals()["this"]
    return this.project_inventory.get("role", {}).get("member", [])


views = [
    # List out features of this profile,
    # e.g. "show.ongoing", "dev.pipeline", ...
]


# Set up environment
def commands():
    env = globals()["env"]
    this = globals()["this"]

    # Project setup
    env.AVALON_PROJECTS = this.project_inventory["root"]
    env.AVALON_PROJECT = this.name


"""
!!! Do not change following attributes !!!
"""
filesystem_root = os.getcwd()  # for mongozark repository
build_command = False
ozark_profile = True
no_variants = True
