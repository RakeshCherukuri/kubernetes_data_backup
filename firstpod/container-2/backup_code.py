import os
from shutil import copyfile

source_directory = '/'
destination_directory = '/myvol/'

source_path_and_file = os.path.join(source_directory,file)
destination_path_and_file = os.path.join(destination_directory,file)
for file in os.listdir(source_directory):
    try:
        print(file)
        os.rename(source_path_and_file,source_path_and_file)
        if  not os.path.exists(destination_path_and_file):
            copyfile(source_path_and_file,destination_path_and_file)

    except OSError as e:
        print(e)
        continue
    