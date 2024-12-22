def encode(pw):
    encoded = ""

    for i in range(len(pw)):
        add = int(pw[i]) + 3
        if (len(str(add))) > 1:
            add = str(add)[1]

        encoded += str(add)


    return encoded

def decode(password):
    decoded_pass = '' #Empty string

    for i in range(len(password)): #Goes through every number in the range of the password
        sub_three = int(password[i]) - 3 #Subtracts 3 from the digit stored in i
        if (sub_three) < 1:
            sub_three += 10 #If the result of the subtraction is negative, it adds ten to it

        decoded_pass += str(sub_three) #Adds the result to the empty variable

    return decoded_pass


def main():
    # hi
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