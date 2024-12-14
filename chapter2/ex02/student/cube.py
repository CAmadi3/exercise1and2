# Write your program here
# cube.py

"""
Program: Cube Surface Area Calculator

Analysis:
This program calculates the surface area of a cube. The surface area of a cube is determined by the formula:
Surface Area = 6 * (edge_length ** 2)

Design (Pseudocode):
1. Prompt the user to input the length of the cube's edge.
2. Convert the input to an integer.
3. Calculate the surface area using the formula: 6 * (edge_length ** 2).
4. Display the calculated surface area to the user.

Inputs:
- edge_length: Integer representing the length of the cube's edge.

Outputs:
- surface_area: Integer representing the surface area of the cube.
"""

def calculate_surface_area(edge_length):
    """
    Calculate the surface area of a cube.

    :param edge_length: Integer representing the length of the cube's edge.
    :return: Integer representing the surface area of the cube.
    """
    return 6 * (edge_length ** 2)

def main():
    # Prompt the user for the length of the edge
    edge_length = int(input("Enter the length of the cube's edge: "))
    
    # Calculate the surface area
    surface_area = calculate_surface_area(edge_length)
    
    # Print the result
    print(f"The surface area of the cube is: {surface_area}")

if __name__ == "__main__":
    main()


