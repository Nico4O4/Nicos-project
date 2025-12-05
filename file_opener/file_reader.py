import pyinputplus as pyip
import sys


def file_reader():
    user_input_file_path = pyip.inputFilepath(prompt="Path to file >> ", mustExist=True)
    
    try:
        file = open(user_input_file_path, "r")
        print("\n--Current file content--", "\n\n", file.read(), "\n\n")
        menu()
    
    except:
        FileNotFoundError
        print("File not found")
        menu()


#first menu when starting programm
def menu():
    while True:
        print("\nFile reader | made by Nico4O4")
        print("'r' | read a file via path")
        print("'q' | Exit")

        user_input1 = input("--> ")
        
        if user_input1 == "r".lower():
            file_reader()
            break

        if user_input1 == "q".lower():
            sys.exit()

        else:
            print("Invalid input\n")
            menu()
        
menu()