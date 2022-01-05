'''

# OOPS practice 

# write a class programmer for storing information of few programers working at ezygen

class programmer:
    company = "Ezygen"
    
    def __init__(self , name , product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

zeeshaan = programmer("zeeshaan " , "python")
abrar = programmer("abrar " , "python ")

zeeshaan.getInfo()
abrar.getInfo()



# write a class calculator capable of finding square , cube and squareroot of a number

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    
    def squareRoot(self):
        print(f"The squareRoot of {self.number} is {self.number**0.5}")


a = int(input("Enter a number to get its square , cube and squareroot"))
b = Calculator(a)
b.square()
b.cube()
b.squareRoot()


# greet the user in the square , cube , and squareroot calculator 

class Calculator:
    def __init__(self, number ):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    
    def squareRoot(self):
        print(f"The squareRoot of {self.number} is {self.number**0.5}")
    
    @staticmethod
    def greet():
        print("******Hello user welcome to my square , cube and squareroot calculator*****")


# a = int(input("Enter a number to get its square , cube and squareroot"))  --> can also be done by taking input from user

b = Calculator(9)
b.greet()
b.square()
b.cube()
b.squareRoot()


# write a class train which has methods to book a ticket , get status of no of seats anf fare info

class Train:
    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The number of seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket in {self.name} is {self.fare} Rs")


intercity = Train("Intercity Express(11022)" , 250 , 10)
intercity.getStatus()
intercity.fareInfo()

'''

# use the above program and add a ticket booking option

class Train:
    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The number of seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket in {self.name} is {self.fare} Rs")
    def bookTicket(self):
        if (self.seats > 0 ):
            print(f"Your ticket has been booked and it is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry the train is full , Try in another train")

intercity = Train("Intercity Express(11022)" , 250 , 10)

intercity.getStatus()

intercity.fareInfo()

intercity.bookTicket()

intercity.getStatus()