import platform
import os
import sys

def get_core() -> str:
    """
    Returns the full path to the core library file based on the operating system.
    
    On Linux, it searches for a '.so' file in the 'core' folder.
    On Windows, it searches for a '.dll' file in the 'core' folder.
    
    Raises an Exception if the operating system is unsupported or no matching file is found.
    """
    system = platform.system()
    core_dir = os.path.dirname(os.path.abspath(__file__))

    if system == 'Linux':
        file_extension = '.so'
    elif system == 'Windows':
        file_extension = '.dll'
    else:
        print("\033[31m[CManager] Unsupported operating system\033[0m", file=sys.stderr)
        raise Exception("[CManager] Unsupported operating system")

    for file_name in os.listdir(core_dir):
        if file_name.endswith(file_extension):
            return os.path.join(core_dir, file_name)

    print(f"\033[31m[CManager] No core file with {file_extension} extension found.\033[0m", file=sys.stderr)
    pass

