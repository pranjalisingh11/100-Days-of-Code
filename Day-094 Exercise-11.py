# Write a python program which reminds you of drinking water every hour or two.
# Your program can either beep or send desktop notifications for a specific operating system

import time
import winsound
from win10toast import ToastNotifier
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

toaster = ToastNotifier()
interval = 5

while True:
    winsound.Beep(1000, 1000)
    # First argument 1000 → the frequency(pitch of sound) in Hertz(Hz). 1000 Hz is like a medium beep.
    # Second argument 1000 -> the duration of the beep in milliseconds. 1000 ms = 1 second.
    # So: "Beep at 1000 Hz for 1 second."
    toaster.show_toast(
        "💧 Water Reminder",
        "Hey Gungun, Drink water now!",
        duration=10,
        threaded=True  # This makes it non-blocking
    )
    # "title", "message body of the notification", "the notification stays on screen for 10 seconds".

    speaker.Speak("Hey Gungun, drink water now!")  # Speaks while popup is visible

    time.sleep(interval)

