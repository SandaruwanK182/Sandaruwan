class Converter:
    @staticmethod
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    @staticmethod
    def decimal_to_octal(decimal):
        return oct(decimal)[2:]

    @staticmethod
    def decimal_to_hexadecimal(decimal):
        return hex(decimal)[2:]

    @staticmethod
    def binary_to_decimal(binary):
        return int(binary, 2)

    @staticmethod
    def octal_to_decimal(octal):
        return int(octal, 8)

    @staticmethod
    def hexadecimal_to_decimal(hexadecimal):
        return int(hexadecimal, 16)

    @staticmethod
    def binary_to_octal(binary):
        decimal = Converter.binary_to_decimal(binary)
        return Converter.decimal_to_octal(decimal)

    @staticmethod
    def binary_to_hexadecimal(binary):
        decimal = Converter.binary_to_decimal(binary)
        return Converter.decimal_to_hexadecimal(decimal)

    @staticmethod
    def octal_to_binary(octal):
        decimal = Converter.octal_to_decimal(octal)
        return Converter.decimal_to_binary(decimal)

    @staticmethod
    def hexadecimal_to_binary(hexadecimal):
        decimal = Converter.hexadecimal_to_decimal(hexadecimal)
        return Converter.decimal_to_binary(decimal)

    @staticmethod
    def octal_to_hexadecimal(octal):
        decimal = Converter.octal_to_decimal(octal)
        return Converter.decimal_to_hexadecimal(decimal)

    @staticmethod
    def hexadecimal_to_octal(hexadecimal):
        decimal = Converter.hexadecimal_to_decimal(hexadecimal)
        return Converter.decimal_to_octal(decimal)
    

print ("\n SandaruwanK Number System Converter\n")
name = str(input("Enter Your  Name :"))
print("\nHi ", name ,"   Welcome to Our System ! \n")

def main():
    
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Binary to Octal")
    print("8. Binary to Hexadecimal")
    print("9. Octal to Binary")
    print("10. Hexadecimal to Binary")
    print("11. Octal to Hexadecimal")
    print("12. Hexadecimal to Octal")

    choice = int(input("\n Enter Your choice:\n "))

    if choice == 1:
        decimal_num = int(input("Enter Your Decimal Number: "))
        print("Your Binary Number is : ", Converter.decimal_to_binary(decimal_num))
    elif choice == 2:
        decimal_num = int(input("Enter Your Decimal Number: "))
        print("Your Octal Number is :  ", Converter.decimal_to_octal(decimal_num))
    elif choice == 3:
        decimal_num = int(input("Enter Your Decimal Number: "))
        print("Your Hexadecimal Number is :  ", Converter.decimal_to_hexadecimal(decimal_num))
    elif choice == 4:
        binary_num = input("Enter Your binary number: ")
        print("Your Decimal Number is :  ", Converter.binary_to_decimal(binary_num))
    elif choice == 5:
        octal_num = input("Enter Your octal number: ")
        print("Your Decimal Number is :  ", Converter.octal_to_decimal(octal_num))
    elif choice == 6:
        hexadecimal_num = input("Enter Your hexadecimal number: ")
        print("Your Decimal Number is :  ", Converter.hexadecimal_to_decimal(hexadecimal_num))
    elif choice == 7:
        binary_num = input("Enter Your binary number: ")
        print("Your Octal Number is :  ", Converter.binary_to_octal(binary_num))
    elif choice == 8:
        binary_num = input("Enter Your binary number: ")
        print("Your Hexadecimal Number is :  ", Converter.binary_to_hexadecimal(binary_num))
    elif choice == 9:
        octal_num = input("Enter Your octal number: ")
        print("Your Binary Number is : ", Converter.octal_to_binary(octal_num))
    elif choice == 10:
        hexadecimal_num = input("Enter Your hexadecimal number: ")
        print("Your Binary Number is :  ", Converter.hexadecimal_to_binary(hexadecimal_num))
    elif choice == 11:
        octal_num = input("Enter Your octal number: ")
        print("Your Hexadecimal Number is :  ", Converter.octal_to_hexadecimal(octal_num))
    elif choice == 12:
        hexadecimal_num = input("Enter Your hexadecimal number: ")
        print("Your Octal Number is :  ", Converter.hexadecimal_to_octal(hexadecimal_num))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()