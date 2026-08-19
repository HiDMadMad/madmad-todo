import os
import subprocess
import shutil
import sys


VERSION = "0.2.0"
APP_NAME = f"CheckMate-v{VERSION}"

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SRC_DIR)
RELEASE_DIR = os.path.join(PROJECT_ROOT, f"{APP_NAME}")

APP_ENTRY = os.path.join(SRC_DIR, "app.py")
ICON_PATH = os.path.join(PROJECT_ROOT, "assets", "icon.ico")

BUILD_WORK_DIR = os.path.join(PROJECT_ROOT, "build_temp")  # pyinstaller temp files
SPEC_DIR = BUILD_WORK_DIR


def check_paths():
    missing = []
    if not os.path.exists(APP_ENTRY):
        missing.append(APP_ENTRY)
    if not os.path.exists(ICON_PATH):
        missing.append(ICON_PATH)
    if missing:
        print("error: the following paths were not found:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)

def build():
    check_paths()
    cmd = [
        "pyinstaller",
        "--onefile",
        "--console",
        f"--icon={ICON_PATH}",
        f"--name={APP_NAME}",
        f"--distpath={RELEASE_DIR}",
        f"--workpath={BUILD_WORK_DIR}",
        f"--specpath={SPEC_DIR}",
        "--paths", SRC_DIR,
        APP_ENTRY,
    ]

    print("running:", " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("build failed.")
        sys.exit(result.returncode)

    release_data_dir = os.path.join(RELEASE_DIR, "data")
    os.makedirs(os.path.join(release_data_dir, "exported-data"), exist_ok=True)

    if os.path.exists(BUILD_WORK_DIR):
        shutil.rmtree(BUILD_WORK_DIR)

    print("\nbuild completed successfully.")
    print(f"output: {os.path.join(PROJECT_ROOT, APP_NAME)}.exe")


if __name__ == "__main__":
    build()
#MadMad_66