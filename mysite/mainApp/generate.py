import random

def random_password():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 22 #27

    password =''
    for i in range(length):
        password += random.choice(chars)
    return password
