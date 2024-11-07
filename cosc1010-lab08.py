# Donovan Appelhans
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to:
# ChatGPT



# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_string(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        pass
    try:
        float_value = float(value)
        if '.' in value and value.count('.') == 1:
            if len(value.split('.')[1]) > 1:
                return False
            return float_value
        else:
            return float_value
    except ValueError:
        return False
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower_x_bound, upper_x_bound):
    if not isinstance(lower_x_bound, int) or not isinstance(upper_x_bound, int):
        return False
    if lower_x_bound > upper_x_bound:
        return False
    y_values = []
    for x in range(lower_x_bound, upper_x_bound + 1):
        y = m * x + b
        y_values.append(y)
    
    return y_values

def get_input(prompt):
    user_input = input(prompt)
    return user_input.strip()

def main():
    while True:
        m_input = get_input("Enter the slope (m) or type 'exit' to quit: ")
        if m_input.lower() == 'exit':
            break

        b_input = get_input("Enter the intercept (b) or type 'exit' to quit: ")
        if b_input.lower() == 'exit':
            break

        lower_x_input = get_input("Enter the lower bound for x or type 'exit' to quit: ")
        if lower_x_input.lower() == 'exit':
            break

        upper_x_input = get_input("Enter the upper bound for x or type 'exit' to quit: ")
        if upper_x_input.lower() == 'exit':
            break
        try:
            m = float(m_input) if '.' in m_input else int(m_input)
            b = float(b_input) if '.' in b_input else int(b_input)
            lower_x_bound = int(lower_x_input)
            upper_x_bound = int(upper_x_input)
            result = slope_intercept(m, b, lower_x_bound, upper_x_bound)
            if result is False:
                print("Invalid input or bounds. Please try again.")
            else:
                print(f"The resulting y values for x from {lower_x_bound} to {upper_x_bound} are: {result}")
        
        except ValueError:
            print("Invalid input. Please ensure you are entering numeric values for m, b, and x bounds.")
main()
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
# If the number you are trying to take the square root of is negative, return null
import math

def sqrt_safe(n):
    if n < 0:
        return None
    return math.sqrt(n)

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    
    root1 = (-b + sqrt_safe(discriminant)) / (2 * a)
    root2 = (-b - sqrt_safe(discriminant)) / (2 * a)
    
    return (root1, root2)

def get_input(prompt):
    user_input = input(prompt)
    return user_input.strip()

def main():
    while True:
        a_input = get_input("Enter the coefficient a (or type 'exit' to quit): ")
        if a_input.lower() == 'exit':
            break

        b_input = get_input("Enter the coefficient b (or type 'exit' to quit): ")
        if b_input.lower() == 'exit':
            break

        c_input = get_input("Enter the coefficient c (or type 'exit' to quit): ")
        if c_input.lower() == 'exit':
            break
        
        try:
            a = float(a_input) if '.' in a_input else int(a_input)
            b = float(b_input) if '.' in b_input else int(b_input)
            c = float(c_input) if '.' in c_input else int(c_input)

            result = quadratic_solver(a, b, c)
            
            if result is None:
                print("The discriminant is negative, so there are no real solutions.")
            else:
                root1, root2 = result
                print(f"The roots of the equation are: {root1} and {root2}")
        
        except ValueError:
            print("Invalid input. Please ensure you are entering numeric values for a, b, and c.")
main()