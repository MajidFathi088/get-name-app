import functions
import FreeSimpleGUI as sg


lable = sg.Text("Enter your name: ")
input_box = sg.InputText(tooltip="enter your name: ", key="name")
add_button = sg.Button("Add")

window = sg.Window("The App",
                   layout=[[[lable], [input_box, add_button]]],
                   font=('Helvetica', 12),)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            names = functions.get_names()
            new_name = values["name"] + "\n"
            names.append(new_name)
            functions.write_names(names)
        case sg.WINDOW_CLOSED:
            break


window.close()