# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
#
# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce:
#
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry
# Note: If you are not using windows, try to figure out how to do the same thing using some other package

# Python program to convert
# text to speech

# import the required module from text to speech conversion
import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = input("Enter items separated by space: ").split()

for name in names:
    s = f"Shoutout to {name}"
    print(s)
    speaker.Speak(s)

# To stop the program press
# CTRL + Z