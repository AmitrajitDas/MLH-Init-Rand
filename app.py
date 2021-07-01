
import random

# user input
n = int(input("Enter number of elements : "))

lst = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", lst)

print(random.choice(lst))
