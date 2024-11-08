#Write a Python program to Check if two sets have any elements in common. Ifyes, display the common elements.
#Input:
#set1 = {10, 20, 30, 40, 50}
#set2 = {60, 70, 80, 90, 10}
#Output:
#{10}

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find the intersection of the two sets
common_elements = set1.intersection(set2)

# Check if there are common elements and display them
if common_elements:
    print(common_elements)
else:
    print("No common elements")
