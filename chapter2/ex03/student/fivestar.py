# Write your program here
"""
Movie Rental System

This program simulates a DVD rental system for Five Star Retro Video, where customers can rent new and old movies at different prices. The goal is to allow users to rent DVDs, calculate total rental costs based on the number of nights rented, and display the rental details.

Design:
1. Define constants for rental prices:
   - NEW_MOVIE_PRICE = 3.00
   - OLDIE_PRICE = 2.00

2. Create a function to calculate the total rental cost:
   - Input: number of nights and type of movie (new or old)
   - Output: total cost

3. Implement user prompts for inputs:
   - Ask the user for the type of movie (new or old)
   - Ask the user for the number of nights rented

4. Display the total cost to the user with appropriate labels.

5. Test the program with various inputs to ensure accuracy.
"""

# Define constants for rental prices
NEW_MOVIE_PRICE = 3.00
OLDIE_PRICE = 2.00

def calculate_rental_cost(movie_type, nights):
    """Calculate total rental cost based on movie type and nights rented."""
    if movie_type.lower() == 'new':
        return NEW_MOVIE_PRICE * nights
    elif movie_type.lower() == 'old':
        return OLDIE_PRICE * nights
    else:
        raise ValueError("Invalid movie type. Please choose 'new' or 'old'.")

def main():
    """Main function to run the rental system."""
    print("Welcome to Five Star Retro Video Rental System!")
    
    # Get the user input for movie type
    movie_type = input("Enter the type of movie (new/old): ")
    
    # Get user input for number of nights
    nights = int(input("Enter the number of nights you want to rent: "))
    
    # Calculate total cost
    try:
        total_cost = calculate_rental_cost(movie_type, nights)
        print(f"The total rental cost for {nights} night(s) of {movie_type} movie is: ${total_cost:.2f}")
    except ValueError as e:
        print(e)

# Run the program
if __name__ == "__main__":
    main()
