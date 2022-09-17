import datetime

username="abcd"
passowrd="vino"
pin=7668
chances=3
balance=40000
user_name=input("Enter user name:")
password=input("Enter password:")
if user_name=="abcd" and password=="vino":
    print("Login successfully")
    while chances!=0:
        user_pin=int(input("Ente user pin:"))
        if user_pin!=pin:
            chances=chances-1
            print("wrong pin")
            print(f"You are left with {chances} chance")
        else:   
            user_choice=input("Enter the option:") 
            print('''
            1.Balance
            2.Deposit
            3.Withdraw
            4.Bill
            ''')
            if user_choice=="balance":
                print(f"Your available balance is rs.{balance}")
            elif user_choice=="deposit":
                deposit=int(input("Enter the amount you want to deposit:"))    
                amount=balance+deposit
                print(f"You deposited an amount of rs.{deposit} and now your available balace is rs.{amount} ")
            elif user_choice=="withdraw":
                withdraw=int(input("Enter the amount you want to withdraw:"))
                print(f"You withdraw an amount of rs.{withdraw}")
                if withdraw>1000:
                    total=amount-withdraw
                    print(f"You withdraw an amount of rs.{withdraw} and now the balance is rs.{total}") 
                else:
                    print(f"You can't withdraw {withdraw} as you have to maintain minimum balance") 
            elif user_choice=="bill":
                date=datetime.datetime.now()
                print(f"Your available balance is {total} on {date}")
        user_exit=input("would u like to exit:")
        if user_exit=="yes":
            print("Thanks for using xyz bank")        
            break
        else:
            continue  


              
              



