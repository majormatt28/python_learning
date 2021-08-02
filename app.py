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

command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand.")