
print("Hi, welcome!\nTo inquiry your balance please press 1\nTo withdraw please press 2\nTo deposit money into account please press 3")


credit = 10000
while True:
    print("Please choose an action:")
    
    action = int(input())
    
    if action == 1:
        print("Credit Amount:", credit)  
        
    elif action == 2:
        print("Enter the amount you would like to withdraw from your account:")
        withdraw = int(input())
        credit = credit - withdraw
        print("New balance: ",credit)
        
    elif action == 3:
        print("Enter the amount you would like to deposit into your account:")
        deposit = int(input())
        credit = credit + deposit
        print("New Balance: ",credit)
        
    else: 
        print("Invalid operation!")
    
    print("Do you want to make a new transaction?: (y/n)")
    new_operation = str(input())
    if new_operation == 'y':
        continue
    elif new_operation == 'n':
        print("Thank you, bye!")
        break

