def add (x, y):
    return x + y

def subtraction (x, y):
    return x - y

def multiplication (x, y):
    return x * y

def division (x, y):
    return x / y

# Display the available operations
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

# user input
choice = input("Enter Choice (1/2/3/4): ")

num1 = float(input("Enter First Number: "))
num1 = float(input("Enter Second Number: ")) 

# Perform the selected operations using for loop
if choice in['1','2','3','4']:
    operations = [add,subtraction,multiplication,division]
    selected_operations = [int(choice) - 1]
    
    result =selected_operation(num1, num2)
    print("result:", result)
    print("invalid input")