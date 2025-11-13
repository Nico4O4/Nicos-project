file_var = open("my_file.txt", "rt")

print("CURRENT CONTENT:\n", file_var.read())

print("\nAdd new content? y / any button to decline")

usr_input = input(">>")


if usr_input == "y":
    try:
        file_extra = open("my_file.txt", "a")
        file_extra.write("\nMeow!\n")
        print("New Content added into the file!")
    except:
        print("Content Error")

else:
    print("No changes made to the file")

print("\nShow content? y / any button to decline")
usr_input = input(">>")


if usr_input == ("y"):
    try:
        file_extra = open("my_file.txt", "rt") #1 parameter file 2 parameter modul rt = read, text format (r würde auch reichen)
        print("Content after change:", file_extra.read())
    except:
        print("Error showing content")

