print("\n   {:=^150}   \n".format("  |   GUESSING GAME   |  "))

from random import randint

guesses = 1

difficulty = int(input("Before we continue, i need to know what difficulty do you want to play.\n"
                       "\n1) Easy"
                       "\n2) Medium"
                       "\n3) Hard"
                       "\nChoose your difficulty: "))

while str(difficulty) not in "123":
    difficulty = int(input("\nInvalid option!"
                           "\nPlease, choose between 1) Easy, 2) Medium or 3) Hard: "))

if difficulty == 1:
    print("\n\n\n{:=^90}\n\n".format("   GAME MODE EASY   "))
    computer = randint(0, 10)
    player = int(input("I will think of a number between 0 and 10.\n\n"
                       "Can you guess which number is it? "))
    while player != computer:
        if player > 10:
            print("I said 'between 0 and 10'. Come on, again.")
        if player > computer:
            if player == computer + 3:
                print("Oh, man... You're so close...")
            elif player == computer + 1:
                print("Hummm... Damn... You're really s close...")
            player = int(input("You missed... Try a lower number: "))
        if player < computer:
            if player == computer - 3:
                print("Oh, man... You're so close...")
            elif player == computer - 1:
                print("Hummm... Damn... You're really s close...")
            player = int(input("You missed... Try a higher number: "))
        guesses += 1

if difficulty == 2:
    print("\n\n\n{:=^90}\n\n".format("   GAME MODE MEDIUM   "))
    computer = randint(0, 15)
    player = int(input("Well, i'll think of a number between 0 and 15. Try to guess which number is it.\n\n"
                       "You're guess: "))
    while player != computer:
        if player > 15:
            print('Oh, man... i said a number between 0 and 15. Try something like that.')
        if player < computer:
            if player == computer - 3:
                print("You're so close...")
            player = int(input("Wrong... Try again with a higher number: "))
        if player > computer:
            if player == computer + 3:
                print("You're so close...")
            player = int(input("Wrong... Try again with a lower number: "))
        guesses += 1

if difficulty == 3:
    print("\n\n\n{:=^90}\n\n".format("   GAME MODE HARD   "))
    computer = randint(0, 20)
    player = int(input("Well, i thought of a number between 0 and 20.\n\n"
                       "What's your guess? "))
    while player != computer:
        if player > 20:
            print("Hellooo... Damn, bro... I said i thought a number between '0 and 20'!")
        player = int(input("Wrong! Try again: "))
        guesses += 1

print("\nCongratulations! You got it right in {} attempts.".format(guesses))

again = str(input("\nDo you wanna play again (Y/N)? ")).strip().upper().split()[0]

if again == "Y":
    print("Reload the game\n\n"
          "(Ctrl + F5)")
if again == "N":
    print("Well, it was a pleasure to play with you.\n\n"
          "Goodbye... See you later...")
