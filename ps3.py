
# print list
f1 = input("Enter fruit number 1")
f2 = input("Enter fruit number 2")
f3 = input("Enter fruit number 3")
f4 = input("Enter fruit number 4")
f5 = input("Enter fruit number 5")
f6 = input("Enter fruit number 6")
f7 = input("Enter fruit number 7")

myFruitList=[f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)

 
# Program to write marks and diaplay in sorted manner


m1 = int(input ("Enter marks of student number 1 : "))
m2 = int(input ("Enter marks of student number 2 : "))
m3 = int(input ("Enter marks of student number 3 : "))
m4 = int(input ("Enter marks of student number 4 : "))
m5 = int(input ("Enter marks of student number 5 : "))
m6 = int(input ("Enter marks of student number 6 : "))
m7 = int(input ("Enter marks of student number 7 : "))
myList =[m1 ,m2,m3,m4,m5,m6,m7] 
myList.sort()
print(myList)


# calculate total percentage of student  
sub1 =int( input ("Enter marks of subject 1\n"))
sub2 =int( input ("Enter marks of subject 2\n"))
sub3 =int( input ("Enter marks of subject 3\n"))
sub4 =int( input ("Enter marks of subject 4\n"))
sub5 =int( input ("Enter marks of subject 5\n"))
sub6 =int( input ("Enter marks of subject 6\n"))
sub7 =int( input ("Enter marks of subject 7\n"))
sub8 =int( input ("Enter marks of subject 8\n"))

sum = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 +sub7 + sub8 )
totalmarks=sum
print("Recieved" , totalmarks , "out of 800")
percentage = (totalmarks/800)*100
print(percentage)