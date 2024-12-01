# Step 1: Creating an empty list called my_list
my_list = []

# Step 2: Appending elements in list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Inserting the value 15 at the second position in the list
my_list.insert(1, 15)

# Step 4: Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Removing the last element from my_list
my_list.pop()

# Step 6: Sorting my_list in ascending order
my_list.sort()

# Step 7: Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)

# Printing the results
print("Final my_list:", my_list)
print("Index of 30:", index_of_30)
