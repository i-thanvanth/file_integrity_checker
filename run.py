import PySimpleGUI as pygui
import os
pygui.theme('reddit')
layout = [[pygui.T("Hello, Welcome to T's hash checker app")],  [pygui.Button("Create hash of a file")],[pygui.Button("Check the file integrity(hash required)")]]
window = pygui.Window("T's file integrity checker", layout)
event, values = window.read()
if event == "Create hash of a file":
    path=os.path.dirname(__file__)+"/hash_create.py"
    os.system("python {}".format(path))
elif event == "Check the file integrity(hash required)":
    path=os.path.dirname(__file__)+"/hash_compare.py"
    os.system("python {}".format(path))