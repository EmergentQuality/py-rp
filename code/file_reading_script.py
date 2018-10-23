# file = open("message.txt", mode='w')

with open("message.txt", mode='w') as file:
    file.write("this message has been written.\n")
    text = "string in a variable, also written.\n"
    file.write(text)
# file.close()
# file_read = open("message.txt", mode='r')
# print(file_read.read())
# file_read.close()
# new_file = open("NewFile.txt", mode='w')
# new_file.write("New content")
# new_file.close()
