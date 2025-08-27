import time

#time.time() method -> eturns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized).
def usingWhile():
  i = 0
  while i<500:
    i = i +1
    print(i)

def usingFor():
  for i in range(500):
    print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)


# time.sleep() method
print(4)
time.sleep(3)
print("This is printed after 3 seconds")


# time.strftime() method
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)