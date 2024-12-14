# Write your program here
# momentum.py

"""
Program: Momentum Calculator

Analysis:
This program calculates the momentum of an object based on its mass and velocity.
Momentum is calculated using the formula: momentum = mass * velocity.

Design (Pseudocode):
1. Prompt the user to input the mass of the object in kilograms.
2. Prompt the user to input the velocity of the object in meters per second.
3. Convert the inputs to floating-point numbers.
4. Calculate the momentum using the formula: momentum = mass * velocity.
5. Display the calculated momentum to the user.

Inputs:
- mass: Float representing the mass of the object in kilograms.
- velocity: Float representing the velocity of the object in meters per second.

Outputs:
- momentum: Float representing the momentum of the object.
"""

def calculate_momentum(mass, velocity):
    """
    Calculate the momentum of an object.

    :param mass: Float representing the mass of the object in kilograms.
    :param velocity: Float representing the velocity of the object in meters per second.
    :return: Float representing the momentum of the object.
    """
    return mass * velocity

def main():
    # Prompt the user for the mass and velocity of the object
    mass = float(input("Enter the mass of the object in kilograms: "))
    velocity = float(input("Enter the velocity of the object in meters per second: "))
    
    # Calculate the momentum
    momentum = calculate_momentum(mass, velocity)
    
    # Print the result
    print(f"The momentum of the object is: {momentum} kg*m/s")

if __name__ == "__main__":
    main()
