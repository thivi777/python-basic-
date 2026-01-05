a = 10
b = "python"
c =10

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))  

# 20.12.2025
# Calculate the average of three numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

average = (a + b + c) / 3
print("The average of three numbers is:", average)

# Calculate the sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a*a + b*b + 2*a*b

print("The sum of two numbers is:", result)

# finding unit place digit question 
num = int(input("Enter a number: "))

unit_digit = num % 10
print("Unit place digit:", unit_digit)

# modifying variable values
num = int(input("Enter a number: "))

tens_digit = (num // 10) % 10
print("Tens place digit:", tens_digit)

# 21.12.2025
# membership operator
a = "Hello, welcome to Python programming"  
b = "Python"
if b in a:
    print(f'"{b}" is found in the string.')
else:
    print(f'"{b}" is not found in the string.') 

# comparison operator
# character by character - left to right
# using ASCII values

# python is case sensitive
str1 = "Enter first string"
str2 = "Enter second string"

print(str1 == str2)  # equal to
print(str1 != str2)  # not equal to
print(str1 > str2)   # greater than
print(str1 < str2)   # less than
print(str1 >= str2)  # greater than or equal to
print(str1 <= str2)  # less than or equal to    
# capetale letter unicode less than small letter unicode

text = "python programming"

print(text.lower)()  # converts to lowercase
print(text.upper())  # converts to uppercase
print(text.capitalize())  # capitalizes first letter
print(text.title())  # capitalizes first letter of each word
print("first character of each word become upper". title())

print(text.index("p"))  # returns index of first occurrence of 'p'
print(text.index("g"))  # returns index of first occurrence of 'g'
print(text.count("o"))  # counts occurrences of 'o'

newstr = "   Hello, World!   "
print(newstr.strip())  # removes leading and trailing whitespace

# list of strings methods
# list is a collection of items in a particular order
empty = []
print(type(empty))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = [1, "a", 2.5, True]

print(list1 + list2)  # concatenation
print(list2 + list1)
print(list1 + list2 + list3)

print(list1 * 3)  # repetition

# Accessing list elements
print(list1) # entire list

# dynamic programming - no need to declare variable type
# a =10
# b = "python"
# c = "10"

# print(a)
# print(type(a))#int
# print(b)
# print(c)
# print(type(c))#string

# a = True
# print(a)
# # print(A)#not defined
# print(type(a))#boolen

# print (type(5))
# print (type(0FF))
print(type([]))