
import os
ModifyList = globals()["ModifyList"]


# Location: avalon
__avalon_uri = os.getenv("OZARK_MONGODB_AVALON",
                         "localhost:27017")
__avalon_loc = os.getenv("OZARK_LOCATION_AVALON",
                         "mongozark@avalon.rez.avalon")

packages_path = ModifyList(append=[__avalon_loc])

plugins = {
    "package_repository": {
        "mongozark": {
            "uri": {
                "avalon": __avalon_uri,
            },
            "location": {
                "avalon": __avalon_loc,
            },
            "profiles": ModifyList(append=[__avalon_loc]),
        },
    }
}
