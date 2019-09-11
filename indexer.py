import index_file, folder_reader, os

dir_path = os.path.dirname(os.path.realpath(__file__))

files = folder_reader.get_files(dir_path)

for file in files:
    index_file(file, file)