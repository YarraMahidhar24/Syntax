def ac(x):
    print(f"your available balance is ${x:.2f}")
def deposit():
    x = float(input("deposit amount in : $"))
    if x>0:
        return x
    else:
        print("plz enter valid amount")
        return 0
def withdraw(x):
    y=float(input("withdraw amount in : $"))
    if x<y:
        print("in sufficient balance")
        print("plz enter valid amount that available in your account")
        return 0
    elif 0<=y<=x:
        return y
    else:
        print("plz enter valid amount")
        return 0
print("------WELCOME TO BANK------")
def main():
    balance=0
    your_in=True
    while your_in:
        print("please select your option")
        print("select 1 to check account balance")
        print("select 2 to DEPOSIT MONEY")
        print("select 3 to WITHDRAW MONEY")
        print("select 4 to TO EXIT")
        i=input("enter which serves you need :")
        if i=="1":
            ac(balance)
        elif i =="2":
            balance+=deposit()
        elif i =="3":
            balance=balance-withdraw(balance)
        elif i =="4":
            your_in = False
        else:
            print("Please give valid input")
    print("---HAVE A NICE DAY---")
    print("---------BYE---------")
if __name__ == '__main__':
    main()
