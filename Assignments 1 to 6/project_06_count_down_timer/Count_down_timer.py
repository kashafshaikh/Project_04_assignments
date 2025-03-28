import time

def countdown(t):
    while t > 0:  # Ensure countdown runs only for positive values
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # Overwrite previous output
        time.sleep(1)
        t -= 1

    print("\nTime's Up!")  # Moves to new line when countdown ends

# Input Validation
while True:
    try:
        t = int(input("Enter the time in seconds for countdown: ").strip())
        if t > 0:
            break
        else:
            print("⛔ Please enter a positive number!")
    except ValueError:
        print("❌ Invalid input! Enter a valid number.")

countdown(t)
