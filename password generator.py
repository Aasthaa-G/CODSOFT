import random

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$%^&*()"

while 1:
    a = int(input("Enter username-"))
    password_len = int(12)
    password_count = int(input("How many passwords would you like:"))
    for x in range(0,password_count):
        print(x)
