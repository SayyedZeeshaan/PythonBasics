
    
while True: 

    print("Press 1 for addition , Press 2 for Subtraction , Press 3 For Multiplication , Press 4 for Division and press 5 to get Percentage")
    print("To Quit press q")
    
    operation = input("Enter the number of operation that you want to perform : ")
    

    if operation == "q" or operation == "Q":
            break
    elif operation == "1":
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            sum = num1+num2
            print(f"The addition of {num1} and {num2} is {sum}\n" )

    elif operation == "2":
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            sub = num1-num2
            print(f"The subtration of {num2} form {num1} is {sub}\n ")

    elif operation == "3":
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            mul = num1*num2
            print(f"The multiplication of {num1} and {num2} is {mul}\n ")

    elif operation == "4":
            num1 = float(input("Enter number 1 : "))
            num2 = float(input("Enter number 2 : "))
            div=num1/num2
            print (f"Value of {num1} divided by {num2} is {div}\n ")
            
    elif operation == "5":
            num1 = float(input("Enter value : "))
            num2 = float(input("Enter Total value : "))
            per = (num1/num2) * 100
            print (f"Percentage of {num1} from {num2} is {per}% \n ")
            


    else :
        print(f"Invalid Operation!! Please Enter a valid operation\n " )


    
print("Thanks for using the calculator")