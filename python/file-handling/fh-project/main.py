from pathlib import Path
import os

def readfileandfolder():
    path = Path(__file__).parent
    items = list(path.rglob("*"))

    for i, file in enumerate(path.iterdir(), start=1):
        if file.is_file():
            print(f"{i}: {file.name}")

def createfile():
    try:
        readfileandfolder()

        name = input("please enter the name for the file: ")
        base_path = Path(__file__).parent   
        p = base_path / name

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)

            print("file created successfully!")
        else:
            print("this file already exists!")

    except Exception as err:
        print(f"an error occurred as {err}")

def readfile():
    try:
        readfileandfolder()

        name = input("which file you want to read: ")

        base_path = Path(__file__).parent   
        p = base_path / name

        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            
            print("file read successfully!")
        else:
            print("entered file doesn't exists!")
    
    except Exception as err:
        print(f"an error occurred as {err}")

def updatefile():
    try:
        readfileandfolder()

        name = input("enter the name of the file you want to update: ")

        base_path = Path(__file__).parent   
        p = base_path / name

        print(p)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file: ")
            print("press 2 for overwriting the data of your file: ")
            print("press 3 for appending some content in your file: ")

            res = int(input("enter your response: "))

            if res == 1:
                name2 = input("enter your new file name: ")
                p2 = base_path / name2
                p.rename(p2)
                print("file renamed successfully!")

            if res == 2:
                with open(p, "w") as fs:
                    data = input("tell what you want to write (this will overwrite the data): ")
                    fs.write(data)

            if res == 3:
                with open(p, "a") as fs:
                    data = input("enter what you want to append: ")
                    fs.write(" "+data)
     
    except Exception as err:
        print(f"an error occurred as {err}")

def deletefile():
    try:
        readfileandfolder()

        name = input("enter the file name you want to delete: ")
        base_path = Path(__file__).parent   
        p = base_path / name

        if p.exists() and p.is_file():
            os.remove(p)

            print("file removed successfully!")
        else:
            print("no such file exists!")

    except Exception as err:
        print(f"an error occurred as {err}")


print("press 1 for creating a file: ")
print("press 2 for reading a file: ")
print("press 3 for updating a file: ")
print("press 4 for deleting a file: ")

check = int(input("please tell what you want to do: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()