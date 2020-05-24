print("\n   {:=^150}   \n".format("   |   MAIN MENU   |   "))

from time import sleep

n1 = int(input('Enter the 1th value: '))
n2 = int(input('Enter the 2th value: '))

exit_program = False

while not exit_program:

    sleep(0.5), print('\n\n{}   >>>    Main  Menu    <<<   {}'.format('=-=' * 10, '=-=' * 10))

    print('[1] Sum\n'
          '[2] Multiply\n'
          '[3] Check the highest number\n'
          '[4] Enter new values\n'
          '[5] Exit program')

    print('{}'.format('=-=' * 30)), sleep(0.5)

    option = int(input('\nEnter the number corresponding to the action you want. What do you want to do: '))

    if option == 1:
        print('\nYou chose to sum the two values.'), sleep(0.75)
        print('The result of {} + {} is equal to {}.'.format(n1, n2, n1 + n2)), sleep(0.25)

    elif option == 2:
        print('\nYou chose to multiply the two values.'), sleep(0.75)
        print('The result of {} x {} is equal to {}.'.format(n1, n2, n1 * n2)), sleep(0.25)

    elif option == 3:
        print('\nYou chose to check the highest value.'), sleep(0.75)
        if n1 == n2:
            print('Error! The numbers you entered are the same.'), sleep(0.25)
        else:
            high = n1
            if n2 > n1:
                high = n2
            print('Between {} and {}, the highest is {}.'.format(n1, n2, high)), sleep(0.25)

    elif option == 4:
        print('\nYou chose to enter new two values. Please, insert them below.'), sleep(0.75)
        n1 = int(input('Enter the new 1th value: '))
        sleep(0.25)
        n2 = int(input('Enter the new 2th value: '))
        sleep(0.25)

    elif option == 5:
        print('\nYou choose to shut down the program.'), sleep(1)
        exit_program = True

    else:
        print('Invalid option! Please, try again... ')

print('\nShutting down... Please, wait...'), sleep(3)
print('\n\n\n{}\n{:^90}\n{}'.format('==' * 45, 'Goodbye...  See you later...', '==' * 45))
