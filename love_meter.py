
name1 = input("What is your name?:")
name2 = input("What is your lover's name?:")

sum = len(name1+name2)

if len(name1) > len(name2):
    sum = sum - 5
else: 
    sum = sum + 3


love = (sum * 52) / (100 * len(name2))

if love > 10: 
    love = 10
elif love < 10:
    love = round(love)
    
print("Love point for", name1, "and", name2,":", love)
