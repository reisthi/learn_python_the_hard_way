f = input("type the name of the file: ")

# def print_all(txt):
#     print(txt.read())


# def print_line(index, txt):
#     print (size, txt.readline())


# def rewind(txt):
#     txt.seek(0)

# def len_of_file(bar):
#     print(len(bar))

# txt = open(f)
# size = len(f)
# len_of_file(txt)
# print_all(txt)
# print_line(size, txt)
# rewind(txt)

def file_status(bar):
    txt = open(bar)
    txt.seek(0)
    # print("Length: ", len(txt))
    print("content: " , txt.read())
    # print("Length: ", len(txt))
    print("Lines?", txt.readline())


file_status(f)