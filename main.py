# age = 20
#
# print("your age is " + str(age) + " Years Old")
# print("your age is",age,"years old")
# Fstrings
# print(f"your age is {age} years old")
# import random
# # 1-INTEGER
# age = 15
# players = 2
# quantity = 5
#
# print(f"You Are Age Is {age} years old")
# print(f"there are {players} Players online")
# print(f"You Would like to  buy {quantity} items")
# from Tools.scripts.mailerdaemon import x

# 2-FLOAT
# gpa = 3.2
# distance = 2.5
# price = 10.99
#
# print(f"Your gpa is {gpa}")
# print(f"you ran {distance}Km")
# print(f"the price is ${price}")

# 3-STRING
# name = "Yousef"
# order = "Meat Halal"
# email = "raqia707@gmail.com"
# print(f"Hello Sir {name}")
# print(f"Your Order {order}")
# print(f"Your Email is : {email}")

# BOOLEAN
# online = True
# for_sale = False
# running = False
# print(f"Are You online?:{online}")
# print(f"Is the item for sale {for_sale}")
# print(f"Game running {running}")
#
# if running:
#     print("the game is running")
# else:
#     print("the game is over")

# VARIABLE
# x = 1
# y = 2
# z = 3
# OR
# x, y, z = 1, 2, 3
# OR
# x = y = z = 2
# print(x)
# print(y)
# print(z)

####################################################
# Type casting => Explicit
# name = "yousef"
# age = 15
# gpa = 1.9
# student = True
# ##########################
# print(type(name))#String
# print(type(age))#integer
# print(type(gpa))#float
# print(type(student))#boolan
# ##########################
#
# ##########################
# # convert integer to float
# age = float(age)
# print(age)
# print(type(age))
# ##########################
#
# ##########################
# #convert integer to boolan
# age = bool(age)
# print(age)#Here he returned the value correctly even if the number is less than zero but if the number is zero he returns the value false
# print(type(age))
# ##########################
#
# #convert string to boolan
# name = bool(name)
# print(name)#it returned true but the name value = 0 return false
# print(type(name))


# Type casting => Implicit
# x = 2
# y = 2.0
#
# x = x / y
# print(x)

####################################################

####################################################
# USER INPUT
# name = str(input("Enter Your Name: "))# I convert name to Str() and add "bro"
# name = name + " bro"
# age = int(input("Enter Your Age: "))
# age = age + 1
# print(f"Hello Bro {name}")
# print(f"you are Age {age} Years Old")
####################################
# Frist Exercise
# adjactive1 = input("Enter an adjactive: ")
# none = input("Enter a none: ")
# adjactive2 = input("Enter an adjactive: ")
# verb = input("Enter a verb: ")
# adjactive3 = input("Enter an adjactive: ")
#
# print(f"Today I Went To a {adjactive1}")
# print(f"In an Exhibit , I saw {none}")
# print(f"{none} Was {adjactive2} and {verb}ing")
# print(f"I was {adjactive3}")
###################################
###################################
# Second exercise => Area Calc
# length = float(input("Enter The Length of a Rectangle: "))
# width = float(input("Enter The Width of a Rectangle: "))
# height = float(input("Enter The Height Of Rectangle: "))
# area = length * width * height
#
# print(f"The Area is: {area}cm^3")
###################################
###################################
# Shopping Cart
# item = input("What Item Would You Like To Buy: ")
# price = float(input("What is the Price: "))
# quantity = float(input("How Many Would You Like: "))
# total = price * quantity
#
# print(f"You Have Bought {quantity} x {item}/s")
# print(f"Your Total is: ${round(total, 2)}")
###################################
###################################
# Cars exercize
# car = input("Enter Your Car Type: ")
# user_name = input("Enter FullName: ")
# user_id = int(input("Enter Your ID Card Number Or ID Car Number: "))
# issues = input("What's Problem In Your Car: ")
# changing = input("Do You want Changing any Think: ")
# changing_price = float(input("The Price Of Changing: "))
# check = input("Do You Want mack Check on Car Sir: ")
# check_price = float(input("The price of check of car: "))
# total = changing_price + check_price
#
# print(f"Type Your car is {car}")
# print(f"Your Name Is {user_name}")
# print(f"Your ID Card or ID Car is: {user_id}")
# print(f"Your problem on Car: {issues}")
# print(f"We did Changed {changing} on car")
# print(f"Price The {changing} is ${changing_price}")
#
# print(f"Price The {check} check is ${check_price}")
# print(f"total: ${total}")
# ###################################
####################################################

####################################################
# String methods

# name = input("Enter Your Full Name: ")
# phone_number =input("Enter The Phone Number: ")

# name = len(name)# => Counting letters in a word
# name = name.find(" ")# => Find the selected item and calculate the letters that precede it
# name = name.rfind("a")# => Find the last letter and calclate the letters that precede it
# name = name.capitalize()# => Convert beginning letters of a word to capital letters
# name = name.upper()# => Convert all letters of word to caiptal
# name = name.lower()# => Convert all capital letters to small
# name = name.isdigit()# => Return Bollan Value Give true in case the input = numbers
# name = name.isalpha()# => Return Boolan value and Give True in case the input = alphabets
# phone_number = phone_number.count("-")# => Calculates the number of repetitions of the value you give it
# phone_number = phone_number.replace("-", "res")#Change the value I set for him

# print(phone_number)

# username = input("Enter a Username: ")
#
# if len(username) > 12:
#     print("Your Username Can't be more than 12 charactars")
# elif not username.find(" ") == -1:
#     print("Your Username Can't Contain Speaces")
# elif not username.isalpha():
#     print("Your User Name Can't contain Number")
# else:
#     print(f"Welcome {username}")
####################################################

####################################################
# Math
# friends = 10

# friends = friends + 1  #Same Result
# friends += 1 #Same Result

# friends = friends - 2  #Same Result
# friends -= 2  #Same Result

# friends = friends * 3 #Same Result
# friends *= 3 #Same Result

# friends = friends / 2 #Same Result
# friends /= 2 #Same Result

# friends = friends ** 2 #Same Result => 5*5
# friends **= 2

# friends = friends % 3#Divide the number 10 into 3 groups and the remaining 1
# friends %= 3#Same Result
#
# print(friends)

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)#Convert a number from negative to positive
# result = pow(4, 3)# => 4 * 4 * 4
# result = max(x , y, z)#Maximum Value Between Values
# result = min(x,y,z)#Minimum Value Between Values
# print(result)


# import math
#
# x = 9.9

# print(math.pi)
# print(math.e)
# result = math.sqrt(9)# => 3 // 8 => 2 // Square Root
# result = math.ceil(x)# 9.9 => 10 // Rounds a number up to the nearest integer
# result = math.floor(x)# 9.9 => 9 // Rounds a number down to the nearest integer

# print(result)


# Calculation of the radius of a circle
# import math
# radius = float(input("Enter The Radius Of a Circle: "))
#
# circumference = 2 * math.pi * radius
# print(f"The circumference is {round(circumference ,2)}cm")


# 2 Exersize calculation
# import math
# radius = float(input("Enter The Radius of Circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of Circle is: {round(area, 2)}cm^2")


# 3 Exersize
# import math
# a = float(input("Enter Side A: "))
# b = float(input("Enter Side B: "))
#
# c = math.sqrt(pow(a, 2) + pow(b, 2))
#
# print(f"Side C: {c}")
####################################################


####################################################
# If statement => (if, elif, else)

# Exercize 1
# age = int(input("Enter Your Age: "))
#
# if age >= 100:
#     print("You are too old to Sing Up")
#
# elif age <= 0:
#     print("You Haven't Been born Yet")
#
# elif age >= 18:
#     print("you are now singed in")
#
# else:
#     print("You Must Be 18+ To Sing Up")


# Answar by Y / N  Exercize 2
# response = input("Would You Food? (Y / N): ")
# if response == "Y":
#     print("Have Some Food!")
# else:
#     print("No Food For You!")

# Exercize 3
# name = input("Enter Your Name: ")
#
# if name == "":
#     print("You Did Not Type in Your Name!")
# else:
#     print(f"Hello {name}")


# Exercize 4
# online = False
#
# if online:
#     print("the user is online")
# else:
#     print("the user is offline")
####################################################

####################################################
# Python calculator program

# num1 = float(input("Enter the 1ST Number: "))
# operator = input("Enter An Operator (+ - * /): ")
# num2 = float(input("Enter the 2ED Number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valied operator")
####################################################

####################################################
# Python weight conversion exercise

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")
#
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your Weight is {round(weight, 2)} {unit}")
#
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"Your Weight is {round(weight, 2)} {unit}")
#
# else:
#     print(f"{unit} Was Not Valid")
####################################################

####################################################
# Python temperature conversion program 🌡️

# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# # Arithmetic base => (°C * 9/5) + 32 = °F
# if unit == "C":
#     temp = round((temp * 9) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}°F")
# # Arithmetic base => (°F - 32) * 5/9 = °C
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1)
#     print(f"The temperature in Celsius is: {temp}°C")
# else:
#     print(f"{unit} is an invalid unit of measurement")
###################################################

###################################################
# Logical operators =>
# and => Checks Two Or More Conditions if True

# temp = float(input("Enter a Temperature: "))
#
# if temp > 15 and temp < 30:
#     print(f"The Temperature is Good ☀️")
# elif temp >= 0 and temp < 14:
#     print("The Weather little Cold Today")
# else:
#     print(f"The Temperature is {int(temp)}°  Really it's so bad")
#####################
# or => Checks if at leats one Condition is true , One must be true and the other false

# temp = float(input("Enter a Temperature: "))

# if temp <= 0 or temp >= 30:
#     print("The temperature is so bad")
# else:
#     print("The Temperature is good")
#
# not => True if Condition is false, and vice versa

# sunny = True

# if not sunny:
#         print("it's cloudy Outside")
#     else:
#         print("it's sunny outside")

###################################################

###################################################
# String indexing
# credit_number = "1234-5678-9012-3456"

