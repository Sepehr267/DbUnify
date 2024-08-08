from ..Raw.Raw import Raw
from typing import List, Union
import os, csv, matplotlib.pyplot as plt

class Exporter:
    """
    # Exporter Class:

    #### The Exporter class provides methods to export data from a database to various formats such as charts (images) and CSV files.

    ### Attributes:
        - manager (Manager): The Manager instance managing the database connection.
        - raw (Raw): An instance of the Raw class for executing raw SQL queries.

    ### Methods:
        - __init__(self, manager): Initializes the Exporter instance with a Manager instance.
        - export_chart_database(self, output_directory, chart_type='bar', x_label='X Label', y_label='Y Label'): 
            Creates charts for all tables in the database and saves them as images.
        - export_chart_table(self, table_name, x_column, y_column, x_label='X Label', y_label='Y Label', title='Chart Title', save_path='chart.png', chart_type='bar'):
            Creates a chart from data in a specific table and saves it as an image.
        - export_data_csv(self, table_name, csv_file_path, csv_file_name='output'):
            Exports data from a table to a CSV file.

    ### Raises:
        - RuntimeError: If there is an error during chart creation or saving, or during CSV data export.

    ### Note:
        - This class is designed for asynchronous usage and requires the use of the 'async' and 'await' keywords for method calls.
        - The 'Manager' and 'Raw' classes are used internally for database management and executing raw SQL queries respectively.
    """

    def __init__(self, manager):
        """
        Initialize the Exporter instance.

        Args:
            manager (Manager): The Manager instance managing the database connection.
        """
        self.manager = manager
        self.raw = Raw(manager)
    
    async def export_chart_database(self, output_directory: str, chart_type: str = 'bar', x_label: str = 'X Label', y_label: str = 'Y Label') -> None:
        """
        Create charts for all tables in the database and save them as images.

        Args:
            output_directory (str): The directory where chart images will be saved.
            chart_type (str): The type of chart to create ('bar', 'line', 'scatter', etc.).
            x_label (str): Label for the x-axis.
            y_label (str): Label for the y-axis.

        Raises:
            RuntimeError: If there is an error creating charts or saving them as images.
        """
        try:
            os.makedirs(output_directory, exist_ok=True)
            tables: List[str] = await self.raw.list_tables()

            for table_name in tables:
                data: List[tuple] = await self.manager.select(table_name)
                x_values: List[str] = [str(row[0]) for row in data] 
                y_values: List[Union[int, float]] = [row[1] for row in data] 
                plt.figure(figsize=(8, 6))
                if chart_type == 'bar':
                    plt.bar(x_values, y_values)
                elif chart_type == 'line':
                    plt.plot(x_values, y_values, marker='o', linestyle='-')
                elif chart_type == 'scatter':
                    plt.scatter(x_values, y_values)
                elif chart_type == 'histogram':
                    plt.hist(y_values, bins='auto', edgecolor='k')
                else:
                    raise RuntimeError(f"Error, Type chart not found!")
                
                plt.xlabel(x_label)
                plt.ylabel(y_label)
                plt.title(f'{chart_type.capitalize()} Chart for Table: {table_name}')

                chart_filename: str = os.path.join(output_directory, f'{table_name}_{chart_type}_chart.png')
                plt.savefig(chart_filename)

                plt.close()

        except Exception as e:
            raise RuntimeError(f"Error creating charts: {str(e)}")

    async def export_chart_table(self, table_name: str, x_column: int, y_column: int, x_label: str = 'X Label', y_label: str = 'Y Label', title: str = 'Chart Title', save_path: str = 'chart.png', chart_type: str = 'bar') -> None:
        """
        Create a chart from data in the database and save it as an image.

        Args:
            table_name (str): Name of the database table to retrieve data from.
            x_column (int): Index of the x-axis column in the retrieved data.
            y_column (int): Index of the y-axis column in the retrieved data.
            x_label (str): Label for the x-axis.
            y_label (str): Label for the y-axis.
            title (str): Title of the chart.
            save_path (str): Path to save the chart image.
            chart_type (str): The type of chart to create ('bar', 'line', 'scatter', etc.).

        Raises:
            RuntimeError: If there is an error creating the chart or saving it as an image.
        """
        try:
            data: List[tuple] = await self.manager.select(table_name)
            x_values: List[Union[int, float]] = [row[x_column] for row in data]
            y_values: List[Union[int, float]] = [row[y_column] for row in data]
            plt.figure(figsize=(8, 6))
            if chart_type == 'bar':
                plt.bar(x_values, y_values)
            elif chart_type == 'line':
                plt.plot(x_values, y_values, marker='o', linestyle='-')
            elif chart_type == 'scatter':
                plt.scatter(x_values, y_values)
            elif chart_type == 'histogram':
                plt.hist(y_values, bins='auto', edgecolor='k')
            else:
                raise RuntimeError(f"Error, Type chart not found!")
                
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.savefig(save_path)
            plt.close()

        except Exception as e:
            raise RuntimeError(f"Error creating chart: {str(e)}")
   
    async def export_data_csv(self, table_name: str, csv_file_path: str, csv_file_name: str = 'output') -> None:
        """
        Export data from a table to a CSV file.

        Args:
            table_name (str): The name of the table to export data from.
            csv_file_path (str): The path to save the exported CSV file.

        Raises:
            Exception: If there is an error during data export.
        """
        try:
            rows: List[tuple] = await self.manager.select(table_name)

            with open(f'{csv_file_path}/{csv_file_name}.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = [description[0] for description in self.manager.cursor.description]
                csv_writer.writerow(header)
                csv_writer.writerows(rows)
        except Exception as e:
            raise Exception(f"Error exporting data: {str(e)}")
