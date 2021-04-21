import os

start_dir = os.path.abspath(".")

SKIP = ['.git', '.idea', '__pycache__']

for folder_path, folder_names, file_names in os.walk(start_dir):
    for skip in SKIP:
        if skip in folder_names:
            folder_names.remove(skip)
    print(folder_path)
    for file_name in file_names:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder_path, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")


