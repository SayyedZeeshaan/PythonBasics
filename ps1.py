
# Basics of python
a = 34
b = 5 
print("The sum of a and b is" , a + b )

c = 45
d = 15 
print("The remainder when c is divided by d is " , c%d)




# average of two numbers 
A = input("Enter first number")
B = input("Enter second number")
A = int(A)
B = int(B)
avg = (A+B)/2
print(avg)

# Square of a number
D =int(input("Enter a number to get its Square "))
Sq = D * D
print(Sq)

# print type of variable

name = 'Zeeshaan'
surname = "Sayyed"
print(type(name))
age = 24
print(type(age))
print ( "My name is", name, "and my age is ", age)


# Concatination

fullname = surname + name
print(fullname)

# string slicing

print(name[2])  #char at index 2 

print (name[0:7])  
print( name [0:])
print (name[-4:-1])

print (name[1:8:2])  #Skiping character

print (len(fullname))  #length of string


