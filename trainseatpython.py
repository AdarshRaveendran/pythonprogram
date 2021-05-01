
N=int(input("Enter seat Number"))#input from the user
if N>0 and N<73:#seats less than 73
 if N%8 == 1 or N%8 == 4:
        print ("L")# lower seat
 elif N%8 == 2 or N%8 == 5:
        print("M")# middle seat
 elif N%8==3 or N%8==6:
        print("U")#upper seat
 elif N%8==7:
        print("SL")#side lower seat
 else:
        print("SU")#side upper seat
else:
    print("invalid seat number")
    
