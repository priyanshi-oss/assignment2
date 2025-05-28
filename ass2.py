

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")



total = 0

for i in range(1, 51):
    total += i

print("Sum of integers from 1 to 50 is:", total)

