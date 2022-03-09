# for loop
# for ITEM in LIST_OF_ITEMS:
#    do something

def countToTenWithList():
    count = [0,1,2,3,4,5,6,7,8,9]
    for number in count:
        print(number+1)

# write a program that calculates the avarage student height from a list of heights
# don't use len() or sum() recreate the use of those functions
def getAvarage(): 
    student_heights = [190, 124, 165, 173, 189, 169, 146]
    sum = 0
    count = 0

    # calculate the total / number of students
    for height in student_heights:
        sum += height
        count += 1

    print(f"total={sum} from {count} students")
    # calcultate the avarage total / amount
    avarage = round(sum / count)
    print(f"avarage={avarage}")

# you are going to write a program that calculates the highest score from a list of scores
# you are not allowed to use the max or min functions
def getHighScore():
    student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
    highScore = 0

    for score in student_scores:
        if score > highScore:
            highScore = score

    # show the result
    print(f"The highest score in the class is: {highScore}")

def countToTenWithRange():
    for number in range(1, 11):
        print(number)

# you are going to write a program that calculates the sum of all the even numbers from 1 to 100
def calculateTotalEvenNumbers():
    total = 0
    for number in range(1, 101):
        #print(number) #print all the numbers from 1 to 100
        if number % 2 == 0:
            # number is even
            # print(number) # print all the EVEN numbers
            total += number

    print(f"total={total}")  

# you are going to write a program that automatically prints the solution to the FizzBuzz game
def playFizzBuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            # divisible by 3 AND 5
            print("FizzBuzz")
        elif number % 3 == 0:
            # divisible by 3
            print("Fizz")
        elif number % 5 == 0:
            # divisible by 5
            print("Buzz")  
        else:
            print(number)    

# countToTenWithList()
# getAvarage()
# getHighScore()
# countToTenWithRange()
# calculateTotalEvenNumbers()
# playFizzBuzz()

# while CONDITION:
#   do something

done = False
count = 1

while not done:
    print(count)
    count += 1
    if count > 10:
        done = True