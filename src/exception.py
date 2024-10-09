import sys 
import logging
from src.logger import logging

def error_message_details(error, error_details):
    '''
    Extracts detailed information from the error and traceback.
    '''
    _, _, exc_tb = error_details.exc_info()  # Get traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file where the error occurred
    line_number = exc_tb.tb_lineno  # Get the line number where the error occurred
    error_message = "An error occurred in python script [{0}] at line number [{1}] with error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    '''
    Custom Exception class to format the error details.
    '''
    def __init__(self, error_message, error_details: sys) -> None: # type: ignore
        super().__init__(error_message)  # Corrected super() usage
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self) -> str:
        return self.error_message


