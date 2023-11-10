# Design a number guessing game where the computer randomly selects a number, and the user has to guess it within a limited number of attempts.
import  random
def guess_me(prompt, guess):
    if prompt == guess:
        return "Correct You have Passed"
    else:
        return "Incorrect Try Again"


guess = random.randint(1,5)
d = 0
while True:
    prompt = int(input(f"Enter Your Guess Range(1-10) left {4-d}/4 : "))
    if guess_me(prompt=prompt, guess=guess) == "Correct You have Passed":
        print("\033[32m\U0001F604\033[0m", guess_me(prompt=prompt, guess=guess), "\033[32m✓\033[0m ")
        break
    else:
        print("\033[31m\U0001F602\033[0m",guess_me(prompt=prompt, guess=guess), " \033[31mX\033[0m")
    if d == 3:
        print("End Of Your Tail")
        break
    else:
        d += 1
