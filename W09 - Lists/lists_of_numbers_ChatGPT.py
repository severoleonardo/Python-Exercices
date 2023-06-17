numbers = []

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

# Compute the sum
total = sum(numbers)

# Compute the average
average = total / len(numbers)

# Find the maximum number
maximum = max(numbers)

print("Numbers entered:", numbers)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
