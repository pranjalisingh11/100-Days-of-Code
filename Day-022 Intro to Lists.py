marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))

#positive indexing
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index


#to check whether the value is present in list or not
if "6" in marks: #"6" is string data type and in marks 6 is a int data type
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

#slicing operator
print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3]) #start:end:jump_index

#list comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)