a=int(input("enter a number:"))
sum=0
temp=a
while temp > 0:
          b=temp%10
          sum=sum+b**3
          temp=temp//10
if a==sum:
    print(a,"is a armstrong number")
else:
    print(a,"is not a armstrong number")
          
