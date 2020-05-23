print("\n\033[1;7;30m   {:=^150}   \033[m\n".format("  |   O JOGO DA ADVINHAÇÃO (3.0)   |  "))

from random import randint

guesses = 1

difficulty = int(input("\033[30mBefore we continue, i need to know what difficulty do you want to play.\n\n\033[1;30m1) Easy\n2) Medium\n3) Hard\nChoose your difficulty:\033[m "))

while str(difficulty) not in "123":
    difficulty = int(input("\n\033[1;31mInvalid option!\n\033[1;30mPlease, choose between 1) Easy, 2) Medium or 3) Hard : \033[m"))

if difficulty == 1:
    print("\n\n\n\n\n\033[1;36m{:=^90}\033[m\n\n".format("   GAME MODE EASY   "))
    computer = randint(0, 10)
    player = int(input("\033[30mI will think of a number between 0 and 10.\n\n\033[1;30mCan you guess which number is it?\033[m "))
    while player != computer:
        if player > computer:
            if player == computer + 3:
                print("\033[30mOh, man... You're so close...\033[m")
            elif player == computer + 1:
                print("\033[30mHummm... Damn... You're really s close...\033[m")
            player = int(input("\033[1;31mYou missed...\033[m \033[33mTry a lower number:\033[m "))
        if player < computer:
            if player == computer - 3:
                print("\033[30mOh, man... You're so close...\033[m")
            elif player == computer - 1:
                print("\033[30mHummm... Damn... You're really s close...\033[m")
            player = int(input("\033[1;31mYou missed...\033[m \033[33mTry a higher number:\033[m "))
        guesses += 1

if difficulty == 2:
    print("\n\n\n\n\n\033[1;34m{:=^90}\033[m\n\n".format("   GAME MODE MEDIUM   "))
    computer = randint(0, 15)
    player = int(input("\n\033[30mWell, i'll think of a number between 0 and 15. Try to guess which number is it.\n\n\033[1;30mYou're guess:\033[m "))
    while player != computer:
        if player > 15:
            print('\033[30mOh, man... i said a number between 0 and 15. Try something like that.\033[m')
        if player < computer:
            if player == computer - 3:
                print("\033[30mYou're so close...\033[m")
            player = int(input("\033[1;31mWrong...\033[m \033[33mTry again with a higher number:\033[m "))
        if player > computer:
            if player == computer + 3:
                print("\033[30mYou're so close...\033[m")
            player = int(input("\033[1;31mWrong...\033[m \033[33mTry again with a lower number:\033[m "))
        guesses += 1

if difficulty == 3:
    print("\n\n\n\n\n\033[1;35m{:=^90}\033[m\n\n".format("   GAME MODE HARD   "))
    computer = randint(0, 20)
    player = int(input("\n\033[30mWell, i thought of a number between 0 and 20.\n\n\033[1;30mWhat's your guess?\033[m "))
    while player != computer:
        if player > 20:
            print("\033[30mHellooo... Damn, bro... I said i thought a number between '0 and 20'!\033[m")
        player = int(input("\033[1;31mWrong!\033[m \033[33mTry again:\033[m "))
        guesses += 1

print("\n\033[1;32mCongratulations! You got it right in {} attempts.\033[m".format(guesses))

again = str(input("\n\033[1;30mDo you wanna play again (Y/N) ?\033[m ")).strip().upper().split()[0]

if again == "Y":
    print("\033[30mReload the game\n\n\033[1;30m(Ctrl + F5)\033[m")
if again == "N":
    print("\033[30mWell, it was a pleasure to play with you.\n\n\033[1;30mGoodbye... See you later...\033[m")
