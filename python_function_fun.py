"""Python Function Fun: Part 2 Prompts
Please complete the following functions.
"""

#arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for i in args:
        print(i)
#arb_args('anne', 'trevor', 'eli', 'marcus')

#inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed.

def inner_func(int1, int2):
    def add_ints(int1, int2):
        addition = int1 + int2
        print(addition)
    def substract_ints(int1, int2):
        subtraction = int1 - int2
        print(subtraction)
    return add_ints(int1,int2), substract_ints(int1, int2)

inner_func(5,2)


#lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. 
# If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(str1, str2="Mystery Meat"):
    if(str2 is None):
        print(f"{str1} would like Mystery Meat")
    else:
        print(f"{str1} would like {str2}")
#lunch_lady("Sammy", "Pizza")

#sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(int1, int2):
    sum = int1 +int2
    product = int1 * int2
    return print(sum, product)
#sum_n_product(10,15)


#alias_arb_args - Should be arb_args but assigned an alias. Remember, variables cann hold functions i Python just like they can in JS. 
# Alternatively, you can call a function from inside another function.

def arb_args(str):
    print(f"This is the original function.{str}")

#alias_function = arb_args
#alias_function("Calling this function using alias")  # This will call original_function

#arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*nums):
    total= 0
    for num in nums:
        total += num
    mean = total / len(nums)  
    return print(mean)

arb_mean(1,2,3,4,5,6,7,8)

#arb_longest_string - Accepts any number of strings and returns the longest one.

def longest_string(*strings):
    longest = ''
    for str in strings:
        if(len(str) > len(longest)):
            longest = str
    return print(f"The longest string is {longest}")
       
longest_string('str1', 'str1214', 'str234', 'str23')