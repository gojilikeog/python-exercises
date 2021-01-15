
# Exercise 1

name = input("What is your name?: ")
age = int(input("What is your age?: "))
print("Dear %s: You will turn 100 in the year %s." % (name, ((100 - age) + 2021)))


# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd
# print out an appropriate message to the user.

number = int(input("Pick a number: "))
numberTwo = int(input("Pick another number: "))

if number % numberTwo == 0:
    print("Wow, you're pretty good at this huh?")
else:
    print("Yeah, didn't think you'd get this one too.")


# Exercise 3

a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}

print([aa for aa in a if aa < 5])


# Exercise 4

number = int(input("Pick a number: "))
number_list = []

for x in range(1, number + 1):
    if number % x == 0:
        number_list.append(x)

print(number_list)


# Exercise 5
# Add numbers the appear in both lists into a new list (no duplicates!)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []

for num in a:
    if num in b:
        if num not in new_list:
            new_list.append(num)

print(new_list)


# Exercise 6
# Ask the user for a string, print out whether the string is a palindrome or not.

string = input("Give me a sentence: ")

if string[::-1] == string:
    print("This string is a palindrome: %s" % string)
else:
    print("This string is not a palindrome: %s" % string)


# Exercise 7
# You're given a list saved in a variable. Write one line of python that takes
# this list a and makes a new list that one has the even elements on this list.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# LEARN TO UNDERSTAND THIS
b = [number for number in a if number % 2 == 0]
print(b)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [number for number in c if number % 2 == 0]
print(d)

# Exercise 8 - Rock Paper Scissors
# Make a 2P Rock-Paper-Scissors Game

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

# Exercise 9
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.

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

# Exercise 10
# List Overlap Comprehensions
# Write a program that returns a list that contains only the
# elements that are common between the lists (without dups).
# Make suer your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [number for number in set(a) if number in b]

print(c)

# set(a) is used to remove the duplicate in a that is causing the
# value to appear, a duplicate that is not accounted for in the writing.

# Exercise 11
# Check Primality Functions
# Ask the user for a number and determine whether the number is
# prime or not. (Prime number is a number with no divisors)

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

# Exericse 12
# Write a program that takes a list of numbers and makes a
# new list of only the first and last elements of the given
# list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]


def first_last(number_list):
    return [number_list[0], number_list[-1]]


b = first_last(a)
print(b)

Exercise 13 - Fibonacci

Write a program that asks how many Fibonnaci numbers to generate
and then generates them. Use functions. Make sure to ask the user
to enter the number of number in the sequence to generate.

def fibonacci_generator(length):

    if length <= 0:
        return []
    elif length == 1:
        new_list = [0, 1]
        return new_list
    elif length == 2:
        new_list = [0, 1, 1]
        return new_list
    else:
        new_list = [0, 1, 1]

    for x in range(2, length):
        new_list.append((new_list[x] + new_list[x - 1]))

    return new_list


numbers = int(input("How many numbers for fibonacci?: "))
numbers_result = fibonacci_generator(numbers)
print(numbers_result)

Exercise 14 - List Remove Duplicates

Write a program(function!) that takes a list and returns a
new list that contains all the elements of the first list
minus all the duplicates

Extras:
- Write two different functions to do this - one using a loop
  and constructing a list, and another using sets.
- Go back and do Exercise 5 using sets, and write a solution
  for that in a different function

    
def remove_duplicates(list_before):
    return set(list_before)


before_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
after_list = remove_duplicates(before_list)
print(after_list)

Exercise 15
Write a program(using functions!) that asks the user for a long
string containing multiple words. Print back to the user the same
string, except with the words in backward order.

# Solution 1
def reverse_string(words):
    reverse = words.split()
    reverse = reverse[::-1]
    return " ".join(reverse)


test_string = "Cracking The Code Interview"
test_string = reverse_string(test_string)
print(test_string)

# Soltuon 2

test_string = "Cracking The Code Interview"
test_string = " ".join(test_string.split()[::-1])
print(test_string)
