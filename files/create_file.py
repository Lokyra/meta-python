try:
    with open('newfile.txt', 'w') as file:
        file.write("This is a new file created !\n") 
        file.writelines(["Hello World\n", "We're on planet python !"])
except FileNotFoundError as e:
    print("ERROR", e)

