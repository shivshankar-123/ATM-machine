print("welcome to ABC bank")
pin=1011
chances=3
balance=50000
while chances !=0:
    user_pin=int(input("enter the four digit number:"))
    if user_pin!=pin:
        chances-=1
        print("wrong pin number")
        print(f"you have {chances} chances left")
    else:
        user_choice=input("B: balance,D:deposit,W:withdraw")
        if user_choice=="B":
          print(f"your total balance is Rs.{balance}")
        if user_choice=="D":
          deposit_user=int(input("Enter the deposited amount:"))
          total_balance= deposit_user+balance
          print(f"you have deposited Rs.{deposit_user}")
          print(f"your total balance is Rs.{total_balance}")
        if user_choice=="W":
          withdraw_user=int(input("Enter the withdraw  amount:"))
          balance=total_balance-withdraw_user
          print(f"you have withdraw Rs.{withdraw_user}")
          print(f"your total balance is Rs.{balance}")
    user_exit=input("Would you like to exit? yes/no")
    if user_exit=="yes":
        print("Thank you for using ABC bank")
        break
    else:
        continue