# print(credit_number[10])# Selcect
# print(credit_number[:4])# from 0 to 4
# print({credit_number[5:9]})# from 0 to 9
# print(credit_number[5:])# from 5 to end
# print(credit_number[-1])# Start From End
# print(credit_number[::2])# Leave 2 Between all Groubs

# Exercize 1 =>
# credit_number = "1234-5678-9012-3456"
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX{last_digits}")

# Exercize => 2  Convert last Number to Frist
# credit_number = "1234-5678-9012-3456"
# credit_number = credit_number[::-1]
# print(credit_number)# Result => 6543-2109-8765-4321
###################################################

###################################################
# email slicer exercise
# email = input("Enter Your Email: ")
# username = email[:email.index("@")]
# domain = email[email.index("@") + 1:]
# print(f"Your Username is {username} and domain is {domain}")
###################################################
###################################################
# Format specifiers
# .(number)f = round to that many decimal places (fixed point)
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:.1f}")
# print(f"price 2 is ${price2:.1f}")
# print(f"price 3 is ${price3:.1f}")
# :(number) = allocate that many spaces
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:10}")
# print(f"price 2 is ${price2:10}")
# print(f"price 3 is ${price3:10}")
# :03 allocate and zero pad that many spaces
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:010}")
# print(f"price 2 is ${price2:010}")
# print(f"price 3 is ${price3:010}")
# :<= left justify
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:<10}")
# print(f"price 2 is ${price2:<10}")
# print(f"price 3 is ${price3:<10}")
# :>= right justify
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:>10}")
# print(f"price 2 is ${price2:>10}")
# print(f"price 3 is ${price3:>10}")
# :^ = Center align
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:^10}")
# print(f"price 2 is ${price2:^10}")
# print(f"price 3 is ${price3:^10}")
# :+ = use a plus sign to indicate positive value
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1:+}")
# print(f"price 2 is ${price2:+}")
# print(f"price 3 is ${price3:+}")
# : = insert a space before positive numbers
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"price 1 is ${price1: }")
# print(f"price 2 is ${price2: }")
# print(f"price 3 is ${price3: }")

# price1 = 3000.14159
# price2 = -9870.65
# price3 = 1200.34
# print(f"price 1 is ${price1:,}")
# print(f"price 2 is ${price2:,}")
# print(f"price 3 is ${price3:,}")

# price1 = 3000.14159
# price2 = -9870.65
# price3 = 1200.34
# print(f"price 1 is ${price1:+,.2f}")
# print(f"price 2 is ${price2:+,.2f}")
# print(f"price 3 is ${price3:+,.2f}")
###################################################

###################################################
# While loops
# name = input("Enter Your Name: ")
#
# while name == "":
#     print("You Did Not Enter Your Name")
#     name = input("Enter Your Name: ")
# print(f"Hello {name}")

# age = int(input("Enter Your Age: "))
#
# while age < 0:
#     print("Age Can't be Negative")
#     age = int(input("Enter Your Age: "))
# print(f"Your Are {age} Years old")

# food = input("Enter A Food You Like (q to quit): ")
#
# while not food == "q":
#     print(f"You Like {food}")
#     food = input("Enter A Food You Like (q to quit): ")
# print("Bye ")

# num = int(input("Enter A # Between 1 - 10: "))
#
# while num < 1 or num > 10:
#     print(f"{num} is Not Valid")
#     num = int(input("Enter A # Between 1 - 10: "))
# print(f"Your Number Is {num}")

# i = 1
# while i < 6:
#     print(i)
#     i += 1
###################################################
###################################################
# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter The Principle Amount: "))
#     if principle < 0:
#         print("Interest Rate Can't Be less Than Zero")
#     else:
#       break
# while True:
#     rate = int(input("Enter The interest rate: "))
#     if rate < 0:
#         print("Rate Can't Be less Than Zero")
#     else:
#       break
# while True:
#     time = int(input("Enter The time in Years: "))
#     if time < 0:
#         print("Time Can't Be less Than Zero")
#     else:
#       break
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance After {time}Year/s : {total:.2f} $")
###################################################

###################################################
# For Loop
# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1, 11)):
#     print(x)

# print("HAPPY NEW YEAR!")

# for x in range(1, 11, 2):#Add Bettwen Every Number 2
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)
###################################################

###################################################
# Nested loops
# for x in range(1, 10):
#     print(x, end="")# Inline Result

# for x in range(1, 10):
#     print(x, end="-")# Add (-) Bettwen Every Number

# for x in range(3):# Repeat for y 3 times
#     for y in range(1, 10):
#         print(y,end="")
#     print()# not inline

# Exercize
# rows = int(input("Enter The Number Of Rows: "))
# columns = int(input("Enter The Number For Columns: "))
# symbol = input("Enter A Symbol To Use: ")
#
# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()
###################################################

###################################################
# Countdown timer
# import time
# your_time = int(input("Enter The Time In Seconds: "))
# for x in range(your_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time'S UP!")
###################################################

###################################################
# Start With Elzero Web School

# types of data------------------------------------
# float = 10.00
# integer = 10
# boolan = 2 == 2
# String = "I'm Yousef"
# list = [1, 2, 3, 4, 5]
# tuple = (1, 2, 3, 4, 5)
# dictionary = {"Yousef": 16, "Taha": 43, "Rana": 34}
# print(type(float))
# -------------------------------------------------

# -------------------------------------------------
# variables Types and Rules
# A, B, C = 1, 2, 3
# print(A)
# print(B)
# print(C)
# -------------------------------------------------

# -------------------------------------------------
# Escaping
# back Line => \b
# print("Hello\bWorld") # Will be remove "o"
# # New Line => \
# print("Hello \
# I love \
# Python")# Will be "Hello I love Python"

# # Escaping Back Slash
# print("Hello Back Clash \"") # Add New " in After back Clash Even Scape

# # Line Feed => Make A New line
# print("hello World\nSecond Line")

# Back Slach T => Added Tab
# print("hello\tSpeace")

# Characters Hex Value
# print("\x4F\x73")# => Os
# -------------------------------------------------

# -------------------------------------------------
# String
# myStringOne = "This Is Single Quote"
# mystringTwo = "this is Double Quotes"
# mystringThree = 'this is Double Quote "Test"'
# mystringfour = "this is Double Quote 'Test'"
# mystringfive = """Frist
# Second 'test' "test" \
# Third"""
# mystringsix = '''Frist
# Second
# Third'''
# print(myStringOne)
# print(mystringTwo)
# print(mystringThree)
# print(mystringfour)
# print(mystringfive)
# print(mystringsix)
# -------------------------------------------------

# -------------------------------------------------
# Index
# myString = "I Love Python"
# print(myString[0])# => I
# print(myString[9])# => t
# print(myString[-1])# => n
# print(myString[-6])# => P

# Slicing [start:end] OR [start:End:steps]
# print(myString[8:11])# => yth
# print(myString[3:5])
# print(myString[:10])# => if Start Empty Will Start From 0 To Any Index
# print(myString[5:])# => if End Empty Will Start From 5 Index to last Letter in index
# print(myString[:])# if Start and End is Empty retern Full data
# print(myString[0::1])# => Full Data
# print(myString[::1])# => Full Data
# print(myString[::2])
# print(myString[::3])
# -------------------------------------------------
# -------------------------------------------------
# Methods For Strings
# a = "   I love Python   "
# print(len(a))# Retern Full Data
# print(a.strip())# Remove All Speaces
# print(a.rstrip())# Remove Right Speaces
# print(a.lstrip())# Remove left Speaces

# a = "#@##@##I love Python###@#@##"
# print(a.strip("#@"))
# print(a.lstrip("#@"))
# print(a.rstrip("#@"))

# title()
# b = "I Love 2d Graphics and 3g Technology and python"
# print(b.title())# Convert Frist Character Is Captial
# print(b.capitalize())# Convert Frist Number capital Without Letters After Numbers
# print(b.upper())# Convert All Data To Capital
# c, d, e = "1", "11", "111"
# print(c.zfill(2))# => 01
# print(d.zfill(3))# => 011
# print(e.zfill(4))# => 0111
# -------------------------------------------------

# -------------------------------------------------
# # Methodes For String Part 2
# split()
# a = "I Love Python And Java"
# print(a.split())
# b = "I-Love-Python-And-Java"
# print(b.split("-"))
# c = "I-Love-Python-And-Java"
# print(c.split("-", 2))# => ['I', 'Love', 'Python-And-Java']
# d = "I-Love-Python-And-Java"
# print(d.rsplit("-", 2))# Remove two last dashs

# center()
# a = "Yousef"
# print(a.center(10))# Add Speaces Counts the number of letters of the word and the rest makes it spaces
# print(a.center(10, "#"))# Hashes

# Count()
# b = "I Love Python And PHP Cuz PHP Is Very Easy"
# print(b.count("PHP"))# How Many Repeat
# print(b.count("PHP", 0, 25))# From, To

# swapcase()
# a = "I Love Python"
# b = "I lOVE pYTHON"
# print(a.swapcase())
# print(b.swapcase())
# startswith()
# a = "I Love My Self"
# print(a.startswith("I"))# True Cuz Variable(a) Contain i in Start
# print(a.startswith("y"))# False Cuz Varible(a) Not Contain y in Start
# print(a.startswith("S", 10, 14))

# endswith()
# a = "I Love Python"
# print(a.endswith("n"))# True Cuz Last letter of word is "n"
# print(a.endswith("e", 2, 6))
# -------------------------------------------------
# -------------------------------------------------
##################################################
# index()
# a = "I Love Python"
# print(a.index("y"))
# print(a.index("P", 0, 8))# => 7
# print(a.index("P", 0, 7))# => Erorr

# find() => If Result False = -1 Not Erorr
# a = "I Love Python"
# print(a.find("P"))
# print(a.find("P", 0, 10))# => 7
# print(a.find("P", 0, 5))# => -1 Cuz It's Erorr

# rjust(Width, Fullchar) ljust(Width, Fullchar)
# a = "Yousef"
# print(a.rjust(15))# If Word Less Than 15 Add Speaces Before Write
# print(a.rjust(15, "#"))# If Word Less Than 15 Add Dashes Before Write
#
# a = "Yousef"
# print(a.ljust(15))# If Word Less Than 15 Add Speaces After Write
# print(a.ljust(15, "#"))# If Word Less Than 15 Add Dashes After Write

# splitlines()
# e = """Frist Line
# Second Line
# Third Line"""
# print(e.splitlines())# => Convert To List

# expandtabs()
# e = "Hello\tI\tLove\tPython"
# print(e.expandtabs(15))# Control Number Of Speaces

# isalnum() is Max Between Alpha and Numbers
# a = "IlovePython"
# b = "IlovePython1234"
# print(a.isalnum())
# print(b.isalnum())

# join() => Convert List To String
# mylist = ["Yousef", "Hassan", "Khalid"]
# print("-".join(mylist))# => Yousef-Hassan-Khalid
# print(" ".join(mylist))# => Yousef Hassan Khalid

# -----------------------Strings Formatting

# -----%s = String
# -----%d = Number , integer
# -----%f = Number , Float

# name = "Yousef"
# age = 15
# rank = 97
# print("My Name is: %s" % name)
# print("My age is: %d" % age)
# print("My rank is: %f" % rank)
# print("My Name's %s and my age %d And My rank %f" % (name, age, rank))

# Exercize
# name = "Yousef"
# pro_languge = "Python"
# since = 2023

# print("Alright, Your Name's %s And You Useing %s for Coding And You Conding Since %s" % (name, pro_languge, since))

# control in float
# _te = 10
# print("My Float Is %.2f" % float_te)# From 10.000000 To 10.00

# Control in String
# mylongmsg = "Hello I'm Yousef TAha I'm Egyptin"
# print("My Long massage is %.10s" % mylongmsg)# 10 letters Only => Hello I'm

# format() => New Way

# name = "Yousef"
# age = 15
# rank = 97

# print("My Name Is: {:s} & My age Is {:d} & My Rank is {:d}".format(name, age, rank))

# Exercize
# fullName = input("Enter Your Full Name: ")
# age = input("What's Your Age: ")
# typeJop = input("Enter Type of Jop: ")
# price = input("how Match You Wanna Take Every Mounth?: $")

# print("""Your Name is: {}
#       Your Age is: {}
#       you Better Work: {} IN Company
#       You Wanna Take: {}""".format(fullName, age, typeJop, price))

# Format Money
# money = 500162350198

# print("My Money In Bank: {:d}".format(money))
# print("My Money In Bank: {:_d}".format(money))# => 500_162_350_198

# Rearrying Items
# a, b, c = "One", "Two", "Three"

# print("Hello {} {} {}".format(a, b, c))# => Hello One Two Three
# print("Hello {1} {0} {2}".format(a, b, c))# => Hello Two One Three

# a, b, c = 10, 20, 30

# print("Hello {} {} {}".format(a, b, c))
# print("Hello {2} {1} {0}".format(a, b, c))# => Hello 30 20 10
# print("Hello {2:.2f} {1:.2f} {0:.3f}".format(a, b, c))# => Hello 30.00 20.00 10.000

# Numbers -----------------------------------

# Complex

# complexNumber = 5+6j

# print(type(complexNumber))

# print(f"Real Part Is: {complexNumber.real}")
# print(f"Imaginary Part Is: {complexNumber.imag}")
# # Can't Convert Complex To Any Varialbes Type
# print(4+6j)
# print(int(4+6j))# => Error
# print(float(4+6j))# => Error

# Arithmetic Operators
# [+] =>  Addition
# [-] => Subtraction
# [*] => Multipication
# [/] => Divsion
# [%] => Modulus
# [**] => Exponent
# [//] => Floor Divsion

# # [+] =>  Addition
# print(5 + 7)

# # [-] => Subtraction
# print(5 - 7)

# # [*] => Multipication
# print(5 + 10 * 100)# Frist 10 * 100 last 5 +
# print((5 + 10) * 100)# Frist(5 + 10) Last * 100

# # [/] => Divsion
# print(int(100 / 20))# => 5

# # [%] => Modulus
# print(8 % 2)# => 0
# print(9 % 2)# => 1

# # [**] => Exponent
# print(2 ** 5)# => 2 * 2 * 2 * 2 * 2 = 32
# print(5 ** 4)# => 5 * 5 * 5 * 5 = 625

# # [//] => Floor Divsion
# print(100 // 20)# => 5
# print(119 // 20)# => 5
# print(120 // 20)# => 6
# print(140 // 20)# => 7
# print(141 // 20)# => 7

# Lists
# myList = ["One", "Two", "One", 1, 100.5, True]

# print(myList)
# print(myList[1])
# print(myList[-1])
# print(myList[3])
# print(myList[-3])
# # Make Slice
# print(myList[1:4])
# # Make Steps
# print(myList[::2])
# # Edit For Items
# myList[1] = 2# Convert "Two" to (2)
# myList[-2] = 99# Convert (100.5) to (99)
# myList[0] = 1# Convert "" to (2)

# myList[0:3] = ["A"]
# print(myList)# ['A', 1, 100.5, True]

# List Methods
# myfrinds = ["Yousef", "Eyad", "Saged"]
# myOldfrinds = ["Haytham", "Sameh", "Ali"]
# myfrinds.append("Ahmed")# Add "Ahmed" To List
# myfrinds.append(100)# Add Number 100 To List
# myfrinds.append(True)# Add Boolan True To List

# myfrinds.append(myOldfrinds)# add myfrinds List To myOldfrinds List
# print(myfrinds)
# print(myfrinds[1])# => Eyad
# print(myfrinds[4])# => 100
# print(myfrinds[6][2])# =>

# extend()
# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# c = ["One", "Two", "Three"]

# a.extend(b)
# a.extend(c)
# output => [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two', 'Three']
# print(a)

# remove()
# x = [1, 2, 3, 4, "Yousef", True, "Yousef", "Yousef"]
# x.remove("Yousef")
# print(x)# => Remove frist "Yousef" Jast

# sort()
# y = [5, 2, 4, 3, 1, -2, -1]# => [-2, -1, 1, 2, 3, 4, 5]
# alpha = ["B", "A", "D", "C"]
# y.sort(reverse=True)# Revers is convert to [5, 4, 3, 2, 1, -1, -2]
# alpha.sort()# => ['A', 'B', 'C', 'D']
# print(y)
# print(alpha)

# # reverse
# z = [10, 1, 80, 100, "Yousef", 100]

# z.reverse()# => [100, 'Yousef', 100, 80, 1, 10]
# print(z)

# clear() => Remove All Items In Array
# a = [1, 2, 3, 4, 5]
# a.clear()
# print(a)

# copy() => Copy List
# a = [1, 2, 3, 4, 5]
# c = a.copy()

# print(a)# Main List 1ST
# print(c)# Copied List 2th

# count() => Number of repetitions
# a = [1, 2, 3, 5, 2, 4, 5, 2, 3, 2]
# print(a.count(2))

# # index()
# i = ["Yousef", "Ramy", "khalid", "Ali", "Ramy", "Taha"]

# print(i.index("Ramy"))# Get Frist value

# insert()
# f = [1, 2, 3, 4, 5, "A", "B"]

# f.insert(1, "Another Value")# Add Any value Before Selected Index
# print(f)

# pop()
# a = [1, 2, 3, 4, 5, "A", "B"]

# print(a.pop(2))
# # -------------------------------------------


# Tuple if You Wanna Write Tuple Without () True
# mytupleOne = ("Yousef", "Osama")# => tuple
# mytupleTwo = "Yousef", "Osama"# => tuple

# print(mytupleOne)# => tuple
# print(mytupleTwo)# => tuple

# print(type(mytupleOne))# <class 'tuple'>
# print(type(mytupleTwo))# <class 'tuple'>


# Tuple indexing
# myTuple = 1, 2, 3, 4, 5

# print(myTuple[1])# => 2
# print(myTuple[-1])# => 5
# print(myTuple[-3])# => 3

# Tuple With One Element
# myTuple1 = ("Yousef",)# Add (,) So,that Know is Tuple
# myTuple2 = "Yousef",# Add (,) So,that Know is Tuple

# print(type(myTuple1))# => Tuple
# print(type(myTuple2))# => Tuple

# Tuple Concateation
# a = 1, 2, 3, 4
# b = 10, 20
# c = a + ("A", "B", 1, True) + b

# print(c)

# Tuple, List, String Repeat
# mystring = "Yousef"
# myList = [1, 2]
# myTuple = ("A", "B")

# print(mystring * 6)#Repeat 6 Times
# print(myList * 6)#Repeat 6 Times
# print(myTuple * 6)#Repeat 6 Times

# Tuple Destruct

# a = ("A", "B", 4, "C")
# x, y, _ , z = a
# print(x)
# print(y)
# print(z)
# ---------------------------------------------------------

# Set ----------------------------------------------------
# Set Not Be Ordered And Not Indexed
# myset = {1, 2, 3, 4}

# print(myset)

# Set Methods
# 1- defference() a - b
# a = {1, 2, 3, 4}
# b = {1, 2, "Yousef", "Osama"}# => {3, 4}
# c = a.difference(b)

# print(c)

# intersection() a & b
# a = {1, 2, 3, "x", "Yousef"}
# b = {1, "Yousef", "P", "x"}

# print(a.intersection(b))# => {'x', 1, 'Yousef'}

# symmetric_difference() => Elements do not exist between A and B
# a = {1, 2, 3, 4, 5, "X"}
# b = {"Yousef", "Osama", 1, 2, 4, "X"}

# print(a.symmetric_difference(b))# => {'Osama', 3, 5, 'Yousef'}

# issuperset() => if Elements in var(a) Exist in var(b) return true or false
# a = {1, 2, 3, 4}
# b = {1, 2, 3}

# print(a.issuperset(b))# => True

# issubset() => if Elements in var(b) Exist in var(a) return true or false
# a = {1, 2, 3, 4}
# b = {1, 2, 3}

# print(a.issubset(b))# => False

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {5, 6, 7, 8}

# print(a.isdisjoint(b))# => False
# print(a.isdisjoint(c))# True

# --------------------------------------------------------

# Dictionary---------------------------------------------------------
# user = {
#   "name" : "Yousef",
#   "age" : 15,
#   "Country" : "German",
#   "Skills" : ["Html", "Css", "JS", "Python"]
# }

# print(user)
# print(user["Country"])# => "German"
# # OR
# print(user.get("Country"))

# print(user.keys())# => dict_keys(['name', 'age', 'Country', 'Skills'])
# print(user.values())# => dict_values(['Yousef', 15, 'German', ['Html', 'Css', 'JS', 'Python']])

# Two-Dimensional Dictionary
# lang = {
#   "frist":{
#     "name": "HTML",
#     "progress": "90%"
#   },
#   "Secound":{
#     "name": "Css",
#     "progress": "70%"
#   },
#   "Third":{
#     "name": "JS",
#     "progress": "60%"
#   }
# }

# print(lang)
# print("_" * 80)
# print(lang["frist"])
# print("_" * 80)
# print(lang["Secound"]["progress"])
# print("_" * 80)
# print(lang.keys())
# print("_" * 80)
# print(lang.values())

# Create Dictionary From Variables
# framework1 = {
#   "name": "Vue.Js",
#   "progress": "60%"
# }
# framework2 = {
#   "name": "React.Js",
#   "progress": "90%"
# }
# framework3 = {
#   "name": "Angler.Js",
#   "progress": "50%"
# }

# allframeworks = {
#   "frist": framework1,
#   "Secound": framework2,
#   "Third": framework3
# }

# print(allframeworks)

# print(framework1["name"])


# Dictionary Methods

# Clear()
# framework = {
#   "name": "Angler.Js",
#   "progress": "50%"
# }
# framework.clear()
# print(framework)# => {} Empty

# update() => Add New Dictionary
# member = {"name": "yousef"}
# member.update({"age": 15})
# print(member)

# copy()
# main = {
#   "name": "yousef",
#   "age": 15
# }

# b = main.copy()
# print(b)
# main.update({"conutry": "German"})

# setdufauld()
# user = {
#   "name": "Yousef"
# }

# print(user.setdefault("age", 15))# => 15

# # popitem()
# member = {
#   "name": "Yousef",
#   "Skills": "Fixed Cars"
# }

# print(member.popitem())# => Last Item In Dict

# items()# Add Dict in Tuple in list in Tuples
# member = {
#   "name": "Yousef",
#   "Skills": "Fixed Cars"
# }

# allitems = member.items()
# print(member)
# member["age"] = 15
# print(allitems)

# # fromkeys()
# a = ("KeyOne", "KeyTwo", "KeyThree")
# b = "x"

# print(dict.fromkeys(a, b))# => {'KeyOne': 'x', 'KeyTwo': 'x', 'KeyThree': 'x'}
# ---------------------------------------------------------


# Comparison Operators

# #  == equal
# print(100 == 100)# => True
# print(100 == 200)# => False
# print(100 == 100.00)# => True


# # != Not equal
# print(100 != 100)# => False
# print(100 != 200)# => True
# print(100 != 100.00)# => False


# # (>)
# print(100 > 100)# => False
# print(100 > 200)# => False
# print(100 > 100.00)# => False
# print(100 > 40)# => True


# # (<)
# print(100 < 100)# => False
# print(100 < 200)# => True
# print(100 < 100.00)# => False
# print(100 < 40)# => False


# User Input--------------------------------------------------
# fristName = input("Enter Frist Name: ")
# middleName = input("Enter Middle Name: ")
# lastName = input("Enter Last Name: ")

# fristName = fristName.strip().capitalize()
# middleName = middleName.strip().capitalize()
# lastName = lastName.strip().capitalize()

# print(f"Hello {fristName:.1s} {middleName} {lastName}")


# # Email Slice
# email = "elesawey@gmail.com"
# username = email[:email.index("@")]
# domain = email[email.index("@")+ 1:]

# print(f"Your Username Is {username} & Your Domain Is {domain}")


# name = input("Enter Your Full Name: ")
# email = input("Enter Your Email: ")

# username = email[:email.index("@")]
# domain = email[email.index("@")+1:]
# name = name.strip().capitalize()
# email = email.strip()
# username = username.strip()
# domain = domain.strip()
# print(f"Hello {name} Your Email is {email}")
# print(f"Your Username Is {username} & Your Domain Is {domain}")


# Calc Age

# age = int(input("Enter Your Age: "))

# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# print(f"You Lived For {months} Monthes")
# print(f"You Lived For {weeks:,} Weeks")
# print(f"You Lived For {days:,} Days")
# print(f"You Lived For {hours:,} Hours")
# print(f"You Lived For {minutes:,} Minutes")
# print(f"You Lived For {seconds:,} Seconds")
# ----------------------------------------------------------------
# ---------------------------------------------------------------
# Control Flow ------> If, Eilf, Else
# userName = str(input("Enter Your Name: ")).strip().capitalize()
# userCountry = str(input("Enter Your Country: ")).strip().capitalize()
# isStudent = str(input("Do You Student (Yes / No):) ")).strip().capitalize()
# courseName = "Python For Every Body"
# coursPrice = 100

# if userCountry == "Egypt":

#   if isStudent == "Yes":
#     print(f"Hello Student {userName} Cuz You Student We Give You Disccount")
#     print(f"The Course {courseName} Will Be Free")

#   else:
#    print(f"The Course {courseName} Will Be Price Is {coursPrice - 90}$")
#    print(f"Hello {userName} Cuz You From {userCountry} We Make a Disccount 80%")


# elif userCountry == "Ksa" or userCountry == "Bahrain" or userCountry == "Kuwait":

#   if isStudent == "Yes":

#     print(f"Hello Student {userName} Cuz You Student We Give You Disccount")
#     print(f"The Course {courseName} Will Be Free")

#   else:
#    print(f"The Course {courseName} Will Be Price Is {coursPrice - 15}$")
#    print(f"Hello {userName} Cuz You From {userCountry} We Make a Disccount 15%")

# elif userCountry == "Suria" or userCountry == "Lebanon":

#  if isStudent == "Yes":
#     print(f"Hello Student {userName} Cuz You Student We Give You Disccount")
#     print(f"The Course {courseName} Will Be Free")

#  else:
#   print(f"The Course {courseName} Will Be Price Is {coursPrice - 85}$")
#   print(f"Hello {userName} Cuz You From {userCountry} We Make a Disccount 85%")

# elif userCountry == "Sudan" or userCountry == "Somalia":

#  if isStudent == "Yes":
#     print(f"Hello Student {userName} Cuz You Student We Give You Disccount")
#     print(f"The Course {courseName} Will Be Free")

#  else:
#   print(f"The Course {courseName} Will Be Price Is {coursPrice - 90}$")
#   print(f"Hello {userName} Cuz You From {userCountry} We Make a Disccount 90%")

# else:
#   print(f"Hello {userName} the Course {courseName} Price is {coursPrice}$")


# Ternary If
# movieRate = int(input("Enter Your Age: "))

# if movieRate <= 16:
#   print("The Movie Not Good For You")

# else:
#   print("The Movie So Good For You And Happy Wathing")

# OR

# Short If
# print("Move Not good For You" if movieRate <= 16 else "The Move So Good For You")


# print(" You Can Write Frist Letter Or Full Name of The Time Unit ".center(80, "#"))

# age = int(input("Enter Your Age: "))

# timeUnit = input("Enter Time Unit: Months, Weeks, Days, Hours, minuts: ").strip().lower()


# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# if timeUnit == "months" or timeUnit == "m":
#   print(f"You Choosed {timeUnit.capitalize()}")

#   print(f"You Lived For {months} Months")

# elif timeUnit == "weeks" or timeUnit == "w":
#   print(f"You Choosed {timeUnit.capitalize()}")

#   print(f"You Lived For {weeks} Weeks")

# elif timeUnit == "days" or timeUnit == "d":
#   print(f"You Choosed {timeUnit.capitalize()}")

#   print(f"You Lived For {days:,} Days")

# elif timeUnit == "hours" or timeUnit == "h":
#   print(f"You Choosed {timeUnit.capitalize()}")

#   print(f"You Lived For {hours:,} Hours")

# elif timeUnit == "minuts" or timeUnit == "min":
#   print(f"You Choosed {timeUnit.capitalize()}")

#   print(f"You Lived For {minutes:,} Minuts")

# elif timeUnit == "secounds" or timeUnit == "s":
#   print(f"You Choosed {timeUnit.capitalize()}")

#   print(f"You Lived For {seconds:,} Seconds")

# else:
#   print(f"The Unit Time {timeUnit} Not Exist")
# ----------------------------------------------------------------
#
#
# Membership Operators
# ----------------------------------------------------------------

# 1- in
# 2- not in
# frinds = ["Yousef", "Mohammed", "Ali"]

# print("Yousef" in frinds)# => True
# print("Ali" not in frinds)# => False


# myCountry = input("Enter Your Country: ").strip().capitalize()
# stydent = input("Do You Student? (Yes , No): ").strip().capitalize()
# productName = "Mac 16GB 500SSD"
# productPrice = 1000
# discountCountries = "Egypt", "Syria", "Sudan", "Libya", "Lebenon"
# discountCountries2 = "Uk" ,"Usa", "Ksa", "Italy", "Kuwait"

# if myCountry in discountCountries:

#   if stydent == "Yes":
#     print(f"You Want Buy {productName} And Cuz You Student You Have Discount 50% Will be Product Price {productPrice - 500}$")

#   else:
#     print(f"Hello Sir, You Want buy {productName} & You Have DisCount 30% Will be Product Price {productPrice - 300}$")

# elif myCountry in discountCountries2:

#   if stydent == "Yes":
#     print(f"You Want Buy {productName} And Cuz You Student You Have Discount 20% Will be Product Price {productPrice - 200}$")

#   else:
#     print(f"Hello Sir, You Want buy {productName} & You Have DisCount 10% Will be Product Price {productPrice - 100}$")


# else:
#   print("You Not Have Discount")


# Big Exercize

# admins = ["Yousef", "Ali", "Mohammed", "Khalid", "Mearna", "Taha"]

# members = ["Louis", "Ehab", "Abd Elkader", "Aliya", "Adham", "Samy"]

# name = input("Enter Your name: ").strip().capitalize()

# if name in admins:
#   print(f"Hello {name}  Welcome to Back")

#   option = input("(Delete(D) or Update(U)) Your Name Please: ").strip().capitalize()

#   if option == "Update" or option == "U":

#      newName = input("Enter A New Name: ").strip().capitalize()

#      admins[admins.index(name)] = newName

#      print(f"Succssfful Updated Your Name To {newName}.")

#   elif option == "Delete"or option == "D":

#     admins.remove(name)

#     print(f"Succssfful Delete Your Name.")


#   else:
#     print("Wrong, The Option Not Exist")

# else:

#   status = input("Are You Want Be Member in Groub Us? (Yes, No): ").strip().capitalize()

#   if status == "Yes" or status == "Y":

#      members.append(name)

#      print(f"You Have Been Added Sir {name}")
#      print(members)

#   else:
#      print("Ok, You Are Not Added")
# ----------------------------------------------------------------

# While Loop  -----------------------------------------------------------------
# a = 0

# while a < 15:

#    print(a)

#    a += 1

# print("Time UP") # => else

# # Empty List to Fill Later
# myFavouritewebs = []

# # Maximum Allowed webs
# maximumWebs = 5

# while maximumWebs > 0 :

#     # input The New Website
#     web = input("Website Name without https:// ")

#     # Add New Website To List
#     myFavouritewebs.append(f"https://{web.strip().lower()}")

#     # Decrease One Number From Allowed Website
#     maximumWebs -= 1

#     # print The Add Message
#     print(f"Website Added, {maximumWebs} Places Left")

#     print(myFavouritewebs)

# else:
#   print("Bookmark Is Full, You Can't Add More")


# # Check If List is Not Empty
# if len(myFavouritewebs) > 0:

#   # Sort The List
#   myFavouritewebs.sort()

#   index = 0

#   while index < len(myFavouritewebs):

#       print(myFavouritewebs[index])

#       index += 1


# ------------------------------------------------------------------------

# tries = 5

# mainPass = "You1980"

# inputPass = input("Enter Your Password: ")

# while inputPass != mainPass:

#     tries -= 1

#     print(f"wrong Password, {'Last' if tries == 0 else tries} Another Chance")

#     inputPass = input("Enter Your Password: ")


#     if tries == 0:

#       print("All Tries Is Finshed")

#       break

# else :

#   print("Correct Password")


# tries = 5

# mainPass = "y1980"

# inputPass = input("Enter Your Password: ")

# while inputPass != mainPass:

#     tries -= 1

#     print(f"Wrong Password, {'Last' if tries == 0 else tries} Another chence")

#     inputPass = input("Enter Your Password: ")

#     if tries == 0:

#       print("All tries Finshed")

#       break

# else:

#   print("Correct Password")


# For -----------------------------------------------------------------

# mySkills = {
#   "Html": "90%",
#   "Css": "80%",
#   "Js": "40%",
#   "Python": "50%",
#   "PHP": "20%",
# }

# for skill in mySkills:# Get Keys ----> Html Css Js Python PHP

# print(skill)

# # Get Keys And Values
# print(f"My Progress in Lang {skill} Is: {mySkills[skill]}")

# OR

# print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}")


# Nested Loop

# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ["Html", "Css", "js"]

# for name in peoples: # Outer Loop
#   print(f"{name} Skills Is: ")

#   for skill in skills: # Inner Loop
#     print(f"- {skill}")


# people = {
#   "Yousef": {
#     "Html": "90%",
#     "Css": "70%",
#     "Js": "60%"
#   },
#   "Osama": {
#     "Html": "70%",
#     "Css": "60%",
#     "Js": "80%"
#   },
#   "Ali": {
#     "Html": "100%",
#     "Css": "60%",
#     "Js": "80%"
#   },
# }

# for name in people:
#   print(f"Skills And Progress For {name} Is: ")

#   for skill in people[name]:
#     print(f"- {skill} => {people[name][skill]}")

# Break, Continue, Pass

# 1- Continue => Stop In Value then Continue
# myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# for x in myNumbers:

#    if x == 13:

#      continue

#    print(x)

# print("#" * 60)

# # Break => Stop In Value And Not Continue
# for x in myNumbers:

#    if x == 10:

#      break

#    print(x)

#   #  Pass => Skip
# for x in myNumbers:

#    if x == 13:

#      pass

#    print(x)


# mySkills = {
#     "HTML": "80%",
#     "CSS": "90%",
#     "Js": "60%",
#     "Python": "40%",
# }

# for skillsKey, skillsvalue in mySkills.items():

#     print(f"{skillsKey} => {skillsvalue}")

# myUltmateSkills = {
#     "HTML": {
#         "main": "80%",
#         "pugjs": "80%",
#     },

#     "Css":{
#         "main": "90%",
#         "Sass": "70%"
#     }
# }

# for mainKey, mainValue in myUltmateSkills.items():

#     print(f"{mainKey} => {mainValue}")

#     for childKey, childValue in mainValue.items():

#         print(f"- {childKey} => {childValue}")
# ---------------------------------------------------------------------


# ------ Function + return ------------------------------------------------------------

# def myfunction():

#     print("Hello World Form Inside Function")

# myfunction()

# OR

# def myfunction():
#     return "Hello World Form Inside Function"
#
#
# print(myfunction())

# Function Parameters + Arguments

# def => [difine] Function Keyword
# sayhello() => Function Name
# name => Parameter
# print(f"Hello {name}") => Task
# sayhello("yousef") => Arguments

# a, b, c = ["Yousef", "Ali", "Mohammed"]
# def sayhello(n):
#
#     print(f"Hello {n}")
#
# sayhello(a)
# sayhello(b)
# sayhello(c)

# def addition(num1, num2):
#
#     if type(num1) != int or type(num2) != int:
#         print("Just Integer Allowed")
#
#     else:
#         print(num1 + num2)
#
# addition(100, 300)# => 400
# addition(-50, 100)# => 50
# addition(100, "yousef")

# def full_name(frist, middle, last):
#
#     print(
#         f"Hello {frist.strip().capitalize()} {middle.strip().upper():.1s} {middle.strip().capitalize()}"
#     )
#
# full_name("Yousef", "Taha", "Elesawey")


# How Make Packing And Notpacking to Arguments  *Arg
# if Add (*) select All

# def say_hello(*people):# same => num1, num2, num3, num4, num5 , num6, num7
#
#     for name in people:
#         print(f"Hello {name}")
#
# say_hello("Mohammed", "Ali", "Galal", "Yousef", "Taha", "kamal", "Ehab")

# def show_details(name, *skills):
#     print(f"Hello {name} Yor Skills Is: ")
#     for skill in skills:
#         print(skill)
# show_details("yousef", "HTML", "CSS", "JS", "PYTHON")
# show_details("Ahmed", "HTML", "CSS", "JS", "PYTHON", "Danjngo", "SQL")

# Default Parameters

# def say_hello(name, age= "Unknown", country= "Unknown"):# Unknow If country is Empty
#
#     print(f"Your Name Is: {name} and Your age Is: {age} & Your Country Is: {country}")
#
# say_hello("yousef", 15, "German")
# say_hello("ali", 35, "egy")
# say_hello("samy", 25)
# say_hello("Khaild")

# Packing and Unpacking Function Arguments **KWArgs => Useing Dictionary

# my_Skills = {
#     "HTML": "90%",
#     "Css": "80%",
#     "Js": "70%"
# }

# def show_skills(**skills):
#
#     for skill_Key, skill_Value in skills.items():
#
#         print(f"Your Is Skill: {skill_Key} And Your Is Progress: {skill_Value}")
#
# # show_skills(Html = "80%", Css = "70%", Js = "60%")# => duct
#
# # OR Useing Duct Out Function
#
# show_skills(**my_Skills)

# Exersize

# mytuple = ("Html", "Css", "Js", "Python")

# myskills = {
#  "Html": "95%",
#  "Css": "90%",
#  "Js": "80%",
#  "Python": "40%",
# }
# def show_Skills(name, *skills, **myskills):
#
#     print(f"Hello {name} \nSkills Without Progress: ")
#
#     for skill in skills:
#
#         print(f"- {skill}")
#
#     for skill_Key, skill_value in myskills.items():
#
#         print(f"Your Skills Is: {skill_Key} and your Progress Is: {skill_value}")
#
# show_Skills("Yousef", *mytuple, **myskills)

# -----------------
# Function Scope
# Global Scope => Get Item Out Function
# -----------------
# x = 1              # Global Scope
#
# def one():
#
#     global x
#
#     x = 2
#
#     print(f"Print Variable From Function Scope {x}") # => 1 Get x out Function
#
# print(f"Print Variable From Global Scope {x}") # => 2 Get x in Function
#
# one()
#
# def two():
#
#     x = 4
#
#     print(f"Print Variable From Function Scope {x}") # => 2 Get x out Function
#
# print(f"Print Variable From Global Scope {x}") # => 4 Get x in Function
#
# two()


# Function Recursion

# def cleanword(word):
#
#     if len(word) == 1:
#         return word
#
#     if word[0] == word[1]:
#         return cleanword(word[1:])
#
#     return word[0] + cleanword(word[1:])
#
# print(cleanword("wwwooorrrldd"))

# lambda Function => Not Have Name
# Anonymous Function

# hello = lambda name, age: f"Hello {name} Your Age Is {age}"
#
# print(hello("Yousef", 15))


# ---------------------------------------------------------------------

# Start Files -----------------------------------------------------------------


# import os
#
# # Directory For The Opened File
# print(os.path.dirname(os.path.abspath(__file__)))
#
# # Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# # print(f"Get a truly path file{os.path.abspath(__file__)}")
#
# print(os.getcwd())
#
# f = open("c:\yousef.txt")


# Read
# myFile = open("c:\yousef.txt", "r")

# print(myFile)# => All Ditales inside File
# print(myFile.name)# => File Name
# print(myFile.mode)# => Mode File
# print(myFile.encoding)# => Encoding File => cp1256

# print(myFile.read())# => read Every Think In File
# print(myFile.read(4))# => read 4 some Thinks Only

# print(myFile.readline())# => read just ONE line
# print(myFile.readline(5))# => read Five Charctars Only

# print(myFile.readlines())# => read Data in Lines And Convert To List

# for line in myFile:
#
#     print(f"- {line}")
#
#     if line.startswith(";"):
#
#         break
#
# # Close The File
# myFile.close()

# Write In Text File
# myFile = open("c:\scound.txt", "w")
#
# myFile.write("Hello Every One I'm Yousef I'm Software Engenaring\n")
# myFile.write("I'm 16 Years Old in damytta School")

# myFileFun = open(r"C:\python.testing\fun.txt", "w")# => write
#
# myFileFun.write("Elesawey SoftWare\n" * 1000)

# myList = ["Yousef\n", "Taha\n", "Awad\n", "Elesawey\n"]
#
# myFile = open("c:\yousef.txt", "w")
#
# myFile.writelines(myList)

# myFile = open("c:\yousef.txt", "a")# => Append
#
# myFile.write("\n\n\nelesawey")

# myFile = open("c:\yousef.txt", "a")

# myFile.truncate(7)

# print(myFile.tell())# => index Equal 6

# myFile = open("c:\yousef.txt", "r")
#
# myFile.seek(11)# => Python Languge Programing
#
# print(myFile.read())

# import os
#
# os.remove("c:\yousef.txt") # => Delete Yousef.txt File
# -------------------------------------------------------------------------------

# Built In Function-------------------------------------------------------------------------------

# all => Check If All Elements Is True Or False
# Any => check Element //  // // //
# bin => Computer Languge (0,1)
# id => Get ELement Addraise from Momury

# x = [0, 0, []]

# if all(x):
#     print("All Elements Is True")
#
# else:
#     print("Mybe You Have one False")

# if any(x):
#     print("There's Element At Least One Element Is True")
# else:
#     print("There's No Any True Elements")

# print(bin(100))# => 0b1100100

# a = 1
# b = 2
#
# print(id(a))# => 2583044974896
# print(id(b))# => 2583044974928

# Sum()
# round()
# range()
# print()

# Sum()# value = 0, Addation All Numbers
# a = [10, 20, 19, 40]
# print(sum(a))# => 89
# print(sum(a, 40))# => 129

# print(round(150.499)) # => 150
# print(round(150.501)) # => 151
# print(round(150.501, 2)) # => 151.5
# print(round(150.555, 2)) # => 151.56

# print(list(range(0, 20, 2)))# Step number between Every Number

# print()
# print("Hello", "i'm", "Yousef", "Taha", "SoftWare", "Devolper", sep="    |    ")


# abs()# covert from Posative To Nagtitave
# pow()
# min()
# max()
# slice()

# abs()
# print(abs(100))# => 100
# print(abs(-100))# => 100
# print(abs(10.19))# => 10.19
# print(abs(-100.98))# => 100.98

# print(pow(2, 4))# => 2 * 2 * 2 * 2 = 16

# slice()
# a = ["A", "B", "C", "D", "E", "F"]
#
# print(a[slice(2, 5)])# => ['C', 'D', 'E']

# MAP

# Normal Function

# def formatText(text):
#
#     return f"-  {text.strip().capitalize()}  -"

# Useing Lambda Function

# mytexts = ["YOusef", "AHMED", "sAYed"]
#
# for name in map(lambda text: f"-  {text.strip().capitalize()}  -", mytexts):
#
#     print(name)


# FILTTRE

# Fillter In Normal Function
# def checkNumber(num):
#
#     if num > 10:
#
#         return num

# Filter Useing Lambda Function
# myNumbers = [1, 20, 30, 40, 5 , 50, 3]
#
# for number in filter(lambda num: num > 10, myNumbers):
#
#     print(number)# => 20, 30, 40, 50

# Example 2

# Nomal Function
# def checkName(name):
#
#     return name.startswith("O")
#
# mymember = ["Yousef", "Osama", "Othman", "Ali", "Omr", "Omnia"]
#
# myReturnData = filter(checkName, mymember)
#
# for person in myReturnData:
#
#     print(person)# => Osama Othman Omr Omnia

# Lambda Function

# mymember = ["Yousef", "Osama", "Othman", "Ali", "Omr", "Omnia"]


# for person in filter(lambda name: name.startswith("O"), mymember):
#
#     print(person)# => Osama Othman Omr Omnia
#
#     Reduce
# from functools import reduce
#
# def sumAll(num1, num2):
#
#     return num1 + num2
#
# numbers = [1, 8, 2, 9 ,100]
#
# result = reduce(sumAll, numbers)
# # How Calc it ? => ((((1 + 8) + 2) + 9)+ 100) => 120
# print(result)# output => 120

# Lambda Function

# numbers = [1, 8, 2, 9 ,100]
#
# result = reduce(lambda num1, num2: num1 + num2, numbers)
# # How Calc it ? => ((((1 + 8) + 2) + 9)+ 100) => 120
# print(result)# output => 120

# enumerate()
# mySkills = ["Html", "Css", "JS", "PHP"]
#
# mySkillsWithCounter = enumerate(mySkills, 20)
#
# for counter, skill in mySkillsWithCounter:
#
#     print(f"{counter}- {skill}")

# reversed()
# myString = "Elesawey"
#
# for letter in reversed(myString):
#     print(letter)
# -------------------------------------------------------------------------------

# Built In Module --------------------------------------------------------------

# 1- Random
# import random
#
# print(f"print Random Float Number => {random.random()}")

# Show All Function Inside Module

# import random
#
# print(dir(random))

# import one Or two Function From Module

# from random import randint
#
# print(f"Print Random Integer => {randint(1, 100)}")

# How Create My Module

# import sys
#
# sys.path.append(r"D:\Games")
#
# print(sys.path)

# import yousef as yo
#
# print(dir(yo))
#
# yo.sayHello("yousef")
# yo.sayHello("Ali")
# yo.sayHello("Omar")
#
# yo.sayGutenMorgin("yousef")
# yo.sayGutenMorgin("Ali")
# yo.sayGutenMorgin("Omar")

# Select One Function Only

# from yousef import sayHello as sH
#
# sH("Ali")

# import pyfiglet
# import termcolor
#
# print(termcolor.colored(pyfiglet.figlet_format("PYTHON"), color="yellow"))

# -------------------------------------------------------------------------------

# # Date And Time
#
# import datetime
#
# # print(datetime.datetime.now())# => 2023-07-15 13:39:34.114533
#
# # Print The Current Year
# print(datetime.datetime.now().year)# => 2023
#
# # Print The Current Month
# print(datetime.datetime.now().month)# => 7
#
# # Print The Current day
# print(datetime.datetime.now().day)# => 15
#
# # Print The Current hour
# print(datetime.datetime.now().hour)# => 13 = 1
#
# # Print The Current minute
# print(datetime.datetime.now().minute)# => 48
#
# # Print The Current second
# print(datetime.datetime.now().second)# => 52
#
# # start and End of Time
# print(datetime.time.min)
# print(datetime.time.max)
#
# # Specific Time
# print(datetime.datetime(2007, 10, 6))
#
# print(" ." * 60)
#
# # Exercize
# mybirthday = datetime.datetime(2007, 10, 1)
# dateNow = datetime.datetime.now()
#
# print(f"My birthday is {mybirthday}\n And My Age Now Is: {(dateNow - mybirthday).days} Days")

# Format DateTime

# 1- https://www.geeksforgeeks.org/python-strftime-function/

# import datetime
#
# mybirthDay = datetime.datetime(2007, 10, 6)
#
# print(mybirthDay.strftime("%d"))# => October
#
# print(mybirthDay.strftime("%m"))# => Saturday
#
# print(mybirthDay.strftime("%Y"))# => 2007

# print(f"I Borned At {mybirthDay.strftime('%Y/%m/%d')}")
# -------------------------------------------------------------------------------

# Iterator and iterable# ------------------------------------------------------------------

# String, tuple, Set, Dict, List = Iterable
#
# myStr = "Yousef"
#
# for letters in myStr:
#
#     print(letters, end="    ")# => Y    o    u    s    e    f

# Convert iterable to Iterator
# mystring = "Yousef"
#
# mystring = iter(mystring)
#
# print(next(mystring))
# print(next(mystring))
# print(next(mystring))
# print(next(mystring))
# print(next(mystring))
# print(next(mystring))

# -------------------------------------------------------------------------------

# Generators ---------------------------------------------------------------------

# def myGenerator():
#
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# myGen = myGenerator()

# print("Hello From python")
# print(next(myGen))# => 1
# print("Hello From python")
# print(next(myGen))# => 2
# print("Hello From python")
# print(next(myGen))# => 3
# print("Hello From python")
# print(next(myGen))# => 4

# for nums in myGen:
#
#     print(nums)
# -------------------------------------------------------------------------------


# Decorators ---------------------------------------------------------------------

# Introdaction

# def myDecoration(func):
#
#     def nestedFunction():
#
#         print("Before")
#
#         func()
#
#         print("After")
#
#     return nestedFunction()
#
#
# @myDecoration
# def sayHallo():
#
#     print("Hello Every One.")
#
# print("-----" * 20)
#
# @myDecoration
# def sayhowAreYou():
#
#     print("Hello are You Bro.")

# Second Lesson

# def myDecoration(func):
#
#     def nestedFunction(num1, num2):
#
#         if num1 < 0 or num2 < 0:
#
#             print("Beware One Number Is less Than Zero")
#
#         func(num1, num2)
#
#     return nestedFunction
#
# @myDecoration
# def calculate(n1, n2):
#
#     print(n1 + n2)
#
# calculate(40, -60)

# Third Lesson

# def myDecoration(func):
#
#     def nestedFunction(*numbers):
#         for number in numbers:
#
#             if number < 0:
#
#                 print("Beware One Number Is less Than Zero")
#
#         func(*numbers)
#
#     return nestedFunction
#
# @myDecoration
# def calculate(n1, n2, n3, n4):
#
#     print(n1 + n2 + n3 + n4)
#
# calculate(-40, 60, 30, 20)
# -------------------------------------------------------------------------------

# Zip()----------------------------------------------------------------------

# mylist1 = [1, 2, 3, 4, 5, 6]
# mylist12 = ["A", "B", "C"]
#
# ultimateList = zip(mylist1, mylist12)
#
# for item in ultimateList:
#
#     print(item)# Output => (1, 'A'), (2, 'B'), (3, 'C')

# ------------------------------------------------------

# mylist1 = [1, 2, 3, 4, 5]
# mylist12 = ["A", "B", "C"]
# tuple1 = ("Yousef", "Ali", "Hamed", "Sayed", "Mohammed", "Ahmed")
# dict1 = {"Name": "Yousef", "Age": 15, "Country": "UK"}
#
# for item1, item2, item3, item4 in zip(mylist1, mylist12, tuple1, dict1):
#
#     print(f"List 1 Item => {item1}")
#
#     print(f"List 2 Item => {item2}")
#
#     print(f"Tuple 1 Item => {item3}")
#
#     print(f"Dictionary 1 Key => {item4} Value => {dict1[item4]}")

# ----------------------------------------------------------------------------

# Image Manipulation With Pillow

# from PIL import Image
#
# # open The Image
#
# myImage = Image.open(r"D:\javascript.learn\aven_gate_01 (1).webp")
#
# # show Image
#
# myImage.show()
#
# # Crodped Image
#
# myBox = (0, 0, 400, 400)
#
# mycroppedImage = myImage.crop(myBox)
#
# # Show Cropped Image
#
# mycroppedImage.show()
#
# # Converted Mode Image
#
# myConverted = myImage.convert("L")
#
# myConverted.show()
# ----------------------------------------------------------------------------

# Documenting----------------------------------------------------------

# def sayhello(name):
#     """
#
#     :param name:
#     :return: Hello {Name}
#     """
#     print(f"Hello {name}")
#
# sayhello("yousef")
#
# # print(sayhello.__doc__)# => :param name: :return: Hello {Name}
#
# #OR
#
# help(sayhello.__doc__)# => :param name: :return: Hello {Name}
# --------------------------------------------------------------------------

# PyLint -------------------------------------------------------------------------

# def sayHello(name):
#
#     msg = "Hello"
#
#     return f"{msg} {name}"

# --------------------------------------------------------------------------

# Errors -------------------------------------------------------------------------

# x = -10
#
# if x < 0:
#      raise Exception(f"The Number {x} Less than Zero")# => Erorr
#
# else:
#     print("This Number Is ok")

# Exercize

# y = "yousef"
#
# if type(y) != int:
#
#     raise ValueError("Only Numbers Allowed")# ValueError: Only Numbers Allowed
#
# print("print message after if Condtion")
# --------------------------------------------------------------------------------


# Try, Except, Else, Finally-----------------------------------------------------

# try:# Try The Code And Test Erorr
#
#     age = int(input("Enter Your Age: "))
#
#     print("Good This Is Integer Form Try")# i can make Else form try Also
#
# except:# Handel The Erorrs If It's Found
#
#     print("Wrong, This Not Intager")
#
# else:# If Theres Not Erorrs
#
#     print("Good This Is Integer Form Else")
#
# finally:
#
#     print("From Finally Whatever Happenes")

#
# Big Exercize

# theFile = None
#
# the_tries = 5
#
# while the_tries > 0:
#
#     try:
#
#         print("Enter The File Name With Absolute Path To Open")
#
#         print(f"{the_tries} Tries Lift")
#
#         file_Name = input("Enter The File Name: ").strip()
#
#         theFile = open(file_Name, "r")
#
#         print(theFile.read())
#
#         print(f"Succssffull Added Your File {file_Name}")
#         break
#
#     except FileNotFoundError:
#
#         print("The File Is Not Found Or Name Is Not Valid")
#
#         the_tries -= 1
#
#     except:
#
#         print("Erorr Happen")
#
#     finally:
#
#         if theFile is not None:
#
#             theFile.close()
#
#             print("File Closed")
#
# else:
#
#     print("All Tries Is Done")

# --------------------------------------------------------------------------------


# Debugging Code ------------------------------------------------------------------

# myList = [1, 2, 3, 4, 5, 6]
#
# myDict = {"Name": "Yousef", "Age": 15, "Country": "Egypt"}
#
# for nums in myList:
#
#     print(nums)
#
# for key, value in myDict.items():
#
#     print(f"{key} => {value}")
#
# def functionOne():
#
#     print("Hello From Function One.")
#
# functionOne()
# --------------------------------------------------------------------------------


# Type Hinting----------------------------------------------------------------------

# ->

# def sayHello(name) -> str: #  ( -> )   This Is String
#
#     print(f"Hello {name}")
#
# sayHello("Yousef")
#
#
# def calc(num1, num2) -> int :
#
#     print(num1 + num2)
#
# calc(10, 40)
# --------------------------------------------------------------------------------


# Regular Expressions -------------------------------------------------------------

# Email => [a-z{, 6}]+@[a-z]+\.[a-z]+

# |   or

# \  Escape Special Character

# ()  separate Groups

# (\d-|\d\)|\d>)\s(\w+)# Matching ----------------\/

# 1- Html
# 2- Css
# 3- JavaScript
#
# 1) Html
# 2) Css
# 3) JavaScript
#
# 1> Html
# 2> Css
# 3> JavaScript


# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\)) # Matching ----------------\/

# 234 4997 456
#
# 654 3461 (653)


# (https?://)(www.)?(\w+.)(org|net|com)

# http://www.yousef.net
#
# http://elesawey.com
#
# https://gaze.org


# import re

# my_Search = re.search(r"[A-Z]{2}", "yousef EElesawey")
#
# print(my_Search)# span=(7, 8)    match='EE'>
#
# print(my_Search.span())# (7, 8)
#
# print(my_Search.string)

# my_Email = yousef@gmail.com
#
# format_Email = re.search(r"[a-z0-9]+@[a-z]+\.[com|org|net]", my_Email)
#
# if format_Email:
#
#     print("Your Email Is Valied")
#     print(format_Email.string)
#     print(format_Email.span())
#
# else:
#
#     print("Your Email Is Not Valied")


# email_input = input("Enter Your Email: ")
#
# format_Email = re.findall("[A-z0-9]+@[A-z0-9]+\.com|net", email_input)
#
# empty_list = []
#
# if format_Email != []:
#
#     empty_list.append(format_Email)
#
#     print("Email Added")
#
# else:
#
#     print("Invalid Email")


# split()

# import re
#
# string_One = "Yousef Taha Elesawey Bug Bounty Hunter"
#
# search_One = re.split(r"\s", string_One)
#
# search_Two = re.split(r"\s", string_One, 1)
#
# print(search_One)# => ['Yousef', 'Taha', 'Elesawey']
#
# print(search_Two)# => ['Yousef', 'Taha Elesawey Bug Bounty Hunter']
#
# print("-_-" * 50)
#
# string_three = "Was --_- deine__ du _-beruf"
#
# search_Three = re.split(r"- | _", string_One, 1)
#
# print(search_Three)# => ['Yousef Taha Elesawey Bug Bounty Hunter']
#
# print("-_-" * 40)

# import re
#
# print(re.sub(r"\s", " - ", "Yousef Taha Elesawey"))


# link formater

# import re
#
# link = input("Enter The Url: ")
#
# my_Formater = re.search(r"(https?://)(www.)?(\w+)\.(org|net|com)(:\d+)?(/\w+.+)?", link)
#
# if my_Formater:
#
#     print("Correct Url")
#
# else:
#
#     print("Wrong Url")
# ---------------------------------------------------------------------------------

# oop------------------------------------------------------------------------------

# class Member:
#
#     def __init__(self):
#
#         print("A New Member Has Been Added")
#
# member_one = Member()
# member_two = Member()
# member_three = Member()
#
# print(member_one.__class__)# => <class '__main__.Member'>

##################################################

# class Member:
#
#     def __init__(self, frist_name, middle_name, last_name):
#
#         self.fname = frist_name
#         self.mname = middle_name
#         self.lname = last_name
#
# member_one = Member("Yousef", "Taha", "Elesawey")
# member_two = Member("Amr", "khalied", "Sayed")
# member_three = Member("Hassan", "Galal", "Ali")
#
# print(member_one.fname, member_one.mname, member_one.lname)# => Yousef Taha Elesawey
# print(member_two.fname, member_two.mname, member_two.lname)# => Amr khalied Sayed
# print(member_three.fname, member_three.mname, member_three.lname)# => Hassan Galal Ali

##################################################

# class Member:
#
#     def __init__(self, fristName, middleName, lastName, gender):
#
#         self.fname = fristName
#         self.mname = middleName
#         self.lname = lastName
#         self.gender = gender
#
#     def fullName(self):
#
#         return f"{self.fname} {self.mname} {self.lname}"
#
#     def mrName(self):
#         if  self.gender == "Male":
#
#             return f"Mr.{self.fname}"
#
#         if  self.gender == "Famale":
#
#             return f"Mrs.{self.fname}"
#
#         else:
#
#             return f"Hallo {self.fname}"
#
#
#     def get_all(self):
#
#         return f"Hello {self.mrName()}. your Full Name Is: {self.fullName()}"
#
# member1 = Member("Yousef", "Taha", "Elesawey", "Male")
# member2 = Member("Mona", "Mohsen", "khaliel", "Famale")
# member3 = Member("Hassan", "Ali", "Walied", "Male")
#
#
# # print(member1.fullName())
# # print(member1.mrName())
# # print(member2.fullName())
# # print(member2.mrName())
# # print(member3.fullName())
# # print(member3.mrName())
#
# print(member1.get_all())
# print(member2.get_all())
# print(member3.get_all())


########################################################

# class Member:
#
#     names_Not_Allowed = ["Shit", "Fuck", "Hell"]
#
#     web_Users = 0
#
#     def __init__(self, fristName, middleName, lastName, gender):
#
#         self.fname = fristName
#         self.mname = middleName
#         self.lname = lastName
#         self.gender = gender
#         Member.web_Users += 1
#
#     def fullName(self):
#
#         if self.fname in Member.names_Not_Allowed or self.mname in \
#         Member.names_Not_Allowed or self.lname in Member.names_Not_Allowed or self.gender in Member.names_Not_Allowed:
#
#             raise ValueError("Your Name Is Not Allow")
#
#         else:
#
#            return f"{self.fname} {self.mname} {self.lname}"
#
#     def mrName(self):
#         if  self.gender == "Male":
#
#             return f"Mr.{self.fname}"
#
#         if  self.gender == "Famale":
#
#             return f"Mrs.{self.fname}"
#
#         else:
#
#             return f"Hallo {self.fname}"
#
#
#     def get_all(self):
#
#         return f"Hello {self.mrName()}. your Full Name Is: {self.fullName()}"
#
#     def delete(self):
#
#         Member.web_Users -= 1
#
#         return f"User {self.fname} Deleted"
#
# member1 = Member("Yousef", "Taha", "Elesawey", "Male")
# member2 = Member("Mona", "Mohsen", "khaliel", "Famale")
# member3 = Member("Hassan", "Ali", "Walied", "Male")
# member4 = Member("Hell", "Fuck", "Shet", "Sisi")# Well Be Deleating
#
# print(Member.web_Users)
#
# print(member1.get_all())
# print(member2.get_all())
# print(member3.get_all())
#
# print(member4.delete())


# Class Methods And Static

# class Member:
#     users = 0
#
#     names_Not_Allowd = ["Hell", "Shit", "Fuck", "Hell"]
#
#     @classmethod
#
#     def show_Users_Count(cls):
#
#         return f"We Have {cls.users} In Our System"
#
#     @staticmethod
#     def sayHello():
#
#         return "Hello From Static Method"
#
#     def __init__(self, fristName, middleName, lastName, gender):
#
#         self.fName = fristName
#         self.mName = middleName
#         self.lName = lastName
#         self.gender = gender
#         Member.users += 1
#     def fullName(self):
#
#        if self.fName in Member.names_Not_Allowd or self.mName in Member.names_Not_Allowd or self.lName in Member.names_Not_Allowd or self.gender in Member.names_Not_Allowd:
#
#            return f"Your Name Not Allowed We Will Delete You from Group"
#
#        else:
#
#            if self.gender == "Male":
#
#                return f"Hello Mr.{self.fName} And Your Full Name Is: {self.fName} {self.mName} {self.lName}"
#
#            elif self.gender == "Female":
#
#                return f"Hello Mrs.{self.fName} Your FullName Is: {self.fName} {self.mName} {self.lName}"
#
#            else:
#
#                return f"Hello {self.fName} Your FullName Is: {self.fName} {self.mName} {self.lName}"
#
#     def delete_Users(self):
#
#         Member.users -= 1
#
#         return f"User {self.fName} Deleted"
#
# memberOne = Member("Yousef", "Taha", "Elesawey", "Male")
# memberTwo = Member("Hassan", "Ali", "Yousef", "male")
# memberThree = Member("Mona", "Galal", "Elesawey", "Female")
# memberFour = Member("Fuck", "shit", "Hell", "Male")
#
# print(memberFour.delete_Users())
#
# print(f"The Grope Contain {Member.users} Member")
#
#
# print(memberOne.fullName())
# print(memberTwo.fullName())
# print(memberThree.fullName())
# print(memberFour.fullName())
#
# print("#" * 40)
#
# print(Member.show_Users_Count())
#
# # Static Method
# print(Member.sayHello())


# Magic Methods

# class Skilles:
#
#     def __init__(self):
#
#         self.skills = ["Html", "Css", "JavaScript"]
#
#     def __str__(self):
#
#         return f"This Is My Skills => {self.skills}"# => This Is My Skills => ['Html', 'Css', 'JavaScript']
#
#     def __len__(self):
#
#         return len(self.skills)
#
# profile = Skilles()
#
# print(profile)
#
# profile.skills.append("PHP")
#
# profile.skills.append("Python")
#
# print(len(profile))# => 5

# Inheritance

# class Food:
#
#     def __init__(self, name, price):# Base Class
#
#         self.name = name
#         self.price = price
#
#         print(f"{name} Is Craeted From Base Class")
#
#     def eat(self):
#
#         print("Eat Method From Base Class")
#
# class Apple(Food):# Drived Class
#
#     def __init__(self, name, price, amount):
#
#         # Food.__init__(self, name, price)# => Same
#
#         # OR
#
#         super().__init__(name, price)# => Same
#
#         self.amount = amount
#
#         print(f"{self.name} and Price Is: {self.price} Is Created Form Derived Class And Amount Is {self.amount}")
#
#     def get_from_tree(self):
#
#         print("Get From Tree From Drived Class")
#
# # food_one = Food("Pizza")
# food_Two = Apple("Pizza", 200, 200)
# food_Two.eat()# inheritan Eat in Apple
# food_Two.get_from_tree()

# Method Override

# class BaseOne:
#
#     def __init__(self):
#
#         print("Base One")
#
# class Basetwo:
#
#     def __init__(self):
#
#         print("Base Two")
#
# class Derived(BaseOne, Basetwo):
#
#     pass
#
# my_var = Derived()# => Base One  Cuz It Frist
#
# print(Derived.mro())


# Encapsulation

# class Member:
#
#     def __init__(self, name):
#
#         self.name = name # Public I Can Change It
#
# one = Member("Yousef")
# one.name = "Mohamed"
# print(one.name)# => Mohamed
##############################################
# class Member:
#
#     def __init__(self, name):
#
#         self.__name = name #    Private Can't Call And Doing Every Think But In main Class
#
#     def sayHello(self):
#
#         return f"Hello {self.__name}"
#
# one = Member("Yousef")
# print(one.sayHello())


# Property Decorator

# class Member:
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
#     def sayhello(self):
#
#         return f"Hello {self.name}"
#
#     @property
#     def age_at_days(self):
#
#         return self.age * 365
#
# one = Member("Yousef", 15)
# print(one.name, one.age_at_days())# => Yousef 5475

# # ---------------------------------------------------------------------------------

# Data Base
#
# import sqlite3
#
#
# db = sqlite3.connect("exer.db")
#
# cr = db.cursor()
#
# cr.execute("create table if not exists users (user_id integer, name text)")
#
#
# # Inserting Data
#
# users_list = ["Yousef", "Ali", "Mohammed", "Khalied", "Mearna", "Sayed", "Sama", "Taha"]
#
# for key ,user in enumerate(users_list):
#
#     cr.execute(f"insert into users(user_id, name) values({key + 1}, '{user}')")
#
# # Fetch Data
#
# cr.execute("select * from users")
#
# # print(cr.fetchone())
# # print(cr.fetchone())
# # print(cr.fetchone())
# # print(cr.fetchone())
#
# # print(cr.fetchall())
#
# print(cr.fetchmany(2))# Select Just Two Items
#
# # Save All Changes
# db.commit()
#
# db.close()


# Exercize

# import sqlite3
#
#
# def get_all_data():
#
#     try:
#
#         # connect to database
#         db = sqlite3.connect("exer.db")
#
#         # print Success Massage
#         print("Conncted To Data Base Successffully")
#
#         # Setting Up The Courser
#         cr = db.cursor()
#
#     # Fetch data From Databace
#         cr.execute("select * from users")
#
#         # Assaing Data From Variable
#         result = cr.fetchall()
#
#         print(f"Database Has {len(result)} Rows")
#
#         # Printing Massage
#         print("Show Data: ")
#
#         # Loop On Result
#         for row in result:
#
#             print(f"UserId => {row[0]}, ", end=" ")
#
#             print(f"UserName Is: {row[1]}")
#
#     except sqlite3.Error as er:
#
#         print(f"Erorr Reading Data {er}")
#
#
#     finally:
#
#            if (db):
#
#                db.close()
#
#                print("Connection To Database Is Closed")
#
# get_all_data()


# update & Delete

# import sqlite3
#
# dp = sqlite3.connect("exer.db")
#
# cr = dp.cursor()
#
# cr.execute("update users set name = 'Gamal' where user_id = 4")# Number 4 Will Change
#
# cr.execute("delete from users where user_id = 4")# Number 4 Will delete
#
# cr.execute("select * from users")
#
# print(cr.fetchall())
#
# dp.commit()
#
# dp.close()

# ------- -------- ------ ------- ----- ------ ----- ------- ----- ----- ---- ----- -----------

# # Random Serial Numbers
# import string
# import random
#
# def make_serial(count):
#
#     all_char = string.ascii_letters + string.digits
#
#     print(all_char)# => abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
#
#     chars_count = len(all_char)
#
#     print(chars_count)# => 62
#
#     serial_List = []
#
#     while count > 0:
#
#         random_Number = random.randint(0, chars_count - 1)
#
#         random_Charcter = all_char[random_Number]
#
#         serial_List.append(random_Charcter)
#
#         count -= 1
#
#     print("".join(serial_List))# => KfUe1WP3V2orzMywCg8GKXGLcpe2MW
#
# make_serial(30)

# ------- -------- ------ ------- ----- ------ ----- ------- ----- ----- ---- ----- -----------


# Flask











print("hello")