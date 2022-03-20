import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "PySimpleGUI", "pygame", "json"], "include_files": ["img\\6103903.ico","img\\Cyber-Security.ico", "img\\cyber-security-icon1.ico", "img\\cyber-security-2303512-1951575.ico", "img\\cyber-security-2303512-1951575.ico", "img\\CyberManager-intro_demo.gif", "img\\Cyber Manager.gif", "utils/som_tempo.mp3"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CyberManager",
    version="0.1",
    description="É um programa que serve para controlar o tempo de uso da máquina enquanto\no cliente usufrui do tempo que lhe foi confiado no Computador ou da Internet.!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="img\\6103903.ico")]
)
