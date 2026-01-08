import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkGrey')

clock = sg.Text("", key='clock')
lable = sg.Text("Enter your name: ")
input_box = sg.InputText(tooltip="enter your name: ", key="name", size=(20, 1))
list_box = sg.Listbox(functions.get_names(), key="listbox", enable_events=True, size=(20, 10))
edit_button = sg.Button("Edit", size=(5, 1))
add_button = sg.Button("Add", size=(8, 1))
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window = sg.Window("The App",
                   layout=[[[clock],
                            [lable],
                            [input_box, add_button],
                            [list_box, sg.Column([[edit_button], [delete_button]])],
                            [exit_button]]],
                   font=('Helvetica', 12),)

while True:
    event, values = window.read(timeout=500)
    if event == sg.WIN_CLOSED:
        break
    window['clock'].update(value=time.strftime("%b %d, %y -%H:%M:%S"))

    match event:
        case "Add":
            new_name = values["name"].strip()
            if new_name:
                names = functions.get_names()
                names.append(new_name + "\n")
                functions.write_names(names)
                window["listbox"].update(values=names)
                window["name"].update("")
            else:
                sg.popup("Name cannot be empty", font=('Helvetica', 12))

        case "Edit":
            try:
                name_to_edit = values['listbox'][0]
                new_name = values['name'] + '\n'

                names = functions.get_names()
                index = names.index(name_to_edit)
                names[index] = new_name
                functions.write_names(names)
                window["listbox"].update(values=names)
            except IndexError:
                sg.popup("Please select a name.", font=('Helvetica', 12))

        case "Delete":
            try:
                name_to_delete = values['listbox'][0]
                names = functions.get_names()
                names.remove(name_to_delete)
                functions.write_names(names)
                window["listbox"].update(values=names)
                window["name"].update(value="")
            except IndexError:
                sg.popup("Please select a name.", font=('Helvetica', 12))

        case "Exit":
            break

        case "listbox":
            window["name"].update(value=values["listbox"][0])
        case sg.WINDOW_CLOSED:
            break


window.close()