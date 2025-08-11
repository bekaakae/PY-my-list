# Initialize an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])
print("After appending elements:", my_list)

# Insert 15 at index 1 (second position)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# Extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)