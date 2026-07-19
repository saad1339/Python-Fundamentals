# Task 1: Print your name, roll number, and class in a box format using print statements.

print ("********************************");
print ("*  Superior University         *");
print ("*  Muhammad Saad Qayyum        *");
print ("*  Roll No: SU92-BSITM-F24-213 *");
print ("*  class    BSITM-F24          *");
print ("********************************");


#Task 2: Take input from user for first name and last name and print it in a single line.

name = input("Enter your First Name : ")
last_name = input("Enter your Last Name : ")
print ("Hello", name , last_name)


# Task 3: Take input from user for a character and print its ASCII value.

char = input("Enter a character : ")
print ("The ASCII value of", char, "is", ord(char))



# Task 4: Take input from user for three numbers and print their sum, multiplication, and division.

First_number = int (input("Enter first Number : "))
second_number = int (input("Enter second Number : "))
third_number = int (input("Enter third Number : "))

sum = First_number + second_number + third_number
print ("The sum of", First_number, second_number, third_number, "is", sum)

multiplication = First_number * second_number * third_number
print ("The multiplication of", First_number, second_number, third_number, "is", multiplication)

division = First_number / second_number / third_number
print ("The division of", First_number, second_number, third_number, "is", division)


#  Task 5: program that takes two numbers from the user and swap them without using third 
#variable.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
a = a + b
b = a - b
a = a - b

print ("After swapping, first number is", a, "and second number is", b)

#Task 6: You are making a program for a bus service. A bus can transport 50 passengers at once. Given the 
#number of passengers waiting in the bus station as input, you need to calculate and output how many 
#empty seats  the last bus will have. For example, the input is 126 passengers. The first bus will leave 
#126-50 = 76 passengers in the station. The next one will leave 26 in the station, thus, the last bus will 
#take all of the 26 passengers, have 50-26 = 24 seats left empty. '''


total_passengers = int(input("Enter the total number of passengers: "))

remaining = total_passengers % 50

if remaining == 0:
    empty_seats = 0
else:
    empty_seats = 50 - remaining

print("The seats left in last bus is:", empty_seats)

#Task 7:# Electricity Bill Calculator

units1 = int(input("Enter units for first 100-unit category: "))
units2 = int(input("Enter units for next 100-unit category: "))
units3 = int(input("Enter units above 200 category: "))

bill = (units1 * 10) + (units2 * 15) + (units3 * 20)

print("Total Electricity Bill:", bill, "PKR")



