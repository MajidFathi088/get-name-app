#from functions import get_names, write_names     #we use it when we have 2-3 functions to riffer

import functions  #import every f-unctions and riffer by call it like methods like functions.get_names()
import time

now = time.strftime("%d/%m/%Y %I:%M:%S %p")
print(now)


while True:
    user_action = input("Enter your action: (add,show,exit,edit, remove) ")
    user_action = user_action.strip()
    #match user_action:
    #we change the match case with if else
        #case 'add':
    if user_action.startswith("add"):     #if 'add' in user_action :  better method to handle the bug
        #name = input("please enter your name:") + "\n"

        name = user_action[4:]

        #file = open("names.txt", "r")
        #names = file.readlines()
        #file.close()


        #with open("names.txt", "r") as file:
            #names = file.readlines()

        names = functions.get_names()    #use the custom function instead of above two lines
        #default parameter doesn't need an argument to send, just if you want to change it

        names.append(name.title() + '\n')

        #file = open("names.txt", "w")
        #file.writelines(names)
        #file.close()

        #with open("names.txt", "w") as file:
            #file.writelines(names)
        functions.write_names(names)   #use the custom function instead of above two lines
        #no need to assume the result to a variable

    #case 'show':
    elif user_action.startswith("show"):    #elif 'show' in user_action :  better method to handle the bug
        #file = open("names.txt", "r")
        #names = file.readlines()
        #file.close()

        # with these lines you can reduce the open lines for files instead of above lines

        #with open("names.txt", "r") as file:
            #names = file.readlines()
        names = functions.get_names()    #use the custom function instead of above two lines


        #new_names = []
        #for name in names:
        #    new_name = name.strip('\n')
        #    new_names.append(new_name)

        #or we can use this single line here

        #new_names = [names.strip('\n') for names in names]

        #or we can just use strip method on name variable like in line 34

        for i,name in enumerate(names): #in case of using above code lines we should use new_names list as argument
            name = name.strip('\n')  #to remove the break line or \n
            row = f"{i + 1}.{name}"
            print(row.title())
    #case 'edit':
    elif user_action.startswith("edit"):    # elif 'edit' in user_action :   better method to handle the bug
        try:    #to fix the error that maybe user cause of it
            #name_num = int(input("please enter the number of the name you want to change:"))
            name_num = int(user_action[5:])
            name_num = name_num - 1

            #with open("names.txt", "r") as file:
                #names = file.readlines()
            names = functions.get_names()  # use the custom function instead of above two lines

            new_name = input("please enter the new name:")
            names[name_num] = new_name + '\n'


            #with open("names.txt", "w") as file:
                #file.writelines(names)
            functions.write_names( names)  # use the custom function instead of above two lines
            # no need to assume the result to a variable


        except ValueError:    #specifid the error type
            print("Invalid input")
            continue   #goes back to the first line and executes again

    #case 'remove':
    elif user_action.startswith("remove"):    #elif 'remove' in user_action :   better method to handle the bug
        try:
            #name_num = int(input("please enter the number of the name you want to remove:"))
            name_num = int(user_action[7:])

            #with open("names.txt", "r") as file:
                #names = file.read()
            names = functions.get_names()  # use the custom function instead of above two lines

            name_to_remove = names[name_num - 1].strip('\n')
            names.pop(name_num - 1)


            #with open("names.txt", "w") as file:
                #file.writelines(names)
            functions.write_names(names)  # use the custom function instead of above two lines
            # no need to assume the result to a variable
            

            massage = rf"Name {name_num} was successfully removed."
            print(massage)
        except IndexError:
            print("Invalid input")
            continue 
    #case 'exit':
    elif user_action.startswith("exit"):     #elif 'exit' in user_action :   better method to handle the bug
        break
    #case _:
    else:
        print("please enter a valid input")
print("Bye!")