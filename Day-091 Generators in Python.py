def my_generator():
    for i in range(5000):
      # Complex computations
      yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in  gen:
  print(j)