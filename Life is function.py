# Function to calculate the area of a circle
def calculate_area(pi, radius):
    return pi * (radius ** 2)

# Function to calculate total due with tax
def calculate_total_due(money, tax):
    return money + (money * tax)

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# Area of a Circle
print("Area of a Circle")
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
area = calculate_area(pi, radius)
print(f"Area of the circle: {area:.2f}")

# Total Due Calculation
print("\n Total Due Calculation")
money = float(input("Enter the purchase amount: "))
tax = float(input("Enter the tax rate (e.g., 0.07 for 7%): "))
total = calculate_total_due(money, tax)
print(f"Total due: ${total:.2f}")

# Fahrenheit to Celsius
print("\n Temperature Conversion")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"Temperature in Celsius: {celsius:.2f}°C")
print("Life is function by Kidmar Desir")