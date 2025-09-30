def hex_char_decode(digit):
    if digit.upper() == "A":
        return 10
    elif digit.upper() == "B":
        return 11
    elif digit.upper() == "C":
        return 12
    elif digit.upper() == "D":
        return 13
    elif digit.upper() == "E":
        return 14
    elif digit.upper() == "F":
        return 15
    else:
        return int(digit)

def hex_string_decode(hex):
    sum = 0
    if "0x" in hex:
        hex = hex[2:]
    counter = len(hex) - 1
    for h in hex:
        sum += hex_char_decode(h) * 16**counter
        counter -= 1
    return sum

def binary_string_decode(binary):
    sum = 0
    if "0b" in binary:
        binary = binary[2:]
    counter = len(binary) - 1
    for b in binary:
        if int(b) == 1:
            sum += 2**counter
        counter -= 1
    return sum

def binary_to_hex(binary):
    decimal = binary_string_decode(binary)
    hex = ""
    for i in range(len(str(decimal))):
        place = decimal % 16
        decimal //= 16
        if place in range(10,16):
            if place == 10:
                hex += "A"
            elif place == 11:
                hex += "B"
            elif place == 12:
                hex += "C"
            elif place == 13:
                hex += "D"
            elif place == 14:
                hex += "E"
            elif place == 15:
                hex += "F"
        else:
            hex += str(place)

    #reverse order
    newhex = ""
    for letter in range(len(hex)-1, -1, -1):
        if hex[letter] == "0":
            if newhex == "":
                continue

        newhex += hex[letter]

    return newhex

loop = True

while loop:
    print("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
    option = input("Please enter an option: ")
    if option == "4":
        print("Goodbye!")
        break
    else:
        number = input("Please enter the numeric string to convert: ")
        if option == "1":
            result = hex_string_decode(number)
        elif option == "2":
            result = binary_string_decode(number)
        elif option == "3":
            result = binary_to_hex(number)
        print(f"Result: {result}\n")
