def calculator_plus(user1, user2):
    return print(user1 + user2)

#hard coded: only fill variables with arguments (arguments = values like user inputs)

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
    user1 = int(input("First Number >> "))
    user2 = int(input("First Number >> "))

    result = calculator_plus(user1, user2)
    
if user0 == 2:
    user1 = int(input("First Number >> "))
    user2 = int(input("First Number >> "))

    result = calculator_minus(user1, user2)

if user0 == 3:
    user1 = int(input("First Number >> "))
    user2 = int(input("Second Number >> "))

    result = calculator_multiplication(user1, user1)

if user0 == 4:
    user1 = int(input("First Number >> "))
    user2 = int(input("Second Number >> "))

    result = calculator_division(user1, user2)

