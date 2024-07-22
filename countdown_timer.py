#!/usr/bin/python3

import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')  # Print the time in place
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("00:00")  # Print final 00:00 when countdown is complete

# Set the countdown time (60 seconds for 1 minute)
countdown_timer(60)
