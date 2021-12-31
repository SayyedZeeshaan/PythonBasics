
a = 1
if(a>3):
    print("The value of a is greater than 3")
elif(a>7):
    print("The value of a is greater than 7")
else:
    print("The value is not greater than 3 or 7")


# take input from user and use it 

a= int(input("Enter your age"))
if (a>18):
    print("You are a fresher")
if (a>25):
    print("You are having some experience")
if(a>35):
    print("You are very experienced")

# Take input of 4 numbers and print the greatest number

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2=num2
else:
    f2 = num3
if (f1>f2):
    print(f1, "Is the greatest of all numbers ")
else:
    print(f2 , "Is the greatest of all numbers")
    
    
# to check wether a student is pass or fail

sub1=int(input("Enter marks in subject 1\n"))
sub2=int(input("Enter marks in subject 2\n"))
sub3=int(input("Enter marks in subject 3\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33 marks in one subject")

elif(sub1+sub2+sub3)/3 <40 :
   print("You are fail because you have less than 40% marks")
else:
    print("Congratulations ! You have passed")
    

# to check spam detector
 
text = input("Enter the text")
if("make a lot of money" in text):
    spam = True
elif("watch this"in text):
    spam = True
elif("Click this"in text):
    spam = True
elif("Open this"in text):
    spam = True
else:
    spam = False

if (spam):
    print("This is a spam text")
else :
    print ("This is not a spam text")

    

# write a program to check weather a given username contains 10 characters or not

username = input("Enter your username which contains at least 10 characters")
if(len(username)>= 10):
    print("Your username is valid")
else:
    print("Your username is invalid")
    

# write a program to find given name present in the list

names = ["zeeshaan" , "shubham" , "rohan" , "pranay" ," dilip"]
name = input("Enter a name to check")
if name in names:
    print("YES ,  your name is present in the list")
else:
    print("NO , Your name is not present in the lsit")


# write a program to check your grade from your percentage

percentage = int(input("Enter ypur percentage "))

if(percentage>=90):
    grade = "A"
elif(percentage>=80):
    grade = "B"
elif(percentage>=70):
    grade = "C"
elif(percentage>=60):
    grade = "D"
elif(percentage>=50):
    grade = "E"
else:
    grade = "Fail"

print("Your grade is" , grade)