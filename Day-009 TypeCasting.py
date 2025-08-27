a="1"
b="2"
print(a+b,"\n")

#typecasting
a = "1"
b = "2"
print(int(a) + int(b),"\n")

#implicit typecasting
a = 7
print(type(a))
b = 3.1
print(type(b))
c = a+b
print(c)
print(type(c),"\n")

#explicit typecasting
str = "15"
num = 3
str_to_num = int(str)
sum = num + str_to_num
print("The sum of both the numbers is: ", sum)