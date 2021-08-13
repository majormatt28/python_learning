# birth_year = input('Birth year: ')
# age = 2021 - int(birth_year)
# print(age)


# user_weight = input("Weight(lbs): ")
# kilo = int(user_weight) * 0.45
# print(kilo)


# name = 'Jennifer'
# print(name[1:-1])

# first = 'Matt'
# last = 'Newton'
# msg = f'{first} [{last}] is a coder'
# print(msg)


# course = 'Python for Beginners'
# course.len()
# print(course.upper())


# x = 10 + 3 * 2
# print(x)


# import math
# print(math.ceil(2.9))

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")  
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# price = 1000000
# good_credit = True

# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")


# has_high_income = True
# has_criminal_record = False
# has_good_credit = False

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")


# temperature = 40

# if temperature >= 40:
#     print("It's a hot ass day")
# else:
#     print("It's not so hot")


# name = "Matt"

# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good!")




# Approach 1 for weight converter

# weight = float(input("What is your weight? "))
# unit = input("Lbs or Kgs? ")
# pound = 2.20462
# converted_weight = float(weight * pound)
# formatted_float = "{:.2f}".format(converted_weight)

# print(weight)
# print(unit)

# if unit == "Kgs":
#     print(f"Your weight is {weight} {unit}")
# elif unit == "Lbs":
#     print(f"Your weight is {formatted_float} {unit}")
# else:
#     print("Not a valid input")



# Approach 2 for weight converter

# weight = int(input('Weight '))
# unit = input('(L)bs or (K)g: ')

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"Your are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"Your {converted} pounds")


# While loops

# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("done")

# Guessing game using while loops

# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit :
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You win!")
#         break
# else:
#     print("Sorry you failed") 

# Building a car game

# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I don't understand.")


# Learning for loop
# for item in range(10):
#     print (item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# prices = [100, 50, 60]
# difference = 0
# for price in prices:
#     difference -= price
# print(f"Differece: {difference}")

# Nested Loops

# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#         print(output)

# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#         print(output)

# Lists 
# names = ['Josh', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[2:])
# print(names)

# numbers = [10, 22, 3, 14, 6, 11]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# 2D Lists

# matrix =[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for item in row:
#         print(item)

# List methods

# numbers = [5, 2, 1, 7, 4]
# numbers.sort()
# print(numbers)

# numbers = [5, 7, 9, 5, 6, 3, 3]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# Tuples
# numbers = (1, 2, 3)
# numbers[0]
# print(numbers)
# *Tuples cannot be changed. They are immutable lists so whenever I would want a list to not change I would use tuple

# Unpacking
# coordinates = (1, 2, 3)
# x, y, z = coordinates

# Dictionaries
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }

# customer["name"] = "Jack Smith"
# print(customer["name"])

# phone = input("Phone: ")
# digit_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output = ""
# for ch in phone:
#     output += digit_mapping.get(ch, "!") + " "
# print(output)

# Emoji Converter
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😃",
#     ":(": "😟",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# Functions

# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')


# print("Start")
# greet_user()
# print("Finish")

# Parameters

# def greet_user(first_name, last_name):
#     print(f'Hi there {first_name} {last_name}!')
#     print('Welcome aboard')


# print("Start")
# greet_user("John", "Smith")
# print("Finish")

# Keyword Arguments
    
