from distutils.core import setup
import py2exe

setup(
    windows=["Main.py"],
    options={
        "py2exe": {
            "includes": ["tkinter"]
        }
    }
)
