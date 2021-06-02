# python program that takes text file as a input and returns the number of words of a given text file
def counting(file_path):
    data1 = open(file_path, "r")
    data2 = data1.read()
    data2.replace(",", " ")
    data2.replace(".", " ")
    data2.replace("?", " ")
    data2.replace("!", " ")
    data2.replace("\n", " ")
    return len(data2.split(" "))


print("numbers of words in a file:", counting("C:\\Users\\navee\\Desktop\\intern\\social\\Lib\\sample3.txt"))

