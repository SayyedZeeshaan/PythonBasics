a = " a1 , a2 , a3 "
b = " b1 , b2 , b3 "

c = a.split(",")
print (c)
d = b.split(",")
print (d)

mymap = {
    c[0] : d[0],
    c[1] : d[1],
    c[2] : d[2]
    }

print(mymap)