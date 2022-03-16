PATH = "source\practice_projects\mailMerge\input\starting_letter.txt"
NAMES = "source\practice_projects\mailMerge\input\\names.txt"
READY = "source\practice_projects\mailMerge\\ready\\letter_"

PLACEHOLDER = "[name]"
with open(NAMES) as names_file:
    names = names_file.readlines()
    # print(names)

with open(PATH) as letter:
    content = letter.read()
    print(content)
    for name in names:
        stripped = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped)
        # print(new_letter)
        fileName = (READY + stripped + ".txt")
        # print(fileName)
        with open(fileName, mode="w") as file:
            # save the letters in the folder /ready
            file.write(new_letter)

