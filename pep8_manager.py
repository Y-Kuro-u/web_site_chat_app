import os
import glob


def auto_pep(file_path):
    file_list = glob.glob(file_path + "/*")
    for file_name in file_list:
        if os.path.isfile(file_name):
            if file_name.split(".")[-1] == "py":
                os.system("autopep8 -i -a " + file_name)
            else:
                continue
        elif os.path.isdir(file_name):
            auto_pep(file_name)
        else:
            continue


auto_pep(".")
