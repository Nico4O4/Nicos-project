import json
import time

print("DB mini-text story | use 'DB' to search for files\n")
user = input(">> ")

if user == "DB".lower():
    try:
        with open("database.json", "r", encoding="utf-8") as first_var:
            main_var = json.load(first_var)
            print("Files found\n")
            print("Downloading files...")
            
            for show in range (0, 30, +5):
                print(f"Status:", show,"MBS", end="\r")
                time.sleep(2.5)

            print("\nDownload Complete. Open and print in Terminal? y/n")
            user = input(">> ")

            if user == "y".lower():
                with open("database.json", "r", encoding="utf-8") as file:
                    main_file = json.load(file)
                    print(f"--File Contents--\n", json.dumps(main_file, indent=2))

            else:
                ("Bye...")


    except:
        FileNotFoundError
        print("Files not found")

else:
    print("non existent command")

#made by Nico4O4