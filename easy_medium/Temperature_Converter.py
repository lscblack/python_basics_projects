# Build a program that can convert temperatures between Celsius and Fahrenheit.

def celsius(temperature):
    celsius2 = (temp - 32) * 5 / 9
    return celsius2


def fahrenheit(temperature):
    fahrenheit2 = temp * 9 / 5 + 32
    return fahrenheit2


while True:
    temp = input("Enter Temperature : ")
    if temp.isnumeric():
        to_ = input("\n1) To Celsius.\n2) Fahrenheit.\nq) To Stop \nEnter Your Choice : \n")
        if to_ == "1":
            print(celsius(temperature=float(temp)))
        elif to_ == "2":
            print(fahrenheit(temperature=float(temp)))
        elif to_.lower() == "q":
            print("\033[32m Tanks For Using Our App.\033[0m")
            break
        else:
            print("\033[31m Enter Valid Choice. \033[0m")
    elif temp.lower() == "q":
        print("\033[32m Tanks For Using Our App.\033[0m")
        break
    else:
        print("\033[31m Only Number Allowed \033[0m")