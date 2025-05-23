#!/Users/shrikantkarve/opt/anaconda3/bin/python
import sys
import time

print("Helloo there!!! After a long time!!")

print("This program prints prime numbers till a number provided as input")

in_number = int(sys.argv[1])

print("Number provided is ",in_number)

primes = []
is_prime = True
# Add code to time the execution of the program
start_time = time.time()
# Add code to check if the input number is less than 2
if in_number < 2:
    print("Please provide a number greater than 1")
    sys.exit(1)

for i in range(2,int(in_number)+1):
    for factor in primes:
        if i%factor == 0:
            is_prime = False
    if is_prime == True:
        # print("Looks like ",i, "is prime")
        primes.append(i)
    is_prime = True
print("Time taken : ", time.time() - start_time)
print("The list of primes below ",in_number, " is ", primes)
