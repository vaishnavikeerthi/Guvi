a=int(input("enter starting km:"))
b=int(input("enter ending km:"))
c=int(input())
d=b-a
if(d>5):
     d=d-5
     fare=(d*8)+100
     print(fare)
     if(c==1):
     	fare1=fare+(0.25*fare)
     	print(fare1)
else:
     fare2=100
     print(fare2)