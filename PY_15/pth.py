import os


# start_path = os.getcwd()
# print(start_path)
# os.chdir('..')
# print(os.getcwd())
def folder_include(path_to_folder):
    disc_fold =  os.walk(path_to_folder)
    for i in disc_fold:
        print(i)

print(folder_include(r'C:\Users\Oleg\Desktop\skillfactory\PY_15'))
