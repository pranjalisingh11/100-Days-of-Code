fruit = "Mango"
print(len(fruit))
len1 = len(fruit)
print("Mango is a ", len1, "letter word. \n")
fruit2 = "Apple, Banana"
# it includes comma and space also
print("Apple, Banana is also a ",len(fruit2), "letter word. \n")

# slicing operation on strings
# syntax = [0 : n-1]
print(fruit[0:4])
print(fruit[:4])
print(fruit[1:4])
print(fruit[:5]) #by default python will take the starting index as 0
print(fruit[:]) #by default it will be taken as full length of a string and return the whole string
print(fruit[0:5])
print(fruit[2:4],"\n")

#negative slicing
print(fruit[0:-3])
print(fruit[0:len(fruit)-3],"\n")
#we perform negative slicing by subtract it from the full length of the string
#i.e len(fruit) = 5 and 5-3 = 2 which gives Ma as an output.

print(fruit[-1:len(fruit)-3]) #it will not return anything as it is 5-1=4:5-3=2, 4:2 which is not possible
print(fruit[-3:-1], "\n") # it will return 2:4 = ng


#Quick quiz
nm = "Harry"
print(nm[-4:-2]) #it will give 1:3 , so it will give index 1 to index 2 because n-1, which is ar



