import os

file_path = "C:/Users/JT/annotation-tool/Images/"
folder_names = os.listdir(file_path)

for folder_name in folder_names:
    path = file_path + folder_name
    file_names = os.listdir(path)

    for idx, name in enumerate(file_names, 1):
        scr = os.path.join(path, name)
        dst = str(idx) + '.jpg'
        dst = os.path.join(path, dst)
        os.rename(scr, dst)
