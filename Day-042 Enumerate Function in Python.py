marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0          -> traditional approach
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Harry, Awesome!")
#     index += 1

#using enumerate function
for index,mark in enumerate(marks):   # by default index starts from 0
# for index,mark in enumerate(marks, start=1):   -> index will start from 1 now
    print(mark)
    if (index == 3):
        print("Harry, Awesome!")
