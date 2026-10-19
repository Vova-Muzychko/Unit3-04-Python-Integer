#!/usr/bin/env python3
# Created by: VovaM
# Created on: October 19, 2026
# This program checks if an integer is positive, negative, or zero.


def main():
    # Input: get integer from the user
    user_number = int(input("Enter an integer: "))

    # Process & Output: check the sign of the integer
    if user_number > 0:
        print("It is a positive number.")
    elif user_number < 0:
        print("It is a negative number.")
    else:
        print("It is zero.")


if __name__ == "__main__":
    main()
