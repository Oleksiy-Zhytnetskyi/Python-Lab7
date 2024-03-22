import pandas as pd


def from_console():
    """
    Gets a string of user input received from the console

    Returns:
        str: The string of user input received from the console.
    """
    return input()


def from_file(file_path):
    """
    Gets the string of text read from a file at the given file path

    Args:
        file_path (str): The path to the file from which text should be read.

    Returns:
        str: The string of text read from a file at file_path
    """
    with open(file_path) as file:
        return file.read()


def from_file_pd(file_path):
    """
    Gets the string of text read from a file at the given file path using the pandas library

    Args:
        file_path (str): The path to the file from which text should be read.

    Returns:
        str: The string of text read from a file at file_path
    """
    return pd.read_csv(file_path, sep=' ', header=None).to_string(index=False, header=False)
