# break -> loop se bahar nikalna
for i in range(12):
    if i==11:
        break
    print("5 X ", i, "=", 5 * i)
print("move out of the loop")


# continue -> iteration se bahar nikalna
for j in range(13):
    if j==11:
        print("skip the iteration")
        continue
    print("5 X ", j, "=", 5 * j)

