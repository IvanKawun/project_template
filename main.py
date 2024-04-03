from app.io.input import *
file = "testFile.txt"

##Дуже мало часу до дедлайну, не встигаю створити файл формату сsv
def main():
    console_text = console_input()

    python_file_text = python_read(file)

    #pandas_file_text = pandas_read("")

    print("Text from console:", console_text)
    print("Text read from file using python built-in methods:", python_file_text)
    #print("Text read from file using pandas built-in methods", pandas_file_text)


    with open("output.txt", "w") as f:
        f.write("Text from console:\n")
        f.write(console_text)
        f.write("\n\nText read from file using python built-in methods:\n")
        f.write(python_file_text)
        #f.write("\n\nText read from file using pandas built-in methods:\n")
        #f.write(pandas_file_text)

if __name__ == '__main__':
    main()


