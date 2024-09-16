class ExporterException(Exception):
    """
    Base class for exceptions raised by the Exporter class.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class ChartCreationException(ExporterException):
    """
    Raised when there is an error creating a chart.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = f"Chart Creation Error: {message}"

class CSVExportException(ExporterException):
    """
    Raised when there is an error exporting data to a CSV file.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = f"CSV Export Error: {message}"

class InvalidChartTypeException(ExporterException):
    """
    Raised when an invalid chart type is provided.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = f"Invalid Chart Type: {message}"
