import os
import shutil

def delete_pycache(path):
    """
    Recursively delete all __pycache__ directories from the specified path.

    Args:
        path (str): The root path to start searching for __pycache__ directories.
    """
    try:
        # Walk through the directory
        for root, dirs, files in os.walk(path, topdown=False):
            for dir_name in dirs:
                if dir_name == '__pycache__':
                    dir_path = os.path.join(root, dir_name)
                    shutil.rmtree(dir_path)  # Remove __pycache__ directory and all its contents
                    print(f'Deleted {dir_path}')
    except PermissionError:
        print('Permission Denied')

if __name__ == "__main__":
    root_path = '.'  # Change this to the path of the directory you want to clean
    delete_pycache(root_path)
