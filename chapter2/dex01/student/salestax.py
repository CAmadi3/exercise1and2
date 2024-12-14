# Corrected program to compute sales tax

purchasePrice = float(input("Enter the purchase price as $: "))
taxRate = int(input("Enter the tax rate as %: "))

# Convert the tax rate from percentage to decimal
taxRateDecimal = taxRate / 100

# Calculate the tax and total amount owed
tax = purchasePrice * taxRateDecimal
totalOwed = purchasePrice + tax

print("Purchase price: ", purchasePrice)
print("Tax: ", tax)
print("Total owed: ", totalOwed)
