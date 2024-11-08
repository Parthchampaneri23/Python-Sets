#Write a Python program to Get Only unique items from two sets.
#Input:
#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#Output:
#{70, 40, 10, 50, 20, 60, 30}


# Define the input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Calculate the symmetric difference
unique_items = set1 ^ set2  # or you can use set1.symmetric_difference(set2)

# Print the output
print(unique_items)
