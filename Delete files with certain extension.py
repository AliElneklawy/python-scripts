import os

dir_name = input("Enter the path: ")
ext = input("Delete extensions: ")

files_in_directory = os.listdir(dir_name)
filtered_files = [file for file in files_in_directory if file.endswith(f".{ext}")]
for file in filtered_files:
	path_to_file = os.path.join(dir_name, file)
	os.remove(path_to_file)