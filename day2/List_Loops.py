students = ["sai", "vasu", "kiran", "vishnu"]
for student in students:
    print(f"Hello, {student}")
students.append("venu")
students.remove("vasu")
print(students[0])
print(students[-1])
print(f"Total students: {len(students)}")




even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")