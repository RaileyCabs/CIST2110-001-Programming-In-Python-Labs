# Lab6
# Author: Bodhi Fox


## add in functions from test.py's test statements here to make the pytest work


def calculate_rectangle_area(width:float,height:float)->float:
    return width*height


def calculate_hypotenuse(side_a:float, side_b:float)->float:
    return(side_a**2 + side_b**2)**.5

def is_even(number: int)->bool:
    if number % 2==0:
        return True
    else:
        return False

def find_maximum(number1: float, number2: float)->float:
    if number1>number2:
        return number1
    else:
        return number2
    

def grade_calculator(score: float)->str:
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid Score"

def main():
    pass



if __name__ == "__main__":
    main()
