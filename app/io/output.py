

def console_output(text):
    """
    Function that outputs given text into console.

    Args:
        text(str): Text that will be written into console.

    Returns:
    """
    print(text)


def file_writing(file,text):
    """
    Function that writes given text into chosen file using python built-in methods.

    Args:
        file(str): Path to file where we need to write.
        text(str): Text that function will write into file.

    Returns:
        str. Returns filepath
    """
    try:
        with open(file, 'w') as f:
            f.write(text)
        return file
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return ""
    pass
