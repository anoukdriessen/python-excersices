import csv

import pandas as pd

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
# createAndWrite()

# read from CSV file
def readFromCSV():
    with open("source/files/ted_talks_data.csv") as file:
        data = csv.reader(file)
        count = 0

        titles = []
        authors = []
        dates = []
        views = []
        likes = []
        links = []

        for row in data:
            if count == 0:
                count += 1
                continue
            # print(row)
            titles.append(row[0])
            authors.append(row[1])
            dates.append(row[2])
            views.append(row[3])
            likes.append(row[4])
            links.append(row[5])
            count += 1
            if count == 101:
                break

        most_views = max(views)
        ted_talk_with_most_views = views.index(most_views)
        print(f"Most viewed {titles[ted_talk_with_most_views]} by {authors[ted_talk_with_most_views]} with {most_views} views")

        most_likes = max(likes)
        ted_talk_with_most_likes = likes.index(most_likes)
        print(f"Most liked {titles[ted_talk_with_most_likes]} by {authors[ted_talk_with_most_likes]} with {most_likes} likes")

# readFromCSV()      

# csv handling with pandas
def withPandas():
    data = pd.read_csv("source/files/ted_talks_data.csv")
    # title,author,date,views,likes,link
    # print(data)
    # print(data["title"])
    # print(data["author"])
    # print(data["date"])
    # print(data["views"])
    # print(data["likes"])
    # print(data["link"])

    # dict = data.to_dict()
    # print(dict)

withPandas()