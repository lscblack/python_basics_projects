# Develop a program that checks if a given word or phrase is a palindrome (reads the same forwards and backward).
original = list(input("Enter Any Word Or Numbers : "))
text_rev = original[::-1]
if original == text_rev:
    print("".join(original), " => Is Palindrome Got => ", "".join(text_rev))
else:
    print("".join(original), " => Is Not Palindrome Got =>  ", "".join(text_rev))
