Exporter
=========

This module provides functionalities for exporting data in synchronous contexts.

.. automodule:: DbUnify.SQLite3.sync.Exporter
   :members:
   :undoc-members:
   :show-inheritance:

Exporter Class
--------------

**Exporter** provides methods to export data from a database to various formats such as charts (images) and CSV files.

.. autoclass:: DbUnify.SQLite3.sync.Exporter.Exporter
   :members:
   :undoc-members:
   :show-inheritance:

**Attributes:**

- `manager (Manager)`: The Manager instance managing the database connection.
- `raw (Raw)`: An instance of the Raw class for executing raw SQL queries.

**Methods:**

**__init__**

Initialize the Exporter instance with a Manager instance.

.. code-block:: python

    from DbUnify.SQLite3.sync.Exporter import Exporter
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Exporter
    manager = Manager(db_name='example.db')
    exporter = Exporter(manager=manager)

**export_chart_database**

Create charts for all tables in the database and save them as images.

.. code-block:: python

    from DbUnify.SQLite3.sync.Exporter import Exporter
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Exporter
    manager = Manager(db_name='example.db')
    exporter = Exporter(manager=manager)
    
    # Export charts for all tables
    exporter.export_chart_database(output_directory='charts/', chart_type='bar', x_label='X Axis', y_label='Y Axis')

**export_chart_table**

Create a chart from data in a specific table and save it as an image.

.. code-block:: python

    from DbUnify.SQLite3.sync.Exporter import Exporter
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Exporter
    manager = Manager(db_name='example.db')
    exporter = Exporter(manager=manager)

    # Export chart from a specific table
    exporter.export_chart_table(
        table_name='user',
        x_column=0,
        y_column=1,
        x_label='Month',
        y_label='Revenue',
        title='Monthly Sales Revenue',
        save_path='sales_chart.png',
        chart_type='line'
    )


**export_data_csv**

Export data from a table to a CSV file.

.. code-block:: python

    from DbUnify.SQLite3.sync.Exporter import Exporter
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Exporter
    manager = Manager(db_name='example.db')
    exporter = Exporter(manager=manager)

    # Export table data to a CSV file
    exporter.export_data_csv(table_name='employees', csv_file_path='data/employees.csv')

Exceptions
-----------

**RuntimeError**

Raised if there is an error creating charts or saving them as images, or during CSV data export.

**Exception**

Raised if there is an error during data export.

Examples
--------

**Exporting Charts and Data**

This example demonstrates how to use the `Exporter` class to export database data as charts and CSV files.

.. code-block:: python

    from DbUnify.SQLite3.sync.Exporter import Exporter
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Exporter
    manager = Manager(db_name='example.db')
    exporter = Exporter(manager=manager)

    # Export charts for all tables in the database
    try:
        exporter.export_chart_database(output_directory='charts/', chart_type='bar', x_label='X Axis', y_label='Y Axis')
    except RuntimeError as e:
        print(f"Error exporting charts: {e}")

    # Export a specific table's chart
    try:
        exporter.export_chart_table(
            table_name='sales',
            x_column=0,
            y_column=1,
            x_label='Month',
            y_label='Revenue',
            title='Monthly Sales Revenue',
            save_path='sales_chart.png',
            chart_type='line'
        )
    except RuntimeError as e:
        print(f"Error exporting chart for table 'sales': {e}")

    # Export data to a CSV file
    try:
        exporter.export_data_csv(table_name='employees', csv_file_path='data/employees.csv')
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")
