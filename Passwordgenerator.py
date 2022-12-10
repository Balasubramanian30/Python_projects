import random
passwordlen = int(input("Enter the length of the password : "))
b = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
v = "".join(random.sample(b,passwordlen))
print(v)