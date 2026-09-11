   #Student Marks Management System
print("------------------------- Student Marks Management System ---------------------------")

marks = [70, 80, 65, 90]

# Display marks - Traversal
print("Original Marks:")
for mark in marks:
    print(mark)

# Insert a new mark
marks.insert(2, 75)

print("\nAfter Insertion:")
print(marks)

# Update a mark
marks[1] = 85

print("\nAfter Updating:")
print(marks)

# Delete a mark
marks.remove(65)

print("\nAfter Deletion:")
print(marks)