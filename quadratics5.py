#Quadratics5.py
#Deeshai Escoffery
#03/19/2015

import math

def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        message = "Please enter the coeffecients (a,b,c): "
        a, b, c = eval(input(message))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError:
        print("\nThere are no real roots")
    except ZeroDivisionError:
        print("\nThe coeffecient must be non-zero.")
    except NameError:
        print("\nThe coeffecients must be numeric.")
    except TypeError:
        print("\nThe coeffecients must be numeric.")
    except SyntaxError:
        print("\nI have no idea what went wrong!!!")
        print("\nTry using a comma between each number!!!")

main()
