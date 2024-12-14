# Write your program here
# sphere.py

import math

"""
Program: Sphere Properties Calculator

Analysis:
This program calculates the diameter, circumference, surface area, and volume of a sphere based on its radius.

Design (Pseudocode):
1. Prompt the user to input the radius of the sphere.
2. Convert the input to a floating-point number.
3. Calculate the diameter using the formula: diameter = 2 * radius.
4. Calculate the circumference using the formula: circumference = 2 * π * radius.
5. Calculate the surface area using the formula: surface area = 4 * π * radius^2.
6. Calculate the volume using the formula: volume = (4/3) * π * radius^3.
7. Display the calculated diameter, circumference, surface area, and volume to the user.

Inputs:
- radius: Float representing the radius of the sphere.

Outputs:
- diameter: Float representing the diameter of the sphere.
- circumference: Float representing the circumference of the sphere.
- surface_area: Float representing the surface area of the sphere.
- volume: Float representing the volume of the sphere.
"""

def calculate_diameter(radius):
    """
    Calculate the diameter of a sphere.

    :param radius: Float representing the radius of the sphere.
    :return: Float representing the diameter of the sphere.
    """
    return 2 * radius

def calculate_circumference(radius):
    """
    Calculate the circumference of a sphere.

    :param radius: Float representing the radius of the sphere.
    :return: Float representing the circumference of the sphere.
    """
    return 2 * math.pi * radius

def calculate_surface_area(radius):
    """
    Calculate the surface area of a sphere.

    :param radius: Float representing the radius of the sphere.
    :return: Float representing the surface area of the sphere.
    """
    return 4 * math.pi * (radius ** 2)

def calculate_volume(radius):
    """
    Calculate the volume of a sphere.

    :param radius: Float representing the radius of the sphere.
    :return: Float representing the volume of the sphere.
    """
    return (4/3) * math.pi * (radius ** 3)

def main():
    # Prompt the user for the radius of the sphere
    radius = float(input("Enter the radius of the sphere: "))
    
    # Calculate the diameter, circumference, surface area, and volume
    diameter = calculate_diameter(radius)
    circumference = calculate_circumference(radius)
    surface_area = calculate_surface_area(radius)
    volume = calculate_volume(radius)
    
    # Print the results
    print(f"Diameter of the sphere: {diameter}")
    print(f"Circumference of the sphere: {circumference}")
    print(f"Surface area of the sphere: {surface_area}")
    print(f"Volume of the sphere: {volume}")

if __name__ == "__main__":
    main()
