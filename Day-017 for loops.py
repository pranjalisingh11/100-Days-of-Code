# iterating over a string
name="Pranjali"
for i in name:
    print(i,end=",")
    if i=="n":
        print("this is a special character.")

# iterating over a list
colors=["red","blue","green","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#range() function
for k in range(5): # 0 to 4(n-1)
    print(k)

for m in range(1,12,2):
    print(m)