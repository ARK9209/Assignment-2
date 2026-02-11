# Create a Dictionary of Student Marks

student_details ={'Ayush': 85, 'Rahul': 78, 'Sneha': 92, 'Priya': 88}

name = input("Enter the student name: ")

if name in student_details:
    print(f"{name}'s marks are: {student_details[name]}")
else:
    print("Student not found.")