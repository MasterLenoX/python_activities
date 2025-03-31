from datetime import datetime

print("testing number 1")
print(50)

print ("Hello ZAWARUDO")

birthdate = datetime(1997, 9, 2)
today = datetime.today()

fname = "Renokusu"
fage = today.year - birthdate.year

print("Konnichiwa!!! " + fname + "-desu")
print("I'm a graduate student and I'm " + str(fage) + " years old")

# fname = input("What's your name? ")
# print("Hello, " , fname)

#if statement

if (5 > 2):
  print ("Five is greater than Two")

# Nested If Else Statement

coffee_drinker = True

if coffee_drinker:
    print("LET's DRINK COFFEE")
elif coffee_drinker == True:
    print("TARA MILK TEA")
else:
    print("YAWA")

