# File Handling

import os

def main():
    directory = r"C:\PGDACC Section\Sem 2\Python"
    filename = input("\n enter file name: ")
    filepath = directory + filename
    print("filepath:", filepath)

    choice = 0
    print("\n Welcome to File Handling \n")

    while choice >= 0:
        print("1. create file")
        print("2. write file")
        print("3. append file")
        print("4. read file")
        print("5. delete file")
        print("-1. exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            f = open(filepath, "w")
            print("\n" + filename + "file Created")
            f.close()
            # break

        if choice == 2:
            message = input("\n write data into file: ")
            f = open(filepath, "w")
            f.write("\n" + message + "\n")
            f.close()
            # break

        if choice == 3:
            message = input("\n append data into file: ")
            f = open(filepath, "a")
            f.write("\n" + message + "\n")
            f.close()
            # break

        if choice == 4:
            f = open(filepath, "r")
            for x in f:
                print(x)
            f.close()
            # break

        if choice == 5:
            os.remove(filepath)


if __name__ == '__main__':
    main()

"""
output:

"""
