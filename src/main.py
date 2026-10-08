# Print name
print("Name: Nur Mohammad")

# Print today’s date
from datetime import date
print("Today's date: ", date.today())

# calling utility functions 
from utils import add, subtract, multiply, divide

print("Addition:", add(5,6))

print("Subtraction:", subtract(45, 32))

print("Multiplication:", multiply(10, 5))

# Handle division by zero error
try:
    print("Division:", divide(10, 2))
    print("Division:", divide(10, 0))
except ValueError as error:
    print("Error:", error)

    