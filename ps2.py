
# greeting user
name = input("Enter your name")
print ("Good Morning, "+  name) 

# letter 

letter = ''' Dear <| Name |> ,
You are selected!

Date : <| Date |>
'''
Name = input("Enter your name\n")
Date = input("enter date")
letter = letter.replace( "<| Name |>" , Name)
letter = letter.replace( "<| Date |>" , Date)
print(letter)