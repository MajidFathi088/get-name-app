#custom functions to reduce te repetitive codes

def get_names(filepath="names.txt"):   #make a default parameter
    """ Read the names and return a list of the names """
    with open(filepath, "r") as file_local:
        names_local = file_local.readlines()
    return [name.strip() for name in names_local]

def write_names(names_local, filepath="names.txt"):
    """ Write the names to the file """
    with open(filepath, "w") as file_local:
        file_local.writelines([name + "\n" for name in names_local])
#no need to return anything

