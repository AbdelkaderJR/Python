#	- write a program that prints hello world

print("hello world")

#	- application to take a number in binary form from the user, and print it as a decimal

bin_num = input("Enter binary number")
dec_num = int(bin_num,2)
print(dec_num)

"""
- write a function that takes a number as an argument and if the number
		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
		divisible by both return "FizzBuzz"  
"""

def div_num(num):
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return num

#- Ask the user to enter the radius of a circle print its calculated area and circumference

radius = float(input("Enter the radius of the circle"))
area = 3.14*(radius**2)
circumference = 2 * 3.14 * radius

print(area)
print(circumference)

#- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

name = input("Enter your name: ")
email = input("Enter your email: ")

if not name.strip().isalpha():
    print("Name must contain only letters.")
elif "@" not in email or "." not in email:
    print("Invalid email, Email must contain '@' and . ")
else:
    print("Name:", name)
    print("Email:", email)


#	- Write a program that prints the number of times the substring 'iti' occurs in a string

text = input("Enter a string: ")
count = text.count("iti")
print(count)
