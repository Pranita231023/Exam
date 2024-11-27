num = int(input("Enter a number: "))
factorial = 1 if num == 0 else num
for i in range(1, num):
    factorial *= i
print(f"Factorial of {num} is {factorial}.")
