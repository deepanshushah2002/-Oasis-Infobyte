Weight = float(input("Enter a Weight: "))
Height = float(input("Enter a Height in Meter: "))

x = Weight / (Height**2)
print(x)
if x < 18.5:
    print("Under Weight")
elif x >= 18.5 and x <= 24.9:
    print("Healthy")
elif x >= 25 and x <= 29.9:
    print("Over Weight")
elif x >= 30 and x <= 39.9:
    print("Obese")
else:
    print("Severely Obese")
