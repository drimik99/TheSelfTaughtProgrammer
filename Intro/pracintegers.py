a = input("enter your favorite number: ")
a = float(a)
b = input("enter another number: ")
b = float(b)
    
try:
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Invalid Input.")


