from setuptools import setup

VERSION = "0.0.1"
APP = ["localobject.py"]
DATA_FILES = ["LICENSE", "README.md"]
OPTIONS = {
    "argv_emulation": True,
    "plist": {
        "LSUIElement": True,
    },
    "packages": ["rumps"],
}

setup(
    app=APP,
    version=VERSION,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
