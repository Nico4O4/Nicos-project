import os
import time

print("Shutdown system? y/n")

user_input = input(">> ")

while True:
    if user_input.lower() == "y":
        for timer in range(43, 0, -1):

            print(f"STATUS: {timer} ", end="\r")    

            time.sleep(1)

        os.system("shutdown /s")
        break

    elif user_input.lower() == "n":
            print("Shutdown fail - by user")
            time.sleep(2.1)
            break
            



    else:
        print("Shutdown Fail")
        user_input = input("-> ")


#coded by: Nico4O4