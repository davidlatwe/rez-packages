
import os
from avalon import api, io, pipeline, lib


def init_workdir():
    io.install()

    app_name = os.environ["AVALON_APP"]
    app_definition = pipeline.lib.get_application(app_name)
    App = type(
        "app_%s" % app_name,
        (pipeline.Application,),
        {
            "name": app_name,
            "config": app_definition.copy()
        }
    )

    # Initialize within the new session's environment
    app = App()
    env = app.environ(api.Session)
    app.initialize(env)

    lib.launch(
        executable=app_name,
        args=app.config.get("args", []),
        environment=env,
        cwd=env["AVALON_WORKDIR"]
    )


if __name__ == "__main__":
    init_workdir()
