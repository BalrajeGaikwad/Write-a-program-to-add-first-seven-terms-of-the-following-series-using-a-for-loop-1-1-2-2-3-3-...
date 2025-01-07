#Write a program to add first seven terms  of the following series using a for loop  1/1! +2/2! +3/3!+...

# Initialize variables
sum_series = 0

# Loop through the first 7 terms
for i in range(1, 8):  # 1 to 7
    # Calculate factorial of i
    factorial = 1
    for j in range(1, i + 1):  # Multiply numbers from 1 to i
        factorial *= j
    
    # Add the current term to the sum
    sum_series += i / factorial

# Print the result
print("The sum of the first seven terms of the series is:", sum_series)
