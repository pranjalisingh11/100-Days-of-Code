import math
result = math.sqrt(9)
print(result)  # Output: 3.0

# from keyword
from math import sqrt
result = sqrt(9)
print(result)  # Output: 3.0

# using multiple functions togethar
from math import sqrt, pi
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793

# importing everything -> generally not suitable
from math import *
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793

# as keyword
import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793

#dir function ->  use to view the names of all the functions and variables defined in a module
import math
print(dir(math))