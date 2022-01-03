
marks1 = [45 , 56, 76, 98]
percentage1 = (sum(marks1)/400)*100


marks2 = [ 67 , 58 , 74 , 95]
percentage2 = (sum(marks2)/400)*100

print (percentage1, percentage2)

# using function

def percent(marks):
    return((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

marks1 = [45 , 56, 76, 98]
percentage1 = percent(marks1)


marks2 = [ 67 , 58 , 74 , 95]
percentage2 = percent(marks2)

print (percentage1 , percentage2)



# funtion to greet a user

def greet(name="Stranger"):    # to use default value
    print("Good Day " + name)

greet("Zeeshaan")     
greet()             # this prints Hello Stranger because stranger is a default value



# Find the maximum number from a set of numbers

def maximum( num1 , num2 , num3 ):
    if(num1>num2):
        if (num1>num3):    
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3

m = maximum( 95 , 554 , 555)
print ("The value of maximum is " + str(m))


# to change celcius to farenhight

def farh(cel):
    return(cel * (9/5)) + 32

c = int(input("Enter temperature in celcius to convert it in farenhight"))
f= farh(c)
print("The temperature in farenhight is " , f)


# print different print functions in same line

print("Hello" , end=" ")
print("How" , end=" ")
print("are", end = " ")
print("you?" , end= " ") 


# draw star pattern
#  ***
#  **
#  *

n = 3
for i in range(n):
    print("*" * (n-i))


# Strip means to remove spaces from a string using (this.strip())

def remove_and_strip(string , word):        #remove a word from a string
    newStr = string.replace(word , "")      # to replace a word in a string
    return newStr.strip()
    
this = "      Zeeshaan is a football player       "
n = remove_and_strip(this , "is")
print(n)
