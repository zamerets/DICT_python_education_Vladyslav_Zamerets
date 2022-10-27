import string
import random


friend_q = None
friends_list = {}
total_amount = None
divided = None
lucky_one = None


def lucky_one_check():
    global lucky_one
    global friend_q
    choice = input("Who is lucky? feature? Write Yes/No: ")
    if choice == "Yes":
        lucky_one = random.randint(0, int(friend_q))
        return lucky_one


def check_number(a):
    while int(a) <= 0:
        a = input("No one is joined for the party!")
        raise SystemExit(1)



def friend_input():
    global friend_q
    friend_q = int(input("Enter the number of friends joining (including you): "))
    if int(friend_q) <= 0:
        check_number(friend_q)
    i = 0
    while i < int(friend_q):
        name = input("Enter the name of a person: ")
        friends_list[name] = 0
        i += 1
    return friend_q
friend_input()


def total_amount_request():
    global total_amount
    total_amount = int(input("Enter the total amount: "))
    return total_amount
total_amount_request()


def dividing():
    global divided
    global total_amount
    global friend_q
    divided = total_amount / friend_q
    for i in friends_list:
        friends_list[i] = divided
dividing()


def luckyone():
    number = lucky_one_check()
    k = -1
    for i in friends_list:
        k += 1
        if k == number:
            friends_list[i] = 0
            print(i + " is lucky one! :) ")
luckyone()


print(friends_list)



