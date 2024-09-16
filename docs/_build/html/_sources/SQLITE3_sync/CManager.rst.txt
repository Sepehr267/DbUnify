CManager
========

This module is responsible for managing synchronous database operations. Use C.

CManager
--------

.. automodule:: DbUnify.SQLite3.sync.CManager.CManager
   :members:
   :undoc-members:
   :show-inheritance:


CManager Core
--------

**CMCoreBuilder**

.. automodule:: DbUnify.SQLite3.sync.CManager.Core.CoreBuilder
   :members:
   :undoc-members:
   :show-inheritance:

The `CMCoreBuilder` class in the CManager Core module is responsible for managing and building the core library for the CManager system. This involves compiling and linking the core library for different operating systems: Linux and Windows. To successfully build the core library, GCC (GNU Compiler Collection) must be installed on your system.

Installing GCC
--------

**Installing GCC on Linux**

1. **Update Package Lists**
   Open your terminal and update the package lists:

   .. code-block:: bash

      sudo apt update

2. **Install GCC and G++**
   Install GCC and G++ using the package manager:

   .. code-block:: bash

      sudo apt install gcc g++

3. **Verify Installation**
   Check that GCC is installed correctly by verifying its version:

   .. code-block:: bash

      gcc --version

   You should see the version of GCC installed.

**Installing GCC on Windows**

1. **Download MinGW**
   Go to the MinGW website and download the installer:
   [MinGW Download](https://sourceforge.net/projects/mingw-w64/files/latest/download)

2. **Run the Installer**
   Run the downloaded installer and follow the prompts to install MinGW. Make sure to select the GCC component during installation.

3. **Add MinGW to PATH**
   After installation, you need to add MinGW to your system PATH:
   
   - **Open System Properties**
     Right-click on "This PC" or "Computer" on your desktop or in File Explorer, and select "Properties." Click on "Advanced system settings."

   - **Edit Environment Variables**
     In the System Properties window, click on the "Environment Variables" button.

   - **Update PATH Variable**
     In the Environment Variables window, find and select the `PATH` variable in the "System variables" section, then click "Edit."

   - **Add MinGW Bin Directory**
     Add the path to the MinGW `bin` directory to the `PATH` variable. The default path is usually `C:\MinGW\bin`. Add this path and click "OK" to save.

4. **Verify Installation**
   Open Command Prompt and check that GCC is installed correctly:

   .. code-block:: cmd

      gcc --version

   You should see the version of GCC installed.

By following these instructions, you will ensure that GCC is installed and properly configured on your system, enabling you to build the CManager core library successfully.


CMCore
--------

Get the path of the CManager Core for your operating system.

.. automodule:: DbUnify.SQLite3.sync.CManager.Core.CMCore
   :members:
   :undoc-members:
   :show-inheritance:

Create Core
--------

**Build Core**

Use Class `CMCoreBuilder` create your own Core CManager for your System 

.. code-block:: python

    from DbUnify.SQLite3.sync import CMCoreBuilder

    builder = CMCoreBuilder()
    builder.build_core()

Examples CManager
--------

**Connect to Database**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    manager.connect_db('database.db')


**Create a table**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    manager.create_table(
        "users",
        [
            ('id', 'INTEGER', ['NOT NULL', 'PRIMARY KEY']),
            ('name', 'TEXT', ['NOT NULL']),
            ('email', 'TEXT', ['UNIQUE'])
        ]
    )


**Insert a row**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    manager.insert_row("users", {
        'name': 'John Doe',
        'email': "john.doe@example.com"
    })


**Fetch all (Select)**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    data = manager.fetch_all('select * from users')
    print(data)


**Update a row**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    manager.update_row("users", {'email': 'john.doe@newdomain.com'}, "name = 'John Doe'")
    

**Delete a row**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    manager.delete_row("users", "name = 'John Doe'")


**Drop Table**

.. code-block:: python

    from DbUnify.SQLite3.sync.CManager import CManager, get_core

    manager = CManager(get_core())

    manager.drop_table("users")

