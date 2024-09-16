import asyncio
from DbUnify.SQLite3.aio.Manager import Manager
from DbUnify.SQLite3.aio.Exporter import Exporter

manager = Manager(db_name='example.db')
exporter = Exporter(manager)

# async def main():
#     await manager.connect()  # Ensure connection is established
#     await exporter.export_chart_database(
#         output_directory='charts',
#         chart_type='bar',
#         x_label='X Axis',
#         y_label='Y Axis'
#     )
#     await manager.close()  # Close the connection when done

# async def main():
#     await manager.connect()  # Ensure connection is established
#     await exporter.export_chart_table(
#         table_name='user',
#         x_column=0,
#         y_column=1,
#         x_label='User ID',
#         y_label='Age',
#         title='User Age Distribution',
#         save_path='charts/user_age_distribution.png',
#         chart_type='bar'
#     )
#     await manager.close()  # Close the connection when done

# async def main():
#     await manager.connect()  # Ensure connection is established
#     await exporter.export_data_csv(table_name='user', csv_file_path='charts', csv_file_name='users_data')
#     await manager.close()  # Close the connection when done

asyncio.run(main())
