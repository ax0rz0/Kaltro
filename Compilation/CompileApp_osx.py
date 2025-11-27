from setuptools import setup

APP = ["Main.py"]
OPTIONS = {"argv_emulation": True, "includes": ["tkinter"]}

setup(
    app=APP,
    options={"py2app": OPTIONS},
)
