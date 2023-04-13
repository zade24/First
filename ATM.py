while True:
    balance = 10000
    print("   ATM    ")
    print("""
    1)       Balance
    2)       Withdraw
    3)       Deposit
    4)       Quit
    """)

    try:
        option = int(input("Enter option: "))
    except Exception as e:
        print("Error:",e)
        print("Enter 1,2,3 or 4 only")

        continue

    if option == 1:
        print("Balance R",balance)
    if option == 2:
        print("Balance R",balance)
        withdraw = float(input("Enter Withdraw amount R "))
        if withdraw >0:
            forewardbalance = (balance - withdraw)
            print("Foreward Balance R",forewardbalance)
        elif withdraw > balance:
            print("No Funds in account")
        else:
            print("None Withdraw made")

    if option == 3:
        print("balance R ",balance)

        deposit = float(input("Enter deposite amount R"))
        if deposit > 0:
            forewardbalance = (balance + deposit)
            print("Forewardbalance R ",forewardbalance)
        
        else:
            print("None deposit made")
            
    if option == 4:
        exit()