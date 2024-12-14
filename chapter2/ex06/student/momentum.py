# Write your program here
# momentum_kinetic_energy.py

"""
Program: Momentum and Kinetic Energy Calculator

Analysis:
This program calculates the momentum and kinetic energy of an object based on its mass and velocity.
Momentum is calculated using the formula: momentum = mass * velocity.
Kinetic energy is calculated using the formula: kinetic_energy = (1/2) * mass * velocity^2.

Design (Pseudocode):
1. Prompt the user to input the mass of the object in kilograms.
2. Prompt the user to input the velocity of the object in meters per second.
3. Convert the inputs to floating-point numbers.
4. Calculate the momentum using the formula: momentum = mass * velocity.
5. Calculate the kinetic energy using the formula: kinetic_energy = (1/2) * mass * velocity^2.
6. Display the calculated momentum and kinetic energy to the user.

Inputs:
- mass: Float representing the mass of the object in kilograms.
- velocity: Float representing the velocity of the object in meters per second.

Outputs:
- momentum: Float representing the momentum of the object.
- kinetic_energy: Float representing the kinetic energy of the object.
"""

def calculate_momentum(mass, velocity):
    """
    Calculate the momentum of an object.

    :param mass: Float representing the mass of the object in kilograms.
    :param velocity: Float representing the velocity of the object in meters per second.
    :return: Float representing the momentum of the object.
    """
    return mass * velocity

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate the kinetic energy of an object.

    :param mass: Float representing the mass of the object in kilograms.
    :param velocity: Float representing the velocity of the object in meters per second.
    :return: Float representing the kinetic energy of the object.
    """
    return 0.5 * mass * (velocity ** 2)

def main():
    # Prompt the user for the mass and velocity of the object
    mass = float(input("Enter the mass of the object in kilograms: "))
    velocity = float(input("Enter the velocity of the object in meters per second: "))
    
    # Calculate the momentum and kinetic energy
    momentum = calculate_momentum(mass, velocity)
    kinetic_energy = calculate_kinetic_energy(mass, velocity)
    
    # Print the results
    print(f"The momentum of the object is: {momentum} kg*m/s")
    print(f"The kinetic energy of the object is: {kinetic_energy} joules")

if __name__ == "__main__":
    main()
