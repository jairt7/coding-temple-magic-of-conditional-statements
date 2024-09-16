# 2. The Greatest Showdown

# Task 1: Identify the Greatest
# Write a Python program that asks the user to enter three numbers.
# Your code should then identify and print out the largest number among the three.
numUno = int(input("Enter the first number: "))
numDos = int(input("Enter the second number: "))
numTres = int(input("Enter the third number: "))
print()
'''
if numUno > numDos:
    if numUno > numTres:
        print("The largest number is", numUno)
    else:
        print("The largest number is", numTres)
elif numDos > numTres:
    print("The largest number is", numDos)
else:
    print("The largest number is", numTres)
'''
# Task 2: Identify the Smallest
# Improve upon your code from Task 1 to also determine the smallest number
# among the three and print it out.
# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that
# "The smallest number is 3. The largest number is 4. "
if numUno > numDos:
    if numUno > numTres:
        if numDos > numTres:
            print("The smallest number is", str(numTres) + ". The largest number is", str(numUno) + ". ")
        else:
            print("The smallest number is", str(numDos) + ". The largest number is", str(numUno) + ". ")
    else:
        print("The smallest number is", str(numDos) + ". The largest number is", str(numTres) + ". ")
elif numDos > numTres:
    if numUno > numTres:
        print("The smallest number is", str(numTres) + ". The largest number is", str(numDos) + ". ")
    else:
        print("The smallest number is", str(numUno) + ". The largest number is", str(numDos) + ". ")
else:
    print("The smallest number is", str(numUno) + ". The largest number is", str(numTres) + ". ")