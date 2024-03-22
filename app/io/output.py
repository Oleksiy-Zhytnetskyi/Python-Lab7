import pandas as pd


def to_console(text):
    """
    Prints a given string to the console

    Args:
        text (str): The text to output to the console.
    """
    print(text)


def to_file(file_path, text):
    """
    Appends a given string to a file at the given file path

    Args:
        file_path (str): The path to the file to which text should be appended.
        text (str): The text to append to the file.
    """
    with open(file_path, 'a') as file:
        file.writelines(text)


def to_file_pd(file_path, text):
    """
    Appends a given string to a file at the given file path using the pandas library

    Args:
        file_path (str): The path to the file to which text should be appended.
        text (str): The text to append into the file.
    """
    pd.DataFrame({'text': [text]}).to_csv(file_path, mode='a', header=False, index=False)
