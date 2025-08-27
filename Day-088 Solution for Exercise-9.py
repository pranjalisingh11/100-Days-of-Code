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