import functions
import FreeSimpleGUI as sg


lable = sg.Text("Enter your name: ")
input_box = sg.InputText(tooltip="enter your name: ", key="name", size=(20, 1))
list_box = sg.Listbox(functions.get_names(), key="listbox", enable_events=True, size=(20, 10))
edit_button = sg.Button("Edit")
add_button = sg.Button("Add")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window = sg.Window("The App",
                   layout=[[[lable],
                            [input_box, add_button],
                            [list_box, edit_button, delete_button],
                            [exit_button]]],
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
            window["listbox"].update(names)

        case "Edit":
            name_to_edit = values['listbox'][0]
            new_name = values['name'] + '\n'

            names = functions.get_names()
            index = names.index(name_to_edit)
            names[index] = new_name
            functions.write_names(names)
            window["listbox"].update(values=names)

        case "Delete":
            name_to_delete = values['listbox'][0]
            names = functions.get_names()
            names.remove(name_to_delete)
            functions.write_names(names)
            window["listbox"].update(values=names)
            window["name"].update(value="")

        case "Exit":
            break

        case "listbox":
            window["name"].update(value=values["listbox"][0])
        case sg.WINDOW_CLOSED:
            break


window.close()