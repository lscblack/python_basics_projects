# Create a program that calculates the factorial of a number provided by the user.
num = int(input("Enter Any Integer Number : "))
fact = 1
# set loop range limit to entered number ex: if 5 then loop will give us 1 2 3 4 5
for x in range(1, num + 1):
    fact *= x

print(f"Factorial of {num} is {fact}")