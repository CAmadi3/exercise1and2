# Write your program here
# equilateral.py

"""
Program: Equilateral Triangle Checker

Analysis:
This program determines whether a triangle is equilateral based on the lengths of its three sides.
An equilateral triangle has all three sides of equal length.

Design (Pseudocode):
1. Prompt the user to input the lengths of the three sides of the triangle.
2. Convert the inputs to floating-point numbers.
3. Check if all three sides are equal.
4. If all sides are equal, print that the triangle is equilateral.
5. Otherwise, print that the triangle is not equilateral.

Inputs:
- side1: Float representing the length of the first side.
- side2: Float representing the length of the second side.
- side3: Float representing the length of the third side.

Outputs:
- A message indicating whether the triangle is equilateral or not.
"""

def is_equilateral(side1, side2, side3):
    """
    Determine if a triangle is equilateral.

    :param side1: Float representing the length of the first side.
    :param side2: Float representing the length of the second side.
    :param side3: Float representing the length of the third side.
    :return: Boolean indicating whether the triangle is equilateral.
    """
    return side1 == side2 == side3

def main():
    # Prompt the user for the lengths of the three sides
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    
    # Check if the triangle is equilateral
    if is_equilateral(side1, side2, side3):
        print("The triangle is equilateral.")
    else:
        print("The triangle is not equilateral.")

if __name__ == "__main__":
    main()
