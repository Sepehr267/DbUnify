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
    databaseLive = LiveManager("example.db", 0.1)
    databaseLive.register_callback('change_detected', on_changes)
    databaseLive.register_callback('schema_change_detected', on_schema_changes)
    databaseLive.run()