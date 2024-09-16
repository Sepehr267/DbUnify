Exporter
=========

This module provides functionalities for exporting data in asynchronous contexts.

.. automodule:: DbUnify.SQLite3.aio.Exporter.Exporter
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------------------

First, import the necessary modules and initialize the `Exporter` class.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Exporter import Exporter

    async def main():
        manager = Manager(db_name='example.db')
        exporter = Exporter(manager)

    asyncio.run(main())

**Export Chart Database**

Create charts for all tables in the database and save them as images.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Exporter import Exporter

    async def main():
        manager = Manager(db_name='example.db')
        exporter = Exporter(manager)
        await exporter.export_chart_database(output_directory='charts', chart_type='bar', x_label='X Axis', y_label='Y Axis')

    asyncio.run(main())

**Export Chart Table**

Create a chart from data in a specific table and save it as an image.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Exporter import Exporter

    async def main():
        manager = Manager(db_name='example.db')
        exporter = Exporter(manager)
        await exporter.export_chart_table(
            table_name='users',
            x_column=0,
            y_column=1,
            x_label='User ID',
            y_label='Age',
            title='User Age Distribution',
            save_path='charts/user_age_distribution.png',
            chart_type='bar'
        )

    asyncio.run(main())

**Export Data to CSV**

Export data from a table to a CSV file.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Exporter import Exporter

    async def main():
        manager = Manager(db_name='example.db')
        exporter = Exporter(manager)
        await exporter.export_data_csv(table_name='users', csv_file_path='data', csv_file_name='users_data')

    asyncio.run(main())