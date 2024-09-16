import random, json

class DatasetGenerator:
    def __init__(self):
        """
        The constructor initializes the class with predefined lists of tables, columns, and values.
        
        Attributes:
            self.tables (list): A list of common database table names.
            self.columns (list): A list of common column names used in tables.
            self.values (list): A list of sample values that can be inserted into the queries.
            self.patterns (list): A list of SQL query patterns that can be used to generate both suspicious and non-suspicious SQL queries.
        """
        self.tables = [
            'users', 'products', 'orders', 'employees', 'departments', 'categories', 'suppliers', 'customers',
            'payments', 'shipments', 'reviews', 'inventory', 'transactions', 'contracts', 'invoices', 'tasks',
            'projects', 'employees_history', 'salaries', 'leaves', 'assets', 'locations', 'warehouses', 'sales',
            'purchases', 'returns', 'promotions', 'discounts', 'subscriptions', 'services', 'appointments',
            'reservations', 'orders_history', 'feedback', 'tickets', 'calendars', 'events', 'notifications',
            'messages', 'alerts', 'preferences', 'settings', 'logs', 'transactions_history', 'audit_trails',
            'user_roles', 'permissions', 'activity_logs', 'user_sessions', 'user_actions', 'user_profiles',
            'account_settings', 'payment_methods', 'refunds', 'order_items', 'shopping_cart', 'wishlists',
            'subscriptions_history', 'service_requests', 'support_tickets', 'customer_feedback', 'product_reviews',
            'product_categories', 'order_status', 'shipping_methods', 'delivery_addresses', 'inventory_logs',
            'purchase_orders', 'service_orders', 'vendor_contacts', 'employee_roles', 'performance_reviews',
            'training_sessions', 'job_positions', 'department_changes', 'attendance_records', 'holiday_schedules',
            'shift_patterns', 'work_orders', 'maintenance_requests', 'incident_reports', 'complaints', 'returns_policy'
        ]

        self.columns = [
            'id', 'username', 'password', 'email', 'first_name', 'last_name', 'phone', 'address', 'city', 'state',
            'country', 'zip_code', 'created_at', 'updated_at', 'deleted_at', 'price', 'quantity', 'order_date',
            'department', 'salary', 'start_date', 'end_date', 'status', 'product_name', 'category_id', 'supplier_id',
            'customer_id', 'payment_method', 'shipment_date', 'review_rating', 'feedback_text', 'inventory_level',
            'transaction_amount', 'contract_date', 'invoice_number', 'task_description', 'project_name', 'employee_id',
            'leave_type', 'asset_id', 'location', 'warehouse_id', 'sale_date', 'purchase_amount', 'return_reason',
            'promotion_code', 'discount_amount', 'subscription_start_date', 'service_type', 'appointment_time',
            'reservation_date', 'ticket_number', 'calendar_event', 'notification_type', 'message_content', 'alert_level',
            'preference_key', 'preference_value', 'log_entry', 'audit_event', 'role_name', 'permission_type',
            'activity_description', 'session_start', 'session_end', 'action_type', 'profile_picture', 'account_status',
            'refund_amount', 'item_name', 'shopping_cart_id', 'wishlist_id', 'service_request_type', 'support_ticket_id',
            'feedback_date', 'product_review_id', 'product_category_id', 'order_status', 'shipping_cost', 'delivery_date',
            'inventory_count', 'purchase_order_number', 'vendor_name', 'performance_score', 'training_topic', 'job_title',
            'department_name', 'attendance_date', 'holiday_name', 'shift_start', 'shift_end', 'work_order_number',
            'maintenance_type', 'incident_description', 'complaint_type', 'return_policy'
        ]
    
        self.values = [
            'admin', 'password', 'item1', '100', '2023-01-01', 'Sales', 'john.doe@example.com', 'Jane Smith',
            '123 Main St', 'New York', 'NY', '10001', '2024-08-22', 'active', 'inactive', '12.99', '25', '2024-08-01',
            'Engineering', '50000', '2024-01-01', '2024-12-31', 'completed', 'pending', 'Samsung Galaxy', 'Electronics',
            'XYZ Corp', 'Alice Johnson', 'credit_card', '2024-08-10', '5 stars', 'Great product!', '50', '5000',
            'New Contract', 'INV-12345', 'Fix bug in login', 'Project Alpha', 'E123', 'vacation', 'Asset001', 'Downtown',
            'Warehouse A', '2024-08-20', '1500', 'Product return', 'SUMMER20', '10%', '2024-07-01', 'Service Request A',
            '2024-08-15', 'Ticket-98765', 'Meeting with client', 'Urgent', 'System alert', 'user_pref1', 'value1',
            'System log entry', 'Audit log entry', 'Admin', 'read', 'Login attempt', '2024-08-22 10:00:00', '2024-08-22 18:00:00',
            'Login', 'profile_pic.png', 'active', '25.00', 'Cart123', 'Wishlist456', 'Service Request B', 'TICKET-1234',
            '2024-08-21', 'Review-987', 'Category 1', 'shipped', '5.99', '2024-08-30', '123456', 'Maintenance A',
            'Report Bug', 'Customer Complaint', 'Return within 30 days'
        ]

        self.patterns = [
            "SELECT * FROM {table} WHERE {column} = '{value}' OR '1'='1';",
            "SELECT * FROM {table} WHERE {column} = '{value}' OR 'x'='x';",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND 1=1;",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND 1=2;",

            "SELECT * FROM {table} WHERE {column} = '{value}' UNION SELECT NULL, NULL, NULL;",
            "SELECT * FROM {table} WHERE {column} = '{value}' UNION ALL SELECT {column}, {column}, {column} FROM {table2};",
            "SELECT {column} FROM {table} WHERE {column} = '{value}' UNION SELECT {column} FROM {table2};",
            "SELECT * FROM {table} WHERE {column} = '{value}' UNION SELECT user(), database();",
            
            "SELECT * FROM {table} WHERE {column} = '{value}' AND 1=1;",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND 1=2;",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND {column} LIKE '%test%';",
            
            "SELECT * FROM {table} WHERE {column} = '{value}' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT user()), FLOOR(RAND() * 2)) x FROM information_schema.tables GROUP BY x) a);",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND 1=CONVERT(int, (SELECT @@version));",
            
            "SELECT * FROM {table} WHERE {column} = '{value}' AND IF(1=1, SLEEP(5), 0);",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND IF(1=2, SLEEP(5), 0);",
            
            "INSERT INTO {table} ({column}) VALUES ('{value}'); SELECT * FROM {table} WHERE {column} = '{value}';",
            "INSERT INTO {table} ({column}) VALUES ('{value}'); SELECT * FROM {table} WHERE {column} = (SELECT {column} FROM {table2} WHERE {column} = '{value}');",
            
            "SELECT * FROM {table} WHERE {column} = '{value}' -- Comment",
            "SELECT * FROM {table} WHERE {column} = '{value}' /* Comment */",
            
            "SELECT * FROM {table} WHERE {column} = '{value}' AND {column} IN (SELECT {column} FROM {table2});",
            "SELECT * FROM {table} WHERE {column} = '{value}' OR EXISTS (SELECT * FROM {table2} WHERE {column} = '{value}');",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND (SELECT COUNT(*) FROM {table2} WHERE {column} = '{value}') > 1;",
            "SELECT * FROM information_schema.tables WHERE table_schema = '{value}';",
            "SELECT * FROM {table} WHERE {column} LIKE '%{value}%';",
            "EXEC xp_cmdshell 'dir';",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND 1=1 UNION ALL SELECT * FROM {table};",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND {column} LIKE '{value}%';",
            "SELECT * FROM {table} WHERE {column} = '{value}' OR '1'='1';",
            "SELECT * FROM {table} WHERE {column} = '{value}' OR {column} IS NULL;",
            "SELECT * FROM {table} WHERE {column} = '{value}' UNION SELECT @@version;",
            "SELECT * FROM {table} WHERE {column} = '{value}' AND (SELECT * FROM {table} WHERE {column} = '{value}') IS NOT NULL;",
            "UPDATE {table} SET {column} = '{value}' WHERE {column} = '{value}' OR 1=1;"
        ]
        
        self.patterns = [
            "SELECT {column} FROM {table} WHERE {column} = '{value}';",
            "INSERT INTO {table} ({column1}, {column2}) VALUES ('{value1}', '{value2}');",
            "UPDATE {table} SET {column} = '{value}' WHERE {column} = '{value}';",
            "DELETE FROM {table} WHERE {column} = '{value}';",
            "SELECT * FROM {table} WHERE {column} BETWEEN '{value1}' AND '{value2}';",
            "SELECT DISTINCT {column} FROM {table};",
            "SELECT COUNT(*) FROM {table} WHERE {column} = '{value}';",
            "SELECT AVG({column}) FROM {table} WHERE {column} > '{value}';",
            "SELECT MIN({column}) FROM {table};",
            "SELECT MAX({column}) FROM {table};",
            "SELECT {column}, COUNT(*) FROM {table} GROUP BY {column};",
            "SELECT * FROM {table} WHERE {column} IN ('{value1}', '{value2}');",
            "SELECT * FROM {table} WHERE {column} NOT IN ('{value1}', '{value2}');",
            "SELECT * FROM {table} WHERE {column} IS NOT NULL;",
            "SELECT * FROM {table} WHERE {column} IS NULL;",
            "SELECT {column} FROM {table} WHERE {column} LIKE '{value}%';"
        ]

    def add_custom_patterns(self, suspicious_patterns: list = None, non_suspicious_patterns: list = None):
        """
        Adds custom SQL query patterns to the existing list of patterns.

        Parameters:
            suspicious_patterns (list): List of custom suspicious SQL patterns to add.
            non_suspicious_patterns (list): List of custom non-suspicious SQL patterns to add.
        """
        if suspicious_patterns:
            self.suspicious_patterns.extend(suspicious_patterns)
        if non_suspicious_patterns:
            self.non_suspicious_patterns.extend(non_suspicious_patterns)

    def add_custom_tables_columns_values(self, tables: list = None, columns: list = None, values: list = None):
        """
        Adds custom tables, columns, and values to the existing lists.

        Parameters:
            tables (list): List of custom table names to add.
            columns (list): List of custom column names to add.
            values (list): List of custom values to add.
        """
        if tables:
            self.tables.extend(tables)
        if columns:
            self.columns.extend(columns)
        if values:
            self.values.extend(values)
                
    def generate_suspicious_query(self) -> str:
        """
        Generates a single suspicious SQL query using predefined patterns, tables, columns, and values.

        Returns:
            str: A suspicious SQL query string.
        """
        pattern = random.choice(self.patterns)
        table = random.choice(self.tables)
        column = random.choice(self.columns)
        value = random.choice(self.values)

        if '{table2}' in pattern:
            table2 = random.choice(self.tables)
            if '{column2}' in pattern:
                column2 = random.choice(self.columns)
                value1 = random.choice(self.values)
                value2 = random.choice(self.values)
                return pattern.format(table=table, column=column, value=value, table2=table2, column2=column2, value1=value1, value2=value2)
            else:
                return pattern.format(table=table, column=column, value=value, table2=table2)
        else:
            if '{column1}' in pattern and '{column2}' in pattern:
                column1 = random.choice(self.columns)
                column2 = random.choice(self.columns)
                value1 = random.choice(self.values)
                value2 = random.choice(self.values)
                return pattern.format(table=table, column=column, value=value, column1=column1, column2=column2, value1=value1, value2=value2)
            elif '{value1}' in pattern and '{value2}' in pattern:
                value1 = random.choice(self.values)
                value2 = random.choice(self.values)
                return pattern.format(table=table, column=column, value=value, value1=value1, value2=value2)
            else:
                return pattern.format(table=table, column=column, value=value)

    def generate_non_suspicious_query(self) -> str:
        """
        Generates a single non-suspicious SQL query using predefined patterns, tables, columns, and values.

        Returns:
            str: A non-suspicious SQL query string.
        """ 
        pattern = random.choice(self.patterns)
        table = random.choice(self.tables)
        column = random.choice(self.columns)
        value = random.choice(self.values)
        
        if '{column1}' in pattern and '{column2}' in pattern:
            column1 = random.choice(self.columns)
            column2 = random.choice(self.columns)
            value1 = random.choice(self.values)
            value2 = random.choice(self.values)
            return pattern.format(table=table, column=column, value=value, column1=column1, column2=column2, value1=value1, value2=value2)
        elif '{value1}' in pattern and '{value2}' in pattern:
            value1 = random.choice(self.values)
            value2 = random.choice(self.values)
            return pattern.format(table=table, column=column, value=value, value1=value1, value2=value2)
        else:
            return pattern.format(table=table, column=column, value=value)

    def generate_dataset(self, num_suspicious: int = 8000, num_non_suspicious: int = 8000) -> list:
        """
        Generates a dataset consisting of both suspicious and non-suspicious SQL queries.

        Parameters:
            num_suspicious (int): Number of suspicious queries to generate.
            num_non_suspicious (int): Number of non-suspicious queries to generate.

        Returns:
            list: A list of dictionaries, each containing a SQL query and its label (1 for suspicious, 0 for non-suspicious).
        """
        data = []
        
        for _ in range(num_suspicious):
            query = self.generate_suspicious_query()
            data.append({'query': query, 'label': 1})
        
        for _ in range(num_non_suspicious):
            query = self.generate_non_suspicious_query()
            data.append({'query': query, 'label': 0}) 
        
        return data

    def save_to_json(self, data: list, filename: str):
        """
        Saves the generated dataset to a JSON file.

        Parameters:
            data (list): The dataset to save.
            filename (str): The name of the file to save the dataset to.
        """        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data generation complete. Dataset saved to '{filename}'.")
