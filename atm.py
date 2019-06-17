
print("Hi, welcome!\nTo inquiry your balance please press 1\nTo withdraw please press 2\nTo deposit money into account please press 3")


credit = 10000
while True:
    action = int(input("Please choose an action:"))
    
    if action == 1:
        print("Credit Amount:", credit)  
        
    elif action == 2:
        withdraw = int(input("Enter the amount you would like to withdraw from your account:"))
        credit = credit - withdraw
        print("New balance: ",credit)
        
    elif action == 3:
        deposit = int(input("Enter the amount you would like to deposit into your account:"))
        credit = credit + deposit
        print("New Balance: ",credit)
        
    else: 
        print("Invalid operation!")

    new_operation = str(input("Do you want to make a new transaction?: (y/n)"))
    if new_operation == 'y':
        continue
    elif new_operation == 'n':
        print("Thank you, bye!")
        break

