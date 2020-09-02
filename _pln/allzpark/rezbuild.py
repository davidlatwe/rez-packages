
import os
import sys
import shutil
import subprocess


def build(source_path, build_path, install_path, targets=None):
    __allzparksrc = os.environ["_GIT_CLONED_SRC_PATH"]
    targets = targets or []

    if "install" in targets:
        dst = install_path
    else:
        dst = build_path

    dst = os.path.normpath(dst)

    if os.path.isdir(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    args = ["python", "setup.py", "build", "--build-base", dst]
    subprocess.check_call(args, cwd=__allzparksrc)

    for dirname in ["bin"]:
        dir_src = os.path.join(source_path, dirname)
        dir_dst = os.path.join(dst, dirname)
        shutil.copytree(dir_src, dir_dst)


if __name__ == "__main__":
    build(source_path=os.environ["REZ_BUILD_SOURCE_PATH"],
          build_path=os.environ["REZ_BUILD_PATH"],
          install_path=os.environ["REZ_BUILD_INSTALL_PATH"],
          targets=sys.argv[1:])
