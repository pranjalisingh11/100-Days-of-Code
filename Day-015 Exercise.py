import time

# Get the current hour in 24-hour format as an integer
current_hour = int(time.strftime('%H'))

# Display current time
current_time = time.strftime('%H:%M:%S')
print("Current Time:", current_time)

# Greet based on the hour
if 5 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 17:
    print("Good Afternoon!")
elif 17 <= current_hour < 21:
    print("Good Evening!")
else:
    print("Hello! It's late, take rest or have a good night!")
