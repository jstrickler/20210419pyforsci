import os  # also imports os.path

folder = 'DATA'
data_files = os.listdir(folder)
# print(data_files)

for file_name in data_files:
    file_path = os.path.join(folder, file_name)
    file_size = os.path.getsize(file_path)
    print(f"{file_size:8d} {file_name}")
