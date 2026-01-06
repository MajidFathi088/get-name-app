import functions
import FreeSimpleGUI as sg

lable = sg.Text("Enter your name: ")
input_box = sg.InputText(tooltip="enter your name: ")
add_button = sg.Button("Add")

window = sg.Window("The App", layout=[[[lable], [input_box, add_button]]])
window.read()
window.close()