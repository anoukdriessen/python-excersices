# Lists for storing related data together
# Lists have a index to an item in the list, the first item always has index 0

def lists_of_fruits():
    fruits = ["Apples", "Bananas", "Pears"]
    print(fruits[0])        # first item
    print(fruits[-1])       # last item

    # items in list
    print(len(fruits))

    # change an item in the list
    print("before", fruits)
    fruits[1] = "Oranges"
    print("after", fruits)

    # add item to end of the list
    print("items in list", len(fruits))
    fruits.append("Bananas")
    print("items in list (after append)", len(fruits))

    # add a bunch of items to the end of the list
    fruits.extend(["Lemons", "Mangos", "Carrots"])
    print(fruits)

    # remove the last item from the list
    fruits.pop()
    print(fruits)

    # nested lists
    # dirty dozen can be improved by storing the same type of data in its own list
    #dirty_dozen = ["Strawberries", "Spinash", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

    dirty_dozen = [fruits, vegetables]
    print(dirty_dozen)
    print(dirty_dozen[0])
    print(dirty_dozen[1])
# lists_of_fruits()

list_with_key_value = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}   

def another_list():
    # show all
    # print(list_with_key_value)

    # get one item by key
    print(list_with_key_value["Bug"])

    # add new item to list
    list_with_key_value["MyKey"] = "My fantastic value"
    print(list_with_key_value["MyKey"])

    # loop trough dictionary
    for key in list_with_key_value:
        print(key)
        print(list_with_key_value[key])

another_list()