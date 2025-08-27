# simple while loop
# a=0
# while a<3:
#     print(a)
#     a=a+1
# print("Done with the loop")

i=int(input("enter any number: "))
while i<=38:
    i = int(input("enter any number: "))
    print(i)
print("Done with the loop")


#decrementing while loop
count = 5
while count>0:
    print(count)
    count = count - 1  #count + 1 will result in infinite loop


#else with while loop
count = 5
while count>0:
    print(count)
    count = count - 1
else:
    print("I am inside else")


#python does not have do-while loop
# do{
#     loop body:
# }
# while(condition);
#example:
# i=int(input("enter any number: "))
# print(i) #do body
# while i<=38: #while
#     i = int(input("enter any number: "))
#     print(i)
# print("Done with the loop")
