import asyncio
from DbUnify.MySQL.aio import Manager, Exporter


async def main():
    manager = Manager(
        host='localhost',
        user='root',
        password='',
        database='example_db',
        port=3306
    )
    
    exporter = Exporter(manager)
    
    try:
        await manager.connect()
        
        # Export Database Charts
        await exporter.export_chart_database(
            output_directory='charts',
            chart_type='bar',
            x_label='X Axis',
            y_label='Y Axis'
        )
        
        # Export Table Chart
        await exporter.export_chart_table(
            table_name='user',
            x_column=0,
            y_column=1,
            x_label='User ID',
            y_label='Age',
            title='User Age Distribution',
            save_path='charts/user_age_distribution.png',
            chart_type='bar'
        )
        
        # Export to CSV
        await exporter.export_data_csv(
            table_name='user',
            csv_file_path='charts',
            csv_file_name='users_data'
        )
    
    finally:
        await manager.close()

if __name__ == "__main__":
    asyncio.run(main())
