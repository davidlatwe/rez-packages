
import os
import stat
import tempfile
import subprocess
from rez.system import system


def spawn():
    env = os.environ.copy()

    # Include rez command line tools
    env["PATH"] = os.path.pathsep.join(
        [os.environ["REZ_CORE_BIN_PATH"], os.environ["PATH"]])

    if system.platform == "windows":
        subprocess.call(["start"], shell=True, env=env)

    elif system.platform == "osx":
        env.pop("REZ_STORED_PROMPT_SH", None)

        with tempfile.NamedTemporaryFile("w", delete=False) as temp:
            lines = list()
            for key, value in env.items():
                lines.append("export %s=\"%s\"" % (key, value))

            lines.append("rm %s" % temp.name)  # self cleanup
            lines.append(system.shell)  # keep shell window open

            temp.write("\n".join(lines))

        st = os.stat(temp.name)
        os.chmod(temp.name, st.st_mode | stat.S_IEXEC)

        subprocess.call(["open", "-a", "Terminal", temp.name])

    elif system.platform == "linux":
        raise NotImplementedError


if __name__ == "__main__":
    spawn()
