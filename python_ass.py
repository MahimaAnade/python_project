import time

def countdown_timer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    print("Time's up!")

# Example usage: countdown for 10 seconds
countdown_timer(10)
