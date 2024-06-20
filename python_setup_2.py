#Section 1 - sets and tuples:
#Pre-Question: Take a look at this JavaScript Array:
# let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.

# What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

my_set = {12, 55, 33, 40, 55, 33, 20, 12}

# print(my_set)

#Question 1a: Create a set of your own with at least 3 different elements.
my_new_set = {1,2,3,4,5,6}
#Question 1b: Add an item to the set that you just created.
my_new_set.add(7)

#Question 1c: Print the set with the new data that you added to it:
print(my_new_set)

#Question 2a: Create a tuple with at least 3 elements inside of it.
new_tuple = ("red","white","blue")


#Question 2b: Print the tuple you just created.
print(new_tuple)



#Section 2 - loops:

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:

for day in days:
    print(day)


# Question 4: Loop through add_list and add each value to x. Print the value of x at each increment:
x = 10
add_list = [10, 6, 12, 4, 5]

for i in add_list:
    i += x
    print(i)



# Question 5: While Loops 

#Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:
iterator = 1
starting_value = 5

while iterator < 10:
    starting_value += 5
    print(starting_value)
    iterator +=1


#Section 3 - conditionals: if, elif, else statements

favorite_movie = "White Chicks"    
#Question 6a: Uncomment the favorite_movie variable above and change the value to the title of your favorite movie
#Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.

if favorite_movie == "White Chicks":
    print("That's a great movie")
    #Otherwise (else), print the string "that's not my favorite movie".  
else:
    print("that's not my favorite movie")

#Mess around with the value of the favorite_movie variable and trigger both conditional responses:



#Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list. 
#If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
#if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
#otherwise, just print the movie in the list:

movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

for item in movie_list:
    if item == "blueberries":
        print(f"{item} is a fruit...not a movie")
    elif item == "Toyota":
        print(f"{item} is a car...not a movie")
    else:
        print(item)


#BONUS - conditional and operators practice:
a = 5
b = 5
c = 12
#Question 7a: Use the correct operator to add variables a & c:
print(a+c)

#Question 7b: Use the correct operator to subtract variables b & c:
print(b-c)
#Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:

#Question 7d: Use the correct operator to find the quotient of variables c & a

#Question 7e: Use the correct operator to find if variables c & b are not equal to each other:


