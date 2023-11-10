# Build a simple calculator program that can perform basic operations like addition, subtraction, multiplication, and division.
def calculate(num):
    try:
        result = eval(num)
    except Exception as e:
        return f"Error Happened {e}"
    else:
        return result


while(True):
    data = input("Enter Your Numbers And Sign Dont Start With Sign Format Ex: 3+4-1/2*3 : \n ('q' to close app) \n")
    if data.lower() =="q":
        break
        print("Thanks For Using Our App")
    else:
        print("result of ",data," = ",calculate(num=data))