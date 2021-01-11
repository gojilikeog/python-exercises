import random

# Functions
"""
def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    return "Hello %s, From My Function! Here's what you said!: %s" % (username, greeting)


my_function()
username = "My momma"
greeting = "Shut up."
my_function_with_args(username, greeting)


# Exercise

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()
"""

"""
# Classes and Objects

class MyClass:
    variable = "blah"

    def function(self):
        print("This message is inside the class.")


my_object_x = MyClass()
my_object_x.function()
my_object_x.variable = "Yo momma"
print(my_object_x.variable)


# Exercise

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car2 = Vehicle()

car1.value = 60_000.00
car1.name = "Fer"
car1.color = "red"
car2.value = 10_000.00
car2.name = "Jump"
car2.color = "blue"

# test code
print(car1.description())
print(car2.description())
"""
# Dictionaries
"""
phonebook = {
    "John": 23456,
    "Jill": 34567,
    "Jack": 45678
}

print(phonebook["Jack"])

# Iterating over dictionaries

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value

del phonebook["Jack"]
print(phonebook)

# OR treat it like a stack - use to catch the data
phonebook.pop("Jill")
print(phonebook)

# Exercise

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

phonebook["Jack"] = 938273443
del phonebook["Jill"]
print(phonebook)


if "Jack" in phonebook and "Jill" not in phonebook:
    print("Jack is listed in the phonebook")
    print("Jill is not listed in the phonebook.")
    print("Nice work!")
"""
# Exercise 1
"""
name = input("What is your name?: ")
age = int(input("What is your age?: "))
print("Dear %s: You will turn 100 in the year %s." % (name, ((100 - age) + 2021)))
"""

# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd
# print out an appropriate message to the user.
"""
number = int(input("Pick a number: "))
numberTwo = int(input("Pick another number: "))

if number % numberTwo == 0:
    print("Wow, you're pretty good at this huh?")
else:
    print("Yeah, didn't think you'd get this one too.")
"""

# Exercise 3
"""
a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}

print([aa for aa in a if aa < 5])
"""

# Exercise 4
"""
number = int(input("Pick a number: "))
number_list = []

for x in range(1, number + 1):
    if number % x == 0:
        number_list.append(x)

print(number_list)
"""

# Exercise 5
# Add numbers the appear in both lists into a new list (no duplicates!)
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []

for num in a:
    if num in b:
        if num not in new_list:
            new_list.append(num)

print(new_list)
"""

# Exercise 6
# Ask the user for a string, print out whether the string is a palindrome or not.
"""
string = input("Give me a sentence: ")

if string[::-1] == string:
    print("This string is a palindrome: %s" % string)
else:
    print("This string is not a palindrome: %s" % string)
"""

# Exercise 7
# You're given a list saved in a variable. Write one line of python that takes
# this list a and makes a new list that one has the even elements on this list.
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# LEARN TO UNDERSTAND THIS
b = [number for number in a if number % 2 == 0]
print(b)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [number for number in c if number % 2 == 0]
print(d)
"""
# Exercise 8 - Rock Paper Scissors
# Make a 2P RPS Game
"""
play_again = True

while play_again:
    player1 = input("What's your move Player 1?: ").lower()
    player2 = input("How about you Player 2?: ").lower()

    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!")
        elif player2 == "paper":
            print("Player 2 wins!")
        else:  # player2.lower() == "rock"
            print("It's a tie.")
    elif player1 == "scissors":
        if player2 == "rock":
            print("Player 2 wins!")
        elif player2 == "paper":
            print("Player 1 wins!")
        else:  # player2.lower() == "scissors"
            print("It's a tie.")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
        else:  # player2.lower() == "paper"
            print("It's a tie.")
    else:
        print("Learn how to spell.")

    if input("Play again?: ").lower() != "yes":
        play_again = False
        print("Thanks for playing!")
"""
# Exercise 9
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.
"""
guess = random.randint(1, 9)
user_guess = int(input("Guess a number between 1 and 9: "))

if user_guess == guess:
    print("You're right!")
elif guess > user_guess > 0:
    print("Too low: %s" % guess)
elif guess < user_guess < 10:
    print("Too high: %s" % guess)
else:
    print("Seems like something went wrong. You entered: %s" % user_guess)
"""
# Exercise 10
# List Overlap Comprehensions
# Write a program that returns a list that contains only the
# elements that are common between the lists (without dups).
# Make suer your program works on two lists of different sizes.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [number for number in set(a) if number in b]

print(c)
"""
# set(a) is used to remove the duplicate in a that is causing the
# value to appear, a duplicate that is not accounted for in the writing.

# Exercise 11
# Check Primality Functions
# Ask the user for a number and determine whether the number is
# prime or not. (Prime number is a number with no divisors)
"""
user_number = int(input("Enter a number, I'll determine if it's prime: "))


def is_prime(number):
    if number == 1:
        print("%s is not a prime number." % number)
        return False

    for x in range(2, number):
        if number % x == 0:
            print("%s is not a prime number." % number)
            return False

    print("%s is a prime number." % number)
    return True


is_prime(user_number)
"""
# Exericse 12
# Write a program that takes a list of numbers and makes a
# new list of only the first and last elements of the given
# list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]


def first_last(number_list):
    return [number_list[0], number_list[-1]]


b = first_last(a)
print(b)
