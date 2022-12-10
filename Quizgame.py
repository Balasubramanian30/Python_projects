def checkguess(guess,answer):
    global  score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3 :
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sry wrong ans, try again")
                attempt = attempt + 1
        if attempt == 3:
            print("The crt ans is ", answer)
score = 0
print("Guess the animal")
guess1 = input("WHIch bear lives in north pole ?")
checkguess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
checkguess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
checkguess(guess3, "Blue Whale")
print("Your Score is "+ str(score))
