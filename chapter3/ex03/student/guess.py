# Write your program here
# TKTK: Add started code here.
# guess.py

import math

def guess_number(lower, upper):
    """
    Perform a binary search to guess the user's number.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :return: The number of guesses made.
    """
    guesses = 0
    while lower <= upper:
        guesses += 1
        guess = (lower + upper) // 2
        print(f"Your number is {guess}")
        hint = input("Enter =, <, or >: ")
        
        if hint == "=":
            print(f"Hooray, I've got it in {guesses} tries!")
            return guesses
        elif hint == "<":
            upper = guess - 1
        elif hint == ">":
            lower = guess + 1
        else:
            print("Invalid input. Please enter =, <, or >.")
    
    print("I'm out of guesses, and you cheated!")
    return guesses

def main():
    # Prompt the user for the range
    lower = int(input("Enter the smaller number: "))
    upper = int(input("Enter the larger number: "))
    
    # Calculate the minimum number of guesses needed
    min_guesses = math.ceil(math.log(upper - lower + 1, 2))
    print(f"The minimum number of guesses needed is {min_guesses}.")
    
    # Perform the guessing game
    guess_number(lower, upper)

if __name__ == "__main__":
    main()
