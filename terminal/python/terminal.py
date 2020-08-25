
import os
import stat
import subprocess
from rez.system import system


def spawn(with_rez=True):
    env = os.environ.copy()

    if with_rez:
        env["PATH"] = os.path.pathsep.join(
            [os.environ["REZ_CORE_BIN_PATH"], os.environ["PATH"]])

    if system.platform == "windows":
        subprocess.call(["start"], shell=True, env=env)

    elif system.platform == "osx":
        with open("tempenv", "w") as tempenv:
            for key, value in env.items():
                tempenv.write("export %s=%s\n" % (key, value))
            tempenv.write(system.shell)
        st = os.stat("tempenv")
        os.chmod("tempenv", st.st_mode | stat.S_IEXEC)
        subprocess.call(["open", "-a", "Terminal", "tempenv"])

    elif system.platform == "linux":
        raise NotImplementedError


if __name__ == "__main__":
    spawn()
