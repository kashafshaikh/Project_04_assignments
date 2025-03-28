# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

import time

def main():
    # Loop from 10 down to 1 using range(start, stop, step)
    # start=10, stop=0 (it will stop before 0), step=-1 (counting backwards)
    for i in range(10, 0, -1):
        print(i)  # Print each number in the countdown
        time.sleep(1)   # Pause for 1 second
    # After the countdown, print Liftoff!
    print("Liftoff!")

# Required line to call main() function when script runs
if __name__ == '__main__':
    main()