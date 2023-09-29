# Lab3
# Author: 

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.


number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 2. Write some code that asks the user for a number and prints out whether it is even or odd.

number2 = int(input("Enter a number: "))
if number2 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.

number3 = int(input("Enter a number: "))
i = 1
while i < number3:
    print(i)
    i += 1 # i = i + 1

# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.

sum_of_numbers = 0
for i in range(5):
    sum_of_numbers += float(input("Enter a number: "))
average = sum_of_numbers / 5
print("The average of the 5 numbers is:", average)


# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.

for number in range(1, 11):
    if number % 3 == 0 or number % 5 == 0:
        print(number)

# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".

number = int(input("Enter a number: "))
count = number
while count >= 1:
    print(count)
    count -= 1
print("Blast off!")

# 7. Write some code that asks the use for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.

number = int(input("Enter a number: "))

for value in range(1, number + 1):
    if value % 7 == 0:
        print('Lucky')
    if value > 100:
        break


