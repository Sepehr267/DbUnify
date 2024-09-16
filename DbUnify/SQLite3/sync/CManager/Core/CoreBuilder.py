from .CMCore import get_core
import platform
import os
import ctypes
import subprocess
import sys

class CMCoreBuilder:
    """
    CMCoreBuilder (CManager Core Builder) is responsible for managing and building the core library for different operating systems.
    
    This class checks the compatibility of the existing core library file (either on Linux or Windows),
    and if the library is missing or incompatible, it compiles and builds the library using the appropriate
    compiler (GCC) based on the detected operating system. For Linux, it builds a shared object (.so), 
    and for Windows, it builds a dynamic-link library (.dll).
    
    The class uses ctypes to check if the library is compatible and subprocess to run the compilation commands.
    It also handles OS-specific file naming conventions, includes system architecture in output files, and links
    to required libraries like SQLite and Python.
    """

    def __init__(self):
        """
        Initializes the CMCoreBuilder class by setting the core library path and base directory.
        It then proceeds to check the compatibility of the core library file and builds it if necessary.
        """
        self.core_path = get_core()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        # self.__check_and_build()

    def __check_and_build(self):
        """
        Checks if the core library file is compatible by verifying its existence and loading it via ctypes.
        If the core file is missing or incompatible, it initiates the build process.
        """
        if self.__is_core_file_compatible():
            print(f"\033[32m[CMCoreBuilder] Core library file is compatible: {self.core_path}\033[0m")
        else:
            print(f"\033[31m[CMCoreBuilder] Core library file is not compatible or missing.\033[0m")
            self.build_core()


    def __is_core_file_compatible(self):
        """
        Determines whether the core library file is compatible or not.
        
        Returns:
            bool: True if the file exists and can be loaded using ctypes, otherwise False.
        """
        if not os.path.isfile(self.core_path):
            return False

        try:
            ctypes.CDLL(self.core_path)
            return True
        except OSError:
            return False

    def build_core(self):
        """
        Initiates the build process for the core library based on the current operating system.
        If the system is Linux, it calls the compile_linux method.
        If the system is Windows, it calls the compile_windows method.
        Otherwise, it prints an unsupported OS message.
        """
        system = platform.system()
        if system == 'Linux':
            self.compile_linux()
        elif system == 'Windows':
            self.compile_windows()
        else:
            print(f"\033[33m[CMCoreBuilder] Unsupported operating system\033[0m")

    def compile_linux(self):
        """
        Compiles the core library for Linux systems using the GCC compiler. The source files manager.c and cache.c are
        compiled and linked to produce a shared object (.so) file. The final output is saved as a Linux-specific shared
        library file.
        
        If the build succeeds, a success message is printed, otherwise an error message is displayed.
        """
        manager_c = os.path.join(self.base_dir, 'Base', 'manager.c')
        cache_c = os.path.join(self.base_dir, 'Base', 'cache.c')
        output_so = os.path.join(self.base_dir, 'CManager-Linux-Debian-v2.2.0.so')

        command = [
            'gcc',
            '-shared', '-o', output_so,
            '-fPIC', '-O3',
            manager_c, cache_c,
            '-lsqlite3'
        ]

        try:
            subprocess.run(command, check=True)
            print(f"\033[32m[CMCoreBuilder] Build complete for Linux: {output_so}\033[0m")
        except subprocess.CalledProcessError as e:
            print(f"\033[31m[CMCoreBuilder] Error running build command: {e}\033[0m")

    def __get_windows_architecture(self):
        """
        Returns the architecture of the current Windows operating system (either 'x64' for 64-bit or 'x86' for 32-bit).
        
        Returns:
            str: 'x64' if the system is 64-bit, 'x86' if it is 32-bit, or 'Unknown' if the architecture cannot be determined.
        """
        arch = platform.architecture()[0]
        if arch == '64bit':
            return 'x64'
        elif arch == '32bit':
            return 'x86'
        else:
            return 'Unknown'

    def compile_windows(self):
        """
        Compiles the core library for Windows systems using the GCC compiler. The source files manager.c and cache.c
        are compiled and linked to produce a shared dynamic-link library (.dll). It also links against the Python and
        SQLite libraries. The final output file is named according to the system architecture (x64 or x86).
        
        If the build succeeds, a success message is printed, otherwise an error message is displayed.
        
        Raises:
            FileNotFoundError: If the required Python library file cannot be found in the Python installation directory.
        """
        manager_c = os.path.join(self.base_dir, 'Base', 'manager.c')
        cache_c = os.path.join(self.base_dir, 'Base', 'cache.c')
        sqlite3_h_dir = os.path.join(self.base_dir, 'Base')
        sqlite3_lib = os.path.join(self.base_dir, 'Base', 'sqlite3.lib')

        python_install_dir = os.path.dirname(sys.executable)
        python_libs_dir = os.path.join(python_install_dir, 'libs')

        lib_files = [f for f in os.listdir(python_libs_dir) if f.startswith('python') and f.endswith('.lib')]
        if lib_files:
            python_lib_file = lib_files[0]
        else:
            print(f"\033[31m[CMCoreBuilder] Python library file not found in the expected directory.\033[0m")
            raise FileNotFoundError("Python library file not found in the expected directory.")

        architecture = self.__get_windows_architecture()

        output_dll = os.path.join(self.base_dir, f'CManager-Windows-{architecture}-v2.2.0.dll')

        command = [
            'gcc',
            '-shared', '-o', output_dll,
            '-I', sqlite3_h_dir,
            manager_c, cache_c,
            sqlite3_lib,
            '-L', sqlite3_h_dir, '-lsqlite3',
            '-L', python_libs_dir, f'-l{python_lib_file[:-4]}'
        ]

        try:
            subprocess.run(command, check=True)
            print(f"\033[32m[CMCoreBuilder] Build complete for Windows: {output_dll}\033[0m")
        except subprocess.CalledProcessError as e:
            print(f"\033[31m[CMCoreBuilder] Error running build command: {e}\033[0m")
