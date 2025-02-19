set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Add items from set2 that are not in set1
set1.update(set2 - set1)
print("Updated set1:", set1)
