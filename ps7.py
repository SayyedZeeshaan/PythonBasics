# program to reply same input
 
msg= input("Say Something ")

while msg != "Stop Copying":
    print (msg)
    msg = input()



# # Print numbers till 20 using while loop

# i = 1

# while i <=20 :
#     print ("The value of i is " , i)
#     i = i+1

# # to print contents of a list

# fruits =["orange" , "grapes" , "mango" , "banana" , "apple" ]

# i=0

# while i<len(fruits):
#     print(fruits[i])
#     i = i+1

# # check list of employes using for loop
# employes = ["Zeeshaan" , "Ajay" , "Saqlain" , "Varun" , "Dipesh" , "Raju"]

# for items in employes:
#     print(items)

# #

# for i in range(8):
#     print(i)
# for a in range(10 , 20):
#     print(a)
# else:
#     print("End")    
    
    


# # print table using for loop

# number = int(input("Enter the number "))
# for i in range (1 , 11):

# #    print(str(number) + " X " + str(i) + " = " + str(i*number))         method 1

#      print(f"{number}X{i}={number*i}")                               # method 2


# #  print table using while loop

# num = int(input("Enter a number to get its table"))
# i = 1

# while(i<=10):
#     print(str(num) + "X" + str(i) +  "=" +  str(i*num) )
#     i = i+1


# # program to greet persons in a list whose name starts with S

# l1 = [ "Zeeeshaan" , "Soham" , "Sachin" , "Rahul"]

# for name in l1:
  
#     if name.startswith("S"):
  
#         print("Hello " + name)


# #  write program to find a given number is prime or not

# num = int(input("Enter the number : "))
# prime = True

# for i in range(2 , num):

#     if(num % i == 0):
#         prime = False
#         break

# if prime:
#     print("The number you entered is a prime number")

# else:
#     print("The number you entered is not a prime number")


# #  write a program to find sum of n natural numbers

# n = int(input("Enter any natural number ")) 
# i = 1
# sum = 0

# while ( i<=n ):
#     sum = sum+i
#     i  = i + 1

# print(" The sum of natural numbers is = ", sum)


# # program to find factorial of number

# num = int(input("Enter any number ")) 

# factorial = 1

# for i in range (1 , num+1):
#     factorial = factorial * i
# print(f"The factorial of this number is {factorial}")

# # print a pattern

# n = 4 
# for i in range(4):
#     print("*" * (i+1))
    