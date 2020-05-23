print("\n\033[1;7;30m   {:=^150}   \033[m\n".format("   |   MAIN MENU (2.0)   |   "))

from time import sleep

n1 = int(input('\033[1;30mEnter the 1th value:\033[m '))
n2 = int(input('\033[1;30mEnter the 2th value:\033[m '))

exit_program = False

while not exit_program:

    sleep(0.5), print('\n\n\n\033[1;30m{}\033[m   \033[1;31m>>>\033[m    \033[1;30mMain  Menu\033[m    \033[1;31m<<<\033[m   \033[1;30m{}\033[m'.format('=-=' * 10, '=-=' * 10))

    print('\033[1;32m[1] Sum\033[m'
          '\n\033[1;35m[2] Multiply\033[m'
          '\n\033[1;36m[3] Check the highest number\033[m'
          '\n\033[1;33m[4] Enter new values\033[m'
          '\n\033[1;31m[5] Exit program\033[m')

    print('{}'.format('\033[1;30m=-=\033[m' * 30)), sleep(0.5)

    option = int(input('\n\033[30mEnter the number corresponding to the action you want.\033[m \033[1;30mWhat do you want to do:\033[m '))

    if option == 1:
        print('\n\033[32mYou chose to sum the two values.\033[m'), sleep(0.75)
        print('\033[32mThe result of {} + {} is equal to {}.\033[m'.format(n1, n2, n1 + n2)), sleep(0.25)

    elif option == 2:
        print('\n\033[35mYou chose to multiply the two values.'), sleep(0.75)
        print('\033[35mThe result of {} x {} is equal to {}.\033[m'.format(n1, n2, n1 * n2)), sleep(0.25)

    elif option == 3:
        print('\n\033[36mYou chose to check the highest value.\033[m'), sleep(0.75)
        if n1 == n2:
            print('\033[1;31mError!\033[m \033[36mThe numbers you entered are the same.\033[m'), sleep(0.25)
        else:
            high = n1
            if n2 > n1:
                high = n2
            print('\033[36mBetween {} and {}, the highest is {}.\033[m'.format(n1, n2, high)), sleep(0.25)

    elif option == 4:
        print('\n\033[33mYou chose to enter new two values. Please, insert them below.\033[m'), sleep(0.75)
        n1 = int(input('\033[1;30mEnter the new 1th value:\033[m ')), sleep(0.25)
        n2 = int(input('\033[1;30mEnter the new 2th value:\033[m ')), sleep(0.25)

    elif option == 5:
        print('\n\033[31mYou chose to shut down the program.\033[m'), sleep(1)
        exit_program = True

    else:
        print('\033[1;31mInvalid option!\033[m \033[1;30mPlease, try again...\033[m ')

print('\n\033[30mShutting down... Please, wait...\033[m'), sleep(3)
print('\n\n\n\n\n{}\n{:^100}\n{}'.format('==' * 45, '\033[1;30mGoodbye...  See you later...\033[m', '==' * 45))
