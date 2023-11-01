def encode(pw):
    encoded = ""

    for i in range(len(pw)):
        add = int(pw[i]) + 3
        if (len(str(add))) > 1:
            add = str(add)[1]

        encoded += str(add)


    return encoded

def decode(pw):
    decoded = ""

    for i in range(len(pw)):
        sub = int(pw[i]) - 3
        if (sub) < 1:
            sub += 10

        decoded += str(sub)

    return decoded


def main():
    while True:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        op = int(input("Please enter an option: "))
        if op == 1:
            passy = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        if op == 2:
            print(f"The encoded password is {encode(pw)}, and the original password is {decode(encode(pw))}.\n")
        if op == 3:
            break

if __name__=='__main__':
    main()