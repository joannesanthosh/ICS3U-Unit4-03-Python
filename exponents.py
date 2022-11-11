#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created in: Nov 2022
# A program that uses loops


def main():
    # Finds the square of integers

    number = input("Enter a positive integer: ")
    try:
        floating_point_number = float(number)
        integer = int(number)
        if integer > 0 and integer == floating_point_number:
            print("")
            for counter in range(integer + 1):
                answer = counter * counter
                print("{0}² = {1}".format(counter, answer))
        elif integer == 0 and integer == floating_point_number:
            print("\n0² = 0")
        else:
            print("\n{} is not a positive integer.".format(integer))
    except ValueError:
        print("\nError: {} is not an integer.".format(number))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
