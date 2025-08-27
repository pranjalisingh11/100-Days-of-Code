# harry.py
def welcome():
  print("Hey you are welcome from harry")

# print(__name__)

if __name__ == "__main__":   # to determine whether the script is being run directly or being imported as a module into another script.
  welcome()

#main.py
import harry
harry.welcome

