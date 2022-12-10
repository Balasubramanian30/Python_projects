import random
minvalue =1
maxvalue = 10
roll_again = "Yes"
while roll_again == "Yes" or roll_again == "Y":
    print("Rolling the dices....")
    print("The values are : ")
    print(random.randint(minvalue, maxvalue))
    print(random.randint(minvalue, maxvalue))
    roll_again = input("Roll the dice again ")
