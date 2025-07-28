import os

def create_folder(dir_path, folder_name):
    try:
        if os.path.exists(dir_path):
            target_path = os.path.join(dir_path, folder_name)
            os.mkdir(target_path)
            print(f"Folder '{folder_name}' created at: {target_path}")
        else:
            print(f"Directory '{dir_path}' does not exist!")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists at '{dir_path}'!")
    except Exception as e:
        print(f"An error occurred: {e}")

create_folder("E:\\", "IloveYou")         