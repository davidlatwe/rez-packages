
import os
ModifyList = globals()["ModifyList"]


# Location: avalon
__avalon_uri = os.getenv("OZARK_MONGODB_AVALON",
                         "localhost:27017")
__avalon_loc = os.getenv("OZARK_LOCATION_AVALON",
                         "mongozark@avalon.rez.avalon")


__profiles_path = [
    __avalon_loc,
]
packages_path = ModifyList(append=__profiles_path)


plugins = {
    "package_repository": {
        "mongozark": {
            "uri": {
                "avalon": __avalon_uri,
            },
            "location": {
                "avalon": __avalon_loc,
            },
            "profiles": __profiles_path,
        },
    }
}
