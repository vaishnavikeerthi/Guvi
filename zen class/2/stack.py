list1=["apple","banana"]
def push(a):
    list1.append(a)
    print(list1)
def pop():
    return list1.pop()
push("orange")
print(list1)
