# Demonstrate List slicing
# List
l1 = list(range(1,11))
# Extracted first five elements
Ext= l1[0:5]
# Reversed extracted elements
reverse = Ext[::-1]

print(f"Original list: {l1}")
print(f"Extracted first five elements: {Ext}")
print(f"Reversed extracted elements: {reverse}")