
def main():
    try:
        number = int(input("enter the input number:"))
        output = number / 0
        print("output:", output)

    except:
        #output = number * 0
        #print(output)
        print("divide by zero is not allowed.....")

if __name__ == '__main__':
    main()
