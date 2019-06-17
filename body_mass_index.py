
height  = int(input("Please enter height(cm): "))
weight = float(input("Please enter weight: "))
bmi = weight/((height/100)**2)

print("Body mass index:", round(bmi, 2))

if bmi <= 18.5:
    print("Underweight")
    print("To reach normal weight, you should gain {} kg.".format(round(18.5*((height/100)**2)-weight,2)))
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
    print("To reach normal weight, you should lose {} kg.".format(round(weight-24.9*((height/100)**2)),2))
elif bmi <= 39.9:
    print("Obese")
    print("To reach normal weight, you should lose {} kg.".format(round(weight-24.9*((height/100)**2)),2))
else: 
    print("Over Obese")
    print("To reach normal weight, you should lose {} kg.".format(round(weight-24.9*((height/100)**2)),2))
