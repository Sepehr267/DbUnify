Exporter
=========

This module provides functionalities for exporting data from a MySQL database to various formats in synchronous contexts.

.. automodule:: DbUnify.MySQL.sync.Exporter.Exporter
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------------------

First, import the necessary modules and initialize the `Exporter` class.

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Exporter import Exporter

    def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        manager.connect()
        exporter = Exporter(manager)

    main()

**Export Chart Database**

Create charts for all tables in the database and save them as images.

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Exporter import Exporter

    def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        manager.connect()
        exporter = Exporter(manager)
        exporter.export_chart_database(
            output_directory='charts',
            chart_type='bar',
            x_label='X Axis',
            y_label='Y Axis')

    main()

**Export Chart Table**

Create a chart from data in a specific table and save it as an image.

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Exporter import Exporter

    def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        manager.connect()
        exporter = Exporter(manager)
        exporter.export_chart_table(
            table_name='user',
            x_column=0,
            y_column=1,
            x_label='User ID',
            y_label='Age',
            title='User Age Distribution',
            save_path='charts/user_age_distribution.png',
            chart_type='bar'
        )

    main()

**Export Data to CSV**

Export data from a table to a CSV file synchronously.

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Exporter import Exporter

    def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        manager.connect()
        exporter = Exporter(manager)
        exporter.export_data_csv(
            table_name='users',
            csv_file_path='data',
            csv_file_name='users_data'
        )

    main()
