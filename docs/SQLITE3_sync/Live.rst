Live
=====

This module handles live events and real-time changes in synchronous contexts.

.. automodule:: DbUnify.SQLite3.sync.Live
   :members:
   :undoc-members:
   :show-inheritance:

LiveManager
------------

**LiveManager** is the primary class for monitoring database changes and events in real-time.

.. autoclass:: DbUnify.SQLite3.sync.Live.LiveManager
   :members:
   :undoc-members:
   :show-inheritance:

**register_callback | On changes**

Register a callback for a specific event | On changes.

.. code-block:: python

    from DbUnify.SQLite3.sync.Live import LiveManager, Attribute

    def on_changes(manager: LiveManager, change: Attribute):
        print("Change detected:")
        print(f"Timestamp: {change.timestamp}")
        print(f"Database: {change.db_name}")
        print(f"Table: {change.table_name}")
        print(f"Operation: {change.operation}")
        print(f"Command: {change.command}")
        print(f"Details: {change.details}")

    databaseLive = LiveManager("test.db", 0.1)
    databaseLive.register_callback('change_detected', on_changes)

**register_callback | On Schema Changes**

Register a callback for a specific event | On Schema Changes.

.. code-block:: python

    from DbUnify.SQLite3.sync.Live import LiveManager, Attribute

    def on_schema_changes(manager: LiveManager, change: Attribute):
        print("Schema change detected:")
        print(f"Timestamp: {change.timestamp}")
        print(f"Database: {change.db_name}")
        print(f"Table: {change.table_name}")
        print(f"Operation: {change.operation}")
        print(f"Command: {change.command}")
        print(f"Details: {change.details}")


    databaseLive = LiveManager("test.db", 0.1)
    databaseLive.register_callback('schema_change_detected', on_schema_changes)


**restart**

Restart monitoring the database.

.. code-block:: python

    databaseLive.restart()

**run**

Continuously monitor the database for changes.

.. code-block:: python

    databaseLive.run()

**start**

Start monitoring the database.

.. code-block:: python

    databaseLive.start()

**stop**

Stop monitoring the database.

.. code-block:: python

    databaseLive.stop()


LiveException
--------------

Base exception class for LiveManager and its derived exceptions.

.. autoclass:: DbUnify.SQLite3.sync.Live.LiveException
   :members:
   :undoc-members:

**DatabaseAccessException**

Exception raised for errors accessing the database.

**EventHandlingException**

Exception raised for errors in event handling.

**LogWriteException**

Exception raised for errors writing to the log file.

**SchemaChangeException**

Exception raised for errors detecting schema changes.

Attribute
---------

**Attribute** represents details of a change event.

.. autoclass:: DbUnify.SQLite3.sync.Live.obj.Attribute
   :members:
   :undoc-members:

**to_dict**

Convert the Attribute object to a dictionary.

.. code-block:: python

    from DbUnify.SQLite3.sync.Live import Attribute

    attr = Attribute(timestamp='2024-08-07T12:34:56', db_name='test.db', table_name='users', operation='INSERT', command='INSERT INTO users (name, email) VALUES (?, ?)', details={'name': 'John Doe', 'email': 'john.doe@example.com'})
    attr_dict = attr.to_dict()
    print(attr_dict)

Examples
--------

**Live Event Listener Example**

This example demonstrates how to set up a `LiveManager` instance to listen for database changes and schema changes.

.. code-block:: python

    from DbUnify.SQLite3.sync.Live import LiveManager, Attribute

    def on_changes(manager: LiveManager, change: Attribute):
        print("Change detected:")
        print(f"Timestamp: {change.timestamp}")
        print(f"Database: {change.db_name}")
        print(f"Table: {change.table_name}")
        print(f"Operation: {change.operation}")
        print(f"Command: {change.command}")
        print(f"Details: {change.details}")

    def on_schema_changes(manager: LiveManager, change: Attribute):
        print("Schema change detected:")
        print(f"Timestamp: {change.timestamp}")
        print(f"Database: {change.db_name}")
        print(f"Table: {change.table_name}")
        print(f"Operation: {change.operation}")
        print(f"Command: {change.command}")
        print(f"Details: {change.details}")

    if __name__ == "__main__":
        databaseLive = LiveManager("test.db", 0.1)
        databaseLive.register_callback('change_detected', on_changes)
        databaseLive.register_callback('schema_change_detected', on_schema_changes)
        databaseLive.run()
