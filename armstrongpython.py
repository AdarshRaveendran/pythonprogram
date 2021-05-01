N=int(input("Enter a Number"))#input from the user
for num in range(0,N):#lower limit 0 to upper limit N
  temp=num
  sum=0#initialization 
  while temp>0:
      rem=temp%10# find sum and cube of rem
      sum=sum+rem*rem*rem
      temp=temp//10
      if sum==num:# condition check
           print (num)
