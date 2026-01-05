# Q1: Student details and grade calculation

name = input("Enter your name: ")
age = int(input("Enter your age: "))

m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

average = (m1 + m2 + m3) / 3

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Average: {average:.2f}")
print(f"Grade  : {grade}")


# Q2: Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print("Result:", result)


# Q3: List operations

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("List:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)


# Q4: Tuple operations

marks = (78, 85, 69, 90, 88)

print("Total marks:", sum(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

# Tuple is suitable because:
# - Marks should not be changed accidentally
# - Tuples are immutable (cannot be modified)
# - They are safer for fixed data


# Q5: Swapping two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# Q6: Dictionary operations

student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "course": input("Enter course: "),
    "marks": []
}

for i in range(3):
    mark = float(input(f"Enter mark {i+1}: "))
    student["marks"].append(mark)

average = sum(student["marks"]) / len(student["marks"])

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

student["grade"] = grade

print("\nStudent Dictionary:")
print(student)
