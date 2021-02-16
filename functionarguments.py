# def print_data( mylist ):
#    #"This changes a passed list into this function"
#    mylist.append([1,2,3,4])
#    print("Values inside the function: ", mylist)

# # Now you can call function
# mylist = [10,20,30]
# print_data( mylist )
# print("Values outside the function: ", mylist)




#type of arguments



#1 Default Arguments



# def func(id,name="spectrum"):
# 	print("ID",id)
# 	print("NAME",name)
# 	return
# func(10)





# def func(name,msge="how are you"):
# 	print("hello",name+","+msge)

# func("rimold") 




#2 required argument


# def func(a):
# 	print("hai",a)
# 	return
# func("rimold")



# 3 keyword argument


# def func(a,b,c,d):
# 	print("this",a)
# 	print("an",b)
# 	print("program",c)
# 	print("keyword",d)
# 	return

# func(a="is",b="example",c="for",d="argument")




# 4 variable length argument

# 		1 postional or non keyword argument
# 		2 keyword argument
# 	1 postional or non keyword argument


# def func(*a):
# 	for b in a:
# 		print(b)
# func(1,2,3,4,5,6)

		# 2 keyword argument

# def myFun(**kwargs):  
#         d={}
#         for key,value in kwargs.items(): 
#                 d[key]=value
#         print(d)
  
# # Driver code 

# myFun(first ='Geeks', mid ='for', last='Geeks')  





def func(a):
	print("hai",a)
	return
func("rimold")



@func
def ordinary():
    print("I am ordinary")
ordinary()


	