set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Add items from set2 to set1 except the common items
set1.update(set2 - set1)
print("Updated set1 with non-common items:", set1)
