# ---------------------------------------------------------
# Program: Longest Increasing Sequence
#
# Accept numbers from the user and find the length of the
# longest continuous increasing sequence.
#
# Example Input:
# 5 8 10 12 3 4 5 6 1
#
# Example Output:
# Longest Sequence Length = 4
# ---------------------------------------------------------

# Take numbers from user separated by spaces
numbers = list(map(int, input("Enter numbers: ").split()))

# Current increasing sequence length
count = 1

# Longest increasing sequence found so far
maximum = 1

# Traverse the list
for i in range(len(numbers) - 1):

    # Check if next number is greater than current number
    if numbers[i + 1] > numbers[i]:

        # Increase current sequence length
        count += 1

    else:

        # Sequence breaks, start counting again
        count = 1

    # Update maximum sequence length if needed
    if count > maximum:
        maximum = count

# Display result
print("Longest Sequence Length =", maximum)