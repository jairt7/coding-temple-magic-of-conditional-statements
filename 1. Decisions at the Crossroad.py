#1. Desicions at the Crossroad
'''
Original code:

number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number = 0:
    print("The number is zero.")
else number < 0:
    print("The number is negative.")
'''

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
else:
    print('Invalid input.')