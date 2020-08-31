
import os
import contextlib
from avalon import api, io, pipeline, lib


@contextlib.contextmanager
def patch(owner, attr, value):
    """Monkey patch context manager.

    with patch(os, 'open', my_open):
        ...
    """
    old = getattr(owner, attr)
    setattr(owner, attr, value)
    try:
        yield getattr(owner, attr)
    finally:
        setattr(owner, attr, old)


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

    session = api.Session
    session["AVALON_SILO"] = "_"  # required by workfile app
    session["AVALON_SILO"] = "_"  # required by workfile app
    session["AVALON_ASSET"] = "_Lobby"
    session["AVALON_TASK"] = "_general"

    def mock_find(*args, **kwargs):
        lobby = {"work": "{root}/{project}/Avalon/{asset}/{task}/{app}"}
        return {"data": {}, "config": {"template": lobby}}

    with patch(io, "find_one", mock_find):
        app = App()
        env = app.environ(session)
        app.initialize(env)

    lib.launch(
        executable=app_name,
        args=app.config.get("args", []),
        environment=env,
        cwd=env["AVALON_WORKDIR"]
    )


if __name__ == "__main__":
    init_workdir()
