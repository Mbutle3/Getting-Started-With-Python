# Booleans
print('-----------------------------------')
print("Topic: Booleans\n")
print(type(True))
print(type(False))
# Integers
print('-----------------------------------')
print("Topic: Integers\n")
print(type(3))
print(type(0))
print(type(-100))
# Floats
print('-----------------------------------')
print("Topic: Floats\n")
print(type(0.0))
print(type(4.))
print(type(3.0))
print(type(-3.3))
print(type(5e10))  # 5 times 10 to the 10
print(type(5e-10))  # 5 times 10 to the negative 10
# Strings
print('-----------------------------------')
print("Topic: Strings\n")
print(type("I am a string."))
print(type("elephant"))
print(type('cat'))
print(type(""))
print(type(''))
print(type(' '))
print(type(" "))
# 2 + 5 vs '2 + 5'
print(type("2+5"))
print(type(2 + 5))
print(2 + 5)
print('2+5')
# print('-----------------------------------')
# loop = True
# name = input("What Is Your Name?\n")
# print("")
# guess = int(input('Guess A Number From 1 to 10\n'))
# while loop is True:
#     if guess == 2:
#         print("You Got It!")
#         loop = False
#         break
#     guess = int(input('Guess A Number From 1 to 10'))
print('-----------------------------------')
print("Topic: Functions\n")


def sumofsquares(x, y):
    sq1 = x * x
    sq2 = y * y
    return sq1 + sq2


def addfive(x):
    print(5 + x)


def square(x):
    return x * x


def greeting():
    print("Hello World!")


def greet(name):
    print("Hello " + name + "!")


def is_it_raining():
    raining = input("Is it raining today? \n")
    return raining


four_squared = square(4)
print(four_squared)
four_squared_squared = square(four_squared)
print(four_squared_squared)
print(square(5))

res = sumofsquares(3, 3)  # 3^2 + 3^2 = 18
print(res)

addfive(10)
addfive(62.5)

greeting()
greet("Noland")
#
# monday_rain = is_it_raining()  # No
# print(monday_rain)  # Should return no
#
# tuesday_rain = is_it_raining()  # Yes
# print(tuesday_rain)  # Should return yes
print('-----------------------------------')
print("Topic: Importing Modules\n")

import calendar

calendar = calendar.month(2022, 12)
print(calendar)

import math

result = math.sqrt(49)
print(result)
print(int(result))

import random

number = random.randint(1, 100)

print(number)

movies = ["Transformers I", "SpiderMan: No Way Home", "X-Men: First Class", " Batman Begins",
          "Joker", " Black Adam", "Black Panther"]  # A "sequence" of movies

watch = random.choice(movies)  # Want to choose a random movie from list

print(watch)

deck = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
print(deck)

random.shuffle(deck)  # Randomly re-arranges the order of items in the sequence

print(deck)
print('-----------------------------------')
print("Topic: Lists - mutable\n")

dbz_heroes = ["Goku", "Vegeta", "Gohan", "Trunks", "Piccolo", "Krillin"]
print(type(dbz_heroes))
print(dbz_heroes)
print(dbz_heroes[0])
print(dbz_heroes[: 1])

listB = [True, "star", 50, 333.3]
print(type(listB))
print(listB)
print(listB[2])
print('-----------------------------------')
print("Topic: Tuples - immutable\n")

madara_info = ("Madara", "Uchiha", "Land of Fire", "December 24th")
hashirama_info = ("Hashirama", "Senju", "Land of Fire", "October 23th")

print(type(madara_info))
print(madara_info)
print(f'Country of Origin: {madara_info[2]}')
print(f'Shinobi: {madara_info[:2]}')
print(type(hashirama_info))
print(hashirama_info)
print(f'Country of Origin: {hashirama_info[2]}')
print(f'Shinobi: {hashirama_info[:2]}')

print('-----------------------------------')
print("Topic: Taking In User Input\n")


# raining = input("Is it raining? (yes/no)\n")
#
# if raining == 'yes':
#     print("You need an umbrella!")
# else:
#     print("You don't need an umbrella!")


