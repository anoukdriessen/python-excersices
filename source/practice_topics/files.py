# OPEN file my_text_file.txt in the source directory
# myFile = open("source/my_text_file.txt")
# CLOSE the file, no need to close the file with -> with open()
# myFile.close()

# read only
def readFile():
    with open("source/files/my_text_file.txt", mode="r") as myFile:
        # READ the file content
        myFileContent = myFile.read()
        print(myFileContent)

# mode write
def overwrite():
    with open("source/files/my_text_file.txt", mode="w") as myFile:
        # WRITE to the file -> overwrites existing content in myFile
        myFile.write("My name is Anouk")

# mode append
def append():
    with open("source/files/my_text_file.txt", mode="a") as myFile:
        # WRITE to the file but don't overwrite existing content
        myFile.write("\nHello World")

# create new file if not exists
# delete the file new_text_file.txt and it will be created when running this method
def createAndWrite():
    with open("source/files/new_text_file.txt", mode="w") as myFile:
        myFile.write("Welcome to my new text file")        

# readFile()
# overwrite()
# append()
createAndWrite()