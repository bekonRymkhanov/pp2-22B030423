def guess(number):
    name=input("Hello! What is your name?\n")
    print('')
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    i=0
    while True:
        Guessed=int(input())
        print('')
        if Guessed==number:
            print(f"Good job, {name}! You guessed my number in {i} guesses")
            break
        elif Guessed>=number:
            print("Your guess is too hight.")
            i+=1
        elif Guessed<=number:
            print("Your guess is too low.")
            i+=1
        print("Take a guess.")
guess(13)
