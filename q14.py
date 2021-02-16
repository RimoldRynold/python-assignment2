l=[]

for i in range(1,31):
    l.append(i**2)
print("squares of 1st 5 and last 5 elements")
print(l[:5]+l[-5:])