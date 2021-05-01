
a=int(input("Enter day"))#input from the user
b=int(input("enter month"))
c=int(input("enter year"))
if a<=31 and b<=12 and (c<=2021):#days less than 32,month less than 13,years lessthan 2021
    print("valid date")
else:
    print("Invalid date")

