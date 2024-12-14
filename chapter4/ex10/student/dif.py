# Write your program here
# dif.py

def compare_files():
    # Prompt the user for the names of two text files
    file1_name = input("Enter the name of the first text file: ")
    file2_name = input("Enter the name of the second text file: ")

    try:
        # Open the files for reading
        with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
            # Read and compare lines from both files
            for line_num, (line1, line2) in enumerate(zip(file1, file2), start=1):
                if line1 != line2:
                    # Output "No" and the first differing lines
                    print("No")
                    print(f"Difference at line {line_num}:")
                    print(f"File 1: {line1.strip()}")
                    print(f"File 2: {line2.strip()}")
                    return
            
            # Check if one file has extra lines
            if file1.read() or file2.read():
                print("No")
                print("One file has additional lines.")
            else:
                # Files are identical
                print("Yes")

    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    compare_files()
