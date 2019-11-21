=int(input("Enter number"))
b=a
rev=0
while(a>0):
    c=a%10
    a=a//10
    rev=rev*10+c
if(b==rev):
    print("The number is a palindrome")
else:
    print("The number not a palindrome")
