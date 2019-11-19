n=int(input("enter the number of students"))
print(n)
for i in range(0,n):
	print("name")
	a=str(input())
	print("mark1:")
	mark1=int(input())
	
	print("mark2:")
	mark2=int(input())
	
	print("mark3:")
	mark3=int(input())
	total=0
	total=mark1+mark2+mark3
	average=total/3
	percentage=float((average/100)*100)
	print(total)
	print(average)
	print(percentage)
	print(i)
if(percentage>=60 and percentage<=70):
	print("college c")
elif(percentage>70 and percentage<=80):
	print("college b")
elif(percentage>80 and percentage<=90):
	print("college a")
elif(percentage>90):
	print("iit")