# print("choose an integer between -10 and 10")
# n = input("enter it here: ")
# n = int(n)
# if n < 5:
#     print("the integer you chose is less than 5.")
# elif n > 5:
#     print("the integer you chose is greater than 5.")
#


def minimum(x, y):
    if x < y:
        return x
    else:
        return y


res = minimum(2, 5)
print(res)
res = minimum(-2, -5)
print(res)
res = minimum(7, 7)
print(res)
res = minimum(4, 4.0)
print(res)
res = minimum(3, 3.1)
print(res)
# res = minimum(3, '3') #Causes Error
# print(res)
res = minimum(4, int('5'))
print(res)

# raining = input("is it raining? (yes/no)\n")
# umbrella = input("do you have an umbrella? (yes/no)\n")
#
# if raining == "yes" and umbrella == 'yes':
#     print("Don't forget your umbrella when you go out!")
# elif raining == "yes" and umbrella == "no":
#     print("Wear a waterproof jacket when you go out!")
# else:
#     print("Okay have a great day!")

x = input("Enter a number here: ")
x = float(x)
if x < 2:
    print("The number is less than 2.")
elif x < 6:
    print("the number is less than 6.")
elif x < 8:
    print("the number is less than 8.")
elif x < 10:
    print("the number is less than 10.")

x = 1
print(float(x))
y = 1.5
print(int(y))
y = 1.4
print(int(y))
y = 1.9
print(int(y))


# input is -4 -> abs is 4
# input is 0 -> abs is 0
# input is 78.3 -> abs is 78.3

def abs_val(num):
    if num < 0:
        return -num
    elif num == 0:
        return 0
    else:
        return num


result = abs_val(-4)
print(result)
result = abs_val(0)
print(result)
result = abs_val(78.3)
print(result)
print('-----------------------------------')
print("Topic: Loops\n")
print("Hangman Game")
word = "consistency"
vowels = ["e", "i", "o"]
vowel_count = 0
for c in word:
    if c in vowels:
        vowel_count += 1
print(vowel_count)

for i in range(4):
    print(i)

for i in range(1, 8, 2):
    print(i)

konoah_hokages = ['hashirama', 'tobirama', 'hiruzen ', 'minato', 'tsunade', 'kakashi', 'naruto']

print('Oldest to Newest Hokages')
i = 1
for hokages in konoah_hokages:
    print(hokages, i)
    i += 1
print('Newest to Oldest Hokages')
i = len(konoah_hokages) - 1
while i >= 0:
    print(konoah_hokages[i], i + 1)
    i -= 1

konoah_hokages_len = len(konoah_hokages)
print(f'Konoah Has Had {konoah_hokages_len} Hokages!')

print('-----------------------------------')
print("Topic: Recursion\n")


def isPalidrome(s):
    if len(s) < 1:
        return True
    else:
        return s[0] == s[-1] and isPalidrome(s[1:-1])


def sumDigits(n):
    if n < 10:
        return n
    else:
        remaining_digits = n // 10
        last_digit = n % 10
        return sumDigits(remaining_digits) + last_digit


def fibFunction(n):
    if n < 1:
        return n
    if n == 1:
        return n
    else:
        return n + fibFunction(n - 1)


print("Sum Of Digits")
print(sumDigits(123))
print(sumDigits(456))
print(sumDigits(789))
print(sumDigits(1012))

print("\nFib Sequence")
print(fibFunction(5))
print(fibFunction(3))
print(fibFunction(1))
print(fibFunction(0))

print("\nIs Palidrome")
print(isPalidrome("bob"))
print(isPalidrome("12221"))
print(isPalidrome("1212112"))
print(isPalidrome("adam"))
print('-----------------------------------')
print("Topic: Classes\n")


class Dog:
    # initialization function;
    def __init__(self, name, age):
        # self is a variable that's bound to the 'Dog' object (used when creating a init method)
        self.name = name
        self.age = age

    def bark(self):  # A L L METHODS receive self!!!
        print("Woof!")


Fido = Dog("Fido", 2)
print(Fido.name)
print(Fido.age)
Fido.bark()
Fido.age += 1
print(Fido.age)

