from DbUnify.SQLite3.sync.Exporter import Exporter
from DbUnify.SQLite3.sync.Manager import Manager

# Initialize Manager and Exporter
manager = Manager(db_name='example.db')
exporter = Exporter(manager=manager)

# Export charts for all tables
# exporter.export_chart_database(output_directory='charts/', chart_type='bar', x_label='X Axis', y_label='Y Axis')

# Export chart from a specific table
# exporter.export_chart_table(
#     table_name='user',
#     x_column=0,
#     y_column=1,
#     x_label='Month',
#     y_label='Revenue',
#     title='Monthly Sales Revenue',
#     save_path='sales_chart.png',
#     chart_type='line'
# )

# Export table data to a CSV file
# exporter.export_data_csv(table_name='user', csv_file_path='charts', csv_file_name='user.csv')
