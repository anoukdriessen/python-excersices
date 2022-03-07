print("Welcome to your virtual garden")
width = int(input("What is the length of your garden [x] = "))
height = int(input("What is the height of your garden [y] = "))
print(f"You chose {width} x and {height} y")

garden = []

i = 0
while i <= (width - 1):
    print(f"Row {i}")
    j = 0
    garden.append([])
    while j <= (height - 1):
        print(f"[{i}][{j}]")
        garden[i].append("EMPTY")
        # garden[i][j] = 
        j += 1

    i += 1    

for row in garden:
    print(row)

position = input("Which field do you want to change?")

# print the number the user choice
position_x = int(position[0])
position_y = int(position[1])
print(f"You chose: Row [{position_x}] Column [{position_y}]")

# change the chosen value
garden[position_x-1][position_y-1] = 'X'
