a = "Pranjalii"
print(a)

#length method
print(len(a))

#uppercase method
print(a.upper())

#lowercase method
print(a.lower())

#strip -> removes any white spaces before and after the string
b = " Singh Parihar  "
print(b.strip())

#rstrip method -> it will remove the trailing characters only after the string
c = "!!! Gungun !!!"
print(c.rstrip("!"))

#replace method -> replaces all occurences of a string with another string
d = "Silver Spoon"
print(d.replace("Sp", "M"))

#split method -> splits the given string at the specified instance and returns the separated strings as list items
e = "Silver Spoon"
print(e.split(" "))      #Splits the string at the whitespace " ".

#capitalize method -> turns only the first char to uppercase and rest all the char to lowercase
blogHeading = "introduction to python"
print(blogHeading.capitalize())
f = "intro tO DjanGO"
print(f.capitalize())

#center method -> align the string to the center,
g = "Welcome to Console!!!"
print(g.center(50))
print(len(g))
print(len(g.center(50))) #so the len of g is 21 so it will give 29 spaces

#count method - count the number of values occurs in the given string
h = "Gungun Singh Gungun"
print(h.count("Gungun"))

#endswith method - check if the string ends with the given value
i = "Welcome to Console !!!"
print(i.endswith("!!!"))   #returns boolean value
print(i.endswith("??"))
print(i.endswith("to",4,10))

#startswith method -> check if the string starts with the given value
i1 = "!!! Welcome to Console ??"
print(i.startswith("!!!"))   #returns boolean value
print(i.startswith("??"))
print(i.startswith("to",4,10))

#find method -> searches for the first occurrence of the given value and returns the index where it is present.
j = "His name is Dan. He is an honest man."
print(j.find("is"))
print(j.find("an",2,10)) #if given value is absent, then return -1

#index method -> searches for the first occurrence of the given value and returns the index where it is present.
# but if given value is absent, then raise an exception, i.e. ValueError
k = "His name is Dan. He is an honest man."
# print(g.index("an",2,10)) #substring not found

#isalnum method -> checks if the string is alphanumeric, only consists A-Z, a-z, 0-9
l = "WelcomeToTheConsole9"
print(l.isalnum()) #returns bool value
l1 = "WelcomeToTheConsole!!!"
print(l1.isalnum())

#isalpha method -> only consists alphabets, A-Z, a-z
m = "Welcome"
print(m.isalpha())
m1 = "Welcome00"
print(m1.isalpha())

#islower method -> returns true if all the char in the string are in lowercase, else false
n = "gungun sp"
print(n.islower())

#isupper method -> returns true if all the char in the string are in uppercase, else false
r = "GUNGUN SINGH"
print(r.isupper())

#isprintable method -> returns true if all the values withing the given string are printable,else false
o = "Happy Diwali"
print(o.isprintable())
o1 = "Happy Diwali\n"
print(o1.isprintable())

#isspace method -> returns true only if the string contains white spaces
p = " "
print(l.isspace())
p1 = "Gungun Singh"
print(p1.isspace()) #only spaces

#istitle method -> returns true only if first letter of each word of the string is capitalized
q = "Gungun Singh Parihar"
print(q.istitle())

#swapcase method -> converts lowercase to uppercase and viceversa
s = "gungun"
print(s.swapcase())
s1 = "GUNGUN"
print(s1.swapcase())

#title method -> capitalizes each letter of the word withing the string
t = "My name is gungun !!"
print(t.title())



s = "LearnPythonWithGPT"
print(s[::2])       # Output: LarnyhnihPT
print(s[1:8:3])     # Output: eo
print(s[-5:-1])

