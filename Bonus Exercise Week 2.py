"""
Write a Python program that prints the numbers from 1 to 100.
If the number is dividable by 3 print Fizz, if the number is dividable by 5 print Buzz instead of the number.
If the number is dividable by 3 and 5 print FizzBuzz.
"""

l = [
    "FizzBuzz" if (i % 3 == 0 and i % 5 == 0)
    else "Fizz" if (i % 3 == 0)
    else "Buzz" if (i % 5 == 0)
    else i for i in range(1, 101)]
for i in l:
    print(i)