# name = 'Elzero'

# # Needed Output
# print(name[1:4])# "lze"
# print(name[::2])# "Ezr"
# print(name[-2::-2])# "rzE"

# name = "#@#@Elzero#@#@"

# # Needed Output
# print(name.strip("#@"))# Elzero

# num1 = "9"
# num2 = "15"
# num3 = "130"
# num4 = "950"
# num5 = "1500"

# # Needed Output
# print(num1.zfill(4))# 0009
# print(num2.zfill(4))# 0015
# print(num3.zfill(4))# 0130
# print(num4.zfill(4))# 0950
# print(num5.zfill(4))# 1500

# msg = "I Love Python And Although Love Elzero Web School"

# # Needed Output
# print(msg.count("Love"))# 2

# x = 1+2j

# print(x.real)# Print Imaginary Part Here
# print(x.imag)# Print Real Part Here

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# print(friends[0])# "Osama" => Method One
# print(friends.pop(0))# "Osama" => Method Two
# print(friends[-1])# "Mahmoud" => Method One
# print(friends.pop(-1))# "Mahmoud" => Method Two

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# print(friends[::2])# "Osama", "Sayed", "Mahmoud"
# print(friends[1::2])# "Ahmed", "Ali"

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# print(friends[1:-1])# "Ahmed", "Sayed", "Ali",
# print(friends[3:])# "Ali", "Mahmoud"

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
# friends[-2:] = ["Elzero", "Elzero"]
# print(friends)

# friends = ["Osama", "Ahmed", "Sayed"]
# friends.insert(0, "Nasser")
# friends.extend(["Salem"])
# # Needed Output
# print(friends)# ["Nasser", "Osama", "Ahmed", "Sayed"]
# print()# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]


# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# # Needed Output
# friends[0:2] = []
# friends.pop()
# print(friends)# ["Ahmed", "Sayed", "Salem"]
# # ["Ahmed", "Sayed"]


# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]

# # Needed Output
# friends.extend(employees)
# print(friends + school)# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]


# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# # Needed Output
# friends.sort()
# friends.sort(reverse=True)
# print(friends)# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# print(friends)# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']


# # Needed Output
# x = "Osama",
# # "Osama"
# print(type(x))# <class 'tuple'>


# friends = ("Osama", "Ahmed", "Sayed")

# x = list(friends)
# x[0] = "Elzero"
# friends = tuple(x)
# print(friends)
# # Needed Output
# # ("Elzero", "Ahmed", "Sayed")
# # <class 'tuple'>
# # 3 Elements


# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# x = nums + letters
# print(nums + letters)
# print(len(x))
# # Needed Output
# # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# # 6 Elements


# my_tuple = (1, 2, 3, 4)

# # Needed Output
# a, b, _, c = my_tuple
# print(a)# 1
# print(b)# 2
# print(c)# 4


# my_list = [1, 2, 3, 3, 4, 5, 1]
# # Needed Output
# unique_list = list(set(my_list))
# print(unique_list)# 1, 2, 3, 4, 5
# print(type(unique_list))# <class 'list'>
# print(unique_list[:-1])# 1, 2, 3, 4


# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# # Needed Output

# print(nums | letters)# {1, 2, 3, "A", "B", "C"}
# nums.update(letters)
# print(nums)# {1, 2, 3, "A", "B", "C"}


# my_set = {1, 2, 3}
# # Needed Output
# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update("A", "B")
# print(my_set)
# my_set.discard("C")
# print(my_set)
# # {1, 2, 3}
# # set()
# # {"A", "B"}

# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# # Needed Output
# print(set_one.issubset(set_two))
# # True


# print(bool("a"))# => True
# print(bool(2))# => True
# print(bool([100, "a"]))# => True
# print(bool(True))# => True

# print("c_" * 40)

# print(bool(""))# => False
# print(bool([]))# => False
# print(bool(0))# => False
# print(bool(False))# => False


# html = 80
# css = 60
# javascript = 70

# # Needed Output  =>  # True

# print(html and css and javascript > 50)# => True


# num_one = 10
# num_two = 20
# num = 20

# # Needed Output => True False

# print(num > num_one or num > num_one)

# print(num > num_one and num > num_one)


# num_one = 10
# num_two = 20

# result = num_one + num_two

# print(result)# 30

# print(result ** 3)# 27000

# print(result ** 3 % 26000)# 1000

# print(result ** 3 % 26000 / 5)# 200.0

# convert = str(result ** 3 % 26000 / 5)

# print(type(convert))


# name = input("Enter Your Name: ").strip().capitalize()

# print(f"Hello {name}, Happy To See You Here")


# age = int(input("Enter Your age: "))


# if age < 16:
#     print(f"Hello Your Age Is Under {age}, Some Articles Is Not Suitable For You")

# else:
#     print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


# frist_name = input("Enter a Frist Name: ").strip().capitalize()

# secound_name = input("Enter a Secound Name: ").strip().capitalize()

# print(f"Hello {frist_name} {secound_name:.1s}")


# email = input("Enter Your Email: ").strip().lower()

# userName = email[:email.index("@")]

# domain = email[email.index("@") + 1: email.index("."):]

# top_Level_Domain = email[email.index(".") + 1:]

# print(f"Your Username Is {userName} Your Domain Is {domain} Your Top Level Domain Is {top_Level_Domain}")


# num1 = int(input("Enter A Frist Number: ").strip().capitalize())
# operation = input("Enter The Operation(%, /, *, -, +): ").strip().capitalize()
# num2 = int(input("Enter A Second Number: ").strip().capitalize())

# if operation == "+":
#     print(int(num1 + num2))

# elif operation == "-":
#     print(int(num1 - num2))

# elif operation == "*":
#     print(int(num1 * num2))

# elif operation == "/":
#     print(int(num1 / num2))

# elif operation == "%":
#     print(int(num1 % num2))

# else:
#     print("Wrong, The Operation or Number Is Not Exist.")


# age = int(input("Enter Your Age: ").strip().capitalize())

# print(f"{'the Website Not Suitable For You' if age < 16 else 'The Website Suitable For You'}")


# age = int(input("Enter Your Age: "))

# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# if age < 10 or age > 99:
#     print("Your Age Is Not Exist")

# else:
#  print(months)
#  print(weeks)
#  print(days)
#  print(hours)
#  print(minutes)
#  print(seconds)

# country = input("Enter Your Country: ").strip().capitalize()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30
# if country in countries:
#     print(f"Hello, Cuz You From {country} You Have Discount {discount}%")
#     print(f"Will Be Price Of Product is {price - 30}$")

# else:
#     print("You Not Have Any Discount")

# num = int(10)

# while num > 0:
#     if num == 0:
#         print("Number 0 Is Not Leager Than 0")

#     else:
#         sum = 0

#     num -= 1

#     if num == 6:

#       continue

#     print(num)

#     sum += 1

#     print(f"{sum}Number Printed Succssffully")


# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20]

# for x in myList:

#    if x == 6 or x == 8 or x == 12:
#        continue

#    print(x)

# print("All Numbers Printed")


# def calculate(num1, num2, operation):
#
#     operation = operation.lower()
#
#     if operation in ["a", "addtion"]:
#         print(num1 + num2)
#     elif operation in ["s", "subtract"]:
#         print(num1 - num2)
#     elif operation in ["m", "multiply"]:
#         print(num1 * num2)
#     else:
#         print("Wrong, The operation Is Not Exist")


# def addition(*addition):
#     sum = 0
#     for num in addition:
#
#         if num == 10:
#
#             continue
#
#         elif num == 5:
#
#             sum -= num
#
#         else:
#
#             num += 1

# def show_skills(name, *skills):
#
#     print(f"Hello {name} Your Skills Is: ")
#
#     for skill in skills:
#
#         print(skill)
#
# show_skills("yousef", "HTML", "CSS", "JS", "Python")


# def show_skills(name, *skills):
#
#     if len(skills) <= 0:
#
#         print(f"Hello {name} You Have No Skills To Show")
#     else:
#      print(f"Hello {name} Your Skills Is: ")
#
#      for skill in skills:
#
#         print(f"- {skill}")
# show_skills("yousef", "HTML", "CSS", "JS", "Python")

# def say_Hello(name= "Unknown", age= "Unknown", country= "Unknown"):
#
#     print(f"Hello {name} Your Age Is {age} And You Live In {country}")
#
# say_Hello()


# values = (0, 1, 2)
#
# if any(values):
#
#   my_var = 0
#
# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
#
# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
#
#   print("Good")
#
# else:
#
#   print("Bad")


# v = 40
#
# my_range = list(range(v))
#
# print(sum(my_range, v) + pow(v, v, v))  # 820

