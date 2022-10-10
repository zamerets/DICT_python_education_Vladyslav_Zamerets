print("My name is Anton")
print("Mt birth year is 2022")
user_name = input("Please, remind me your name: ")
print("What a great name you have, " + user_name + "!")
print("Let me guess your age :) ")
print("Please, enter reminder of your age by 3, 5, 7: ")
remainder3 = input()
remainder5 = input()
remainder7 = input()
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")


