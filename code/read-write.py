# open a the source file in read modeself.
source_file = open("NewFile.txt", mode='r')
# read file contents into a variable.
source_content = source_file.read()
# close the source fileself.
source_file.close()
# open a new file in write mode.
target_file = open("ClonedFile.txt", mode='w')
# write the contents of the variable to the new file.
target_file.write(source_content)
# close the target file.
target_file.close()
