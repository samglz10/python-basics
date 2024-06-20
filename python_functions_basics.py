# Function Definition Practice:
# Define functions according to the following prompts.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
     print('hello')
     return
say_hello()
# 2. a 'sum' function that accepts two integers and returns the sum.

def sum(int1, int2):
     return print(int1 + int2)
sum(1,2)

# 3. an 'average' function that accepts two numbers and returns the average.
def average(num1, num2):
     return print((num1 + num2)/ 2)
average(8,2)

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def last_first_name(first, last):
     return print(f"{last}, {first}")
last_first_name('Lady','Gaga')

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.

def student_list(first_name, last_name, graduation_year, student_number):
     return print([first_name,last_name,graduation_year, student_number])
student_list("Samuel", "Gonzalez", "2017", "50001234")

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def above_18(age):
    if age >= 18:
        return print(True)
    else:
         print(False)
above_18(19)
#7. A function that accepts a string and prints the string in reverse (no return value).
    #<object_name>[<start_index>, <stop_index>, <step>]
def reversed_string(str):
    return print(f"{str[::-1]}")
reversed_string("RaceCar")