'''The program contains several errors, including syntax errors and logical errors.
Errors:
Syntax Error:

Missing parentheses at the end of the input statement.
Missing colon (:) at the end of the while statement.
The variable total is used before it is initialized.
Logical Error:

The while loop condition should be count <= 10 to include the 10th iteration.
The total variable should be initialized before the loop starts.
Corrected Code:
Here is the corrected version of the program:'''

# Corrected program to compute the average of 10 test scores

count = 1
total = 0  # Initialize total to 0 before the loop

while count <= 10:  # Include the 10th iteration
    score = int(input("Enter test score number " + str(count) + ": "))  # Corrected input statement
    total = total + score
    count = count + 1

average = total / 10  # Calculate the average
print("The average test score is", average)
