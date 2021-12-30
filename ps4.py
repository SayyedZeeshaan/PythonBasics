
#dictionary

myDict = {
    "Zeeshaan" : "A football player",
    " SayyedZeeshaan" : "A coder",
    " age " :"24",
    1 : 2 
}
print(list(myDict.keys()))   #print keys of dictionary

print(list(myDict.values()))   #print values of dictionary

print(myDict)

updteDict={                      #update a dictionary
    "Address" : "Akola",
    "Pin" : "444001"
 }

myDict.update(updteDict)

print(myDict)

print(myDict.get("Zeeshaan"))    # returns none if not present in dictionary

print(myDict["Zeeshaan"])         #throws error if not present in dictionary



# Sets
a = {1,2,3,4,5}  #no repeated value in set

b = set()        #empty set 

a.add(6)

a.add(7)            #add values in set

a.add((8,9,10))        #can add tuples in set

print(a)

# dictionaty cannot be added in sets

print(len(a))

a.remove(3)          #remove value form set

print(a)