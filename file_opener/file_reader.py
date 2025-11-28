import pyinputplus as pyip

print("File opener from Nico4O4")
print("\nInsert path to check content")

user_input_file_path = pyip.inputFilepath(prompt=">> ", mustExist=True)


try:
    file = open(user_input_file_path, "r")
    print("\n--Current file content--\n", file.read())

except:
    FileNotFoundError
    print("File not found")


