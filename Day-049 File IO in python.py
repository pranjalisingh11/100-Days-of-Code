# READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close() # -> this is mandate to close a file

# using with -> automatically closes the file
with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside with")