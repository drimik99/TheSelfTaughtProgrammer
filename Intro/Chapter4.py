# simple statement is just a line of code
# compound statement are made up of one more clauses
  # a clause consists of two or more lines of code: a header followed by a suite(s)
    # a header is a line of code in a clause that contains a keyword, followed by a colon 
    # a sequence of one or more lines of indented code
    
    #in for statements like

  for i in range(10):
    print("hello")

    # for i in range(10) is the header and it has one suite which is print("hello")
      # header controls the suites whereas suite is just a line of code in a clause


# CHAPTER 4: FUNCTIONS
# compound statements that can take in input, execute a body of code and return an output
 
age = input("Enter your age: ")
int_age = int(age)

if age > 21:
  print("You are young!")
else:
  print("You are old!")


# Required and Optional Parameters
  # when user calls a funnction, they must pass the required parameters into it 
  # or Python will raise an exception
  # optional parameters: [function_name] ([parameter_name] = [parameter_value])


# scope --> same as C++
# if you want to modify a global variable inside a local scope, must do "global" 
# [variable_name] to declare it within the scope

# exception handling
  # use keywords "try" and "except" when your code may raise an exception
    # the try clause contains the error could occur
    # the except clause contains the code that will execute if the exception in your try clause occurs

#example
a = input("enter your favorite number: ")
a = float(a)
b = input("enter another number: ")
b = float(b)
    
try:
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Invalid Input.")

# ValueError --> occurs if you give the built in functions - int, string, float - bad input

# DocStrings
  # these are comments left at the top of a function explaining what data type each parameter needs to be 
  # they explain what the function does 
  # example

def add(x,y):
  """
  Returns x + y
  :param x: int
  :param y: int
  :return: int sum of x and y
  """
  return x + y

