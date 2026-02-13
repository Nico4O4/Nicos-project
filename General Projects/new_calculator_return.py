def calculator_plus(first_input, second_input):
    return print(first_input + second_input)

#hard coded: only fill variables with arguments (arguments = values like user inputs)
#defs are like machines they do something directly with the given value

def calculator_minus(user1, user2):
    return print(user1 - user2)

def calculator_multiplication(user1, user2):
    return print(user1 * user2)

def calculator_division(user1, user2):
    return print(user1 / user2)



asci = """
--Return Calculator by: Nico4O4--

Choose an operation...
---------------------------------
1 = (+)
2 = (-)
3 = (*)
4 = (/)
"""
print(asci)

user0 = int(input(">> "))

if user0 == 1:
    input1 = int(input("First Number >> "))
    input2 = int(input("First Number >> "))

    result = calculator_plus(input1, input2)

if user0 == 2:
    input1 = int(input("First Number >> "))
    input2 = int(input("First Number >> "))

    result = calculator_minus(input1, input2)

if user0 == 3:
    input1 = int(input("First Number >> "))
    input2 = int(input("Second Number >> "))

    result = calculator_multiplication(input1, input2)

if user0 == 4:
    input1 = int(input("First Number >> "))
    input2 = int(input("Second Number >> "))

    result = calculator_division(input1, input2)

#coded by: nico4o4