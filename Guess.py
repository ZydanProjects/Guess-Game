#the purpose of this code is to create a simple of application of guessing game
def guess():
    count = 0

    while count < 3:
        user = int(input('Enter a number to guess: '))
       
        if user == 13:
            print('Your guess is correct. Good Job :D')
            break
        elif user < 13:
            print('Your number is low. Try again :D')
        elif user > 13:
            print('Your number is high. Try again :D')
        else:
            pass
       
        count +=1

    print('Good luck next time. ')
