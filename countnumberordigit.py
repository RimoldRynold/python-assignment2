a=input("enter a sentence")
b=c=0
for i in a:
	if i.isdigit():
		b=b+1
	elif i.isalpha():
		c=c+1
	pass
print("digit is  ",b)
print("alphabet is  ",c)