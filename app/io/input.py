import pandas as pd

def console_input():
    """
    Function that allows to input a text in console.

    Returns:
        str. Returns the line that user wrote in console.
    """
    text = input("Input the text in console: ")
    return text

def python_read(file):
    """
    Function that reads text from file using python built-in methods.

    Args:
        file(str): Path of a file that function reads from.

    Returns:
       str. Returns text from file.
    """
    try:
        with open(file, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file}' wasn't found.")
        return ""

def pandas_read(file):
    """
    Function that reads text from file using pandas methods.

    Args:
        file(str): Path of a file that function reads from.

    Returns:
        str. Returns text from file.
    """
    try:
        df = pd.read_csv(file)
        text = df.to_string(index=False)
        return text
    except FileNotFoundError:
        print(f"File '{file}' wasn't found.")
    return ""