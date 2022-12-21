from decouple import config
from random import choice
my_money = config("MY_MONEY", cast=int)
list_numbers = [i for i in range(1, 31)]
client_earnings = 0
def casino_game():
    while True:
        global client_earnings
        global my_money
        print(f'Your balance: {my_money}$')
        if my_money <= 0:
            print("You don't have enough money\nGame over!")
            break
        quetion = input("Do you wanna play?(yes/no): ")
        if quetion.lower() == "yes":
            bet = int(input("Enter your bet: "))
            if bet > my_money:
                raise ValueError(f"You don't have enough money, your balance:{my_money}$")
            win_number = choice(list_numbers)
            client_choice = input(f"Choose your lucky number from {list_numbers[0]} to {list_numbers[-1]}: ")
            if int(client_choice) > list_numbers[-1]:
                raise ValueError("You choose number out of range, please enter correct number!")
            if int(win_number) == int(client_choice):
                my_money = my_money + (bet * 2)
                client_earnings = client_earnings + bet * 2
            else:
                my_money -= bet
                print(f'Your number: {client_choice}, did not match the winning number: {win_number} ')
        elif quetion.lower() != 'yes' and quetion.lower() != 'no':
            raise ValueError('please enter only yes or no!')
        else:
            print(f"You won {client_earnings}$ and your balance now {my_money}$")
            break

start_game = casino_game()