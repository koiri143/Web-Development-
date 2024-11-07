# Print a greeting from Helsinki
print("Hello from helsinki!")

# Print a generic hello world message
print("Hello world!")

# Print a message indicating this is the first program
print("This is my first program.")

# Print a message about the purpose of the program
print("This program prints three lines of text")

# Print a line with quotes inside the text
print('He said: "Hello world!" and kept on coding.')
from collections.abc import Sequence


print("Welcome!")#this is comment
print("He said: \"Hello world!\" and kept on coding.")

# Print a greeting by concatenating  strings
print("Hello " + "anil!")

# Ask the use for their name and store it in a variable 
input("What is your name? ")

# Prompt the user for their name again and with a concatenated string
print("Welcome " + input("What is your name? ") + "!")

# Print the first character of the string "Hello"
print("Hello"[0])

# Print the first two characters of the string "Hello" using slicing
print("Hello"[0:2])

# Concatenate the strings "123" and "456" and print the result
print("123" + "456")




#  = "Finding a substring."

# Print the entire string
print(Sequence)

# Print the character at index 2 (the third character, 'n')
print(Sequence[2])

# Print the character at index -2 (the second-to-last character, 'i')
print(Sequence[-2])

# Print the substring from index 2 to index 9 (not inclusive), which is "nding a "
print(Sequence[2:9])

# Print the substring from the start to index 9 (not inclusive), which is "Finding a"
print(Sequence[:9])

# Print the substring from index -1 to index -2 (not inclusive), which is "substri"
print(Sequence[-1:-2])

# Print every third character from index 2 to 9, which is "ni" (at indices 2, 5, and 8)
print(Sequence[2:9:3])

# Print every third character of the entire string, w "Fia b."
print(Sequence[::3])

# Print the string in reverse order
print(Sequence[::-1])# Adding two integers
print(123 + 456)  # Output: 579 (int)

# Printing a large integer using underscores for readability
print(123_456_789)
# Output: 123456789 (int)

# Printing a floating-point number
print(3.14)
# Output: 3.14 (float)

# Printing a boolean value represent True
print(True)
# Output: True (bool)

# Calculate the length of the string .Calculate the number of characters.
CalcLen = len("Calculate the number of characters")  
# Print the type of the variable CalcLen (should be int since len() returns an integer)
print(type(CalcLen))

# Convert the integer 50 to a float and assign it to Num1
Num1 = float(50)  
# Print the type of the variable Num1 (should be float)
print(type(Num1))

# Convert the string "90" to an integer and assign it to Num2
Num2 = int("90")  
# Calculate Num3 by adding 90 and Num8, and assign the result to Num3
Num3 = 90 + Num8   # type: ignore
# Print the value of Num3
print(Num3)

# Concatenate the string representation of Num8 and Num3 and print the result
print(str(Num1) + str(Num3))



# The order of multiplication and division first, then addition and subtraction
print(5 * 3 - 4 / 2 + 2)  
# Calculation: (15 - 2 + 2) = 15

# Parentheses change the order of operations, so (2 + 2) is calculated first
print(5 * 3 - 4 / (2 + 2))  
# Calculation: (15 - 1) = 14

# The difference between the two expressions:
# The first expression evaluates to 15, while the second evaluates to 14 due to the parentheses affecting the division.

# Print the result of dividing 8 by 3
print(8 / 3)  
# This will output a float: approximately 2.6666666666666665

# Convert the result of 8 / 3 to an integer, truncating the decimal part
print(int(8 / 3))  
# This will output: 2

# Round the result of 8 / 3 to the nearest integer.
print(round(8 / 3))  
# This will output: 3

# Round the result of 8 / 3 to 2 decimal places.
print(round(8 / 3, 2))  
# This will output: 2.67
  

# Assign a name and age to variables
Name = "anil"
Age = 24

# Print the formatted string
print(FormattedString) # type: ignore

 
print("Warning! The temperature is too high!")

print("Everything cool! Keep on going :)")


print("The CPU is fried. Get your fire extinguisher.")

print("Warning! The temperature is too high!")

print("Everything cool! Keep on going :)")                          



first_name = ("anil: ")
second_name = ("koiri: ")

print(first_name + " is longer than " + second_name + ".")
print(first_name + " and " + second_name + " are of equal length.")

x = 4
print(x < 5 and x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))

Town = "Lahti"
Street = "Mukkulankatu"
Building = 19

if Town == "Lahti" and Street == "Mukkulankatu" and Building == 19:
    print("You are at LAB!")
elif Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19):
    print("You are in the correct town, but you need to check your address.")
elif Building > 19:
    print("You went too far.")
elif Building < 19:
    print("You are not there yet.")
else:
    print("You are completely lost...")



num4 = (5, 10)
num2 = (6, 10)
num3 = (8, 10)

print(":", num4, num2, num3)

if num4 <= num4 and num4 <= num3:
    smallest = num4
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num4 and num2 <= num3:
    smallest = num2
    if num4 <= num3:
        middle = num4
        largest = num3
    else:
        middle = num3
        largest = num4
else:
    smallest = num3
    if num4 <= num2:
        middle = num4
        largest = num2
    else:
        middle = num2
        largest = num4

print("Numbers in order:", smallest, middle, largest)




print("n:", )

user_name = input("anil: ")
print("The letter '" + random_letter + "' was found in your name '" + user_name + "'.") # type: ignore
print("The letter '" + random_letter + "' was not found in your name '" + user_name + "'.") # type: ignore

print("welcome to this  resturant")
print("Select from the list:")
print("1. Login")
print("2. Go to settings")
print("3. Logout")

user_input = input("menu: ")

if user_input == "5":
    print("anil")
elif user_input == "6":
    print("Settings")
elif user_input == "3":
    print("koiri")
else:
    print("menu")


print("welcome to this  resturant")
print("Select from the list:")
print("1. Login")
print("2. Go to settings")
print("3. Logout")

user_input = input("menu: ")

if user_input == "5":
    print("anil")
elif user_input == "6":
    print("Settings")
elif user_input == "3":
    print("koiri")
else:
    print("menu")


    







 





