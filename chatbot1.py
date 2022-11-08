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
print("Now I will prove to you that I can count to any number you want.")
entered_number = input("Enter a number:")
counter = 1
while counter - 1 < int(entered_number):
    print(str(counter)+"!")
    counter = counter + 1
print("Take a quiz")
correct = False
while not correct:
    print("How many letters does the english alphabet contains")
    print("1) 26")
    print("2) 27")
    print("3) 28")
    print("4) 29")
    user_input = input("Enter your answer: ")
    if user_input == "1":
        correct = True
        print("You're right :) !!!")
    else:
        print("Your answer is incorrect! ")
print("Completed!")