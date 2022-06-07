print('\n \n')
import random
x=input('Enter Name: ')
print('\n\n\n                 ',x,'\n          Welcome To Our Number Guessing Game !!! \n\n')
y=int(input('Press 1 to start the Game!'))
print()

while True:
    print('**************************************************************************************************************************************')
    if (y==1):
        a=int(input('\nChoose level : \n 1.Easy \n 2.Medium \n 3.Hard \n'))
        if (a==1):
            b=random.randint(1,10)
            print()
            print(x,'Computer has choosen its number , Now its your turn !!')
            c=int(input('Enter a number between 1 to 10: '))
            print()
            if (c==b):
                print('Wohoo , Congrats',x,'You guessed it right !!!\n')
            else:
                print('Oops , You guessed it wrong',x,'!')
                print('The number was ',b)
            d=input('Do you want to play again? (Y/N): ')
            if (d in ['Y','y']):
                continue
            else:
                print('\n\n\nThis game was developed by : Aniket Kumar Paul \n \n HOPE YOU LIKED IT \n Press Enter to Quit\n')
                input()
                exit()
        elif (a==2):
            b=random.randint(1,50)
            print('\n',x,'Computer has choosen its number , Now its your turn !!\n')
            c=int(input('Enter a number between 1 to 50: '))
            print()
            if (c==b):
                print('Wohoo , Congrats',x,'You guessed it right !!!\n')
            else:
                print('Oops , You guessed it wrong',x,'!\n')
                print('The number was ',b,'\n')
            d=input('Do you want to play again? (Y/N): ')
            print()
            if (d in ['Y','y']):
                continue
            else:
                print('\n\n\nThis game was developed by : Aniket Kumar Paul \n \n HOPE YOU LIKED IT \n Press Enter to Quit\n')
                input()
                exit()
        elif (a==3):
            b=random.randint(1,100)
            print('\n',x,'Computer has choosen its number , Now its your turn !!\n')
            c=int(input('Enter a number between 1 to 100: '))
            print()
            if (c==b):
                print('Wohoo , Congrats',x,'You guessed it right !!!\n')
            else:
                print('Oops , You guessed it wrong',x,'!\n')
                print('The number was ',b,'\n')
            d=input('Do you want to play again? (Y/N): ')
            print()
            if (d in ['Y','y']):
                continue
            else:
                print('\n\n\nThis game was developed by : Aniket Kumar Paul \n \n HOPE YOU LIKED IT \n Press Enter to Quit\n')
                input()
                exit()
        else:
            print('\nInvalid Option\n')
            continue
            
            
