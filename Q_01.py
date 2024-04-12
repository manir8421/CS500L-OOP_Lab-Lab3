
# 20099_Maniruzzaman_Md_lab3
# Week_03/lab_03/Q_01
# Question: program  to enter an integer and displays its corresponding hex number ...


def dec_hex(dec_val):
    hex_dig = "0123456789ABCDEF"
    hex_result = ""

    while dec_val > 0:
        rem = dec_val % 16
        hex_result = hex_dig[rem] + hex_result
        dec_val //= 16

    return hex_result

def main():
    print("===== Decimal Number to Hexadecimal Number Converter =====")

    dec_input = input("Enter the decimal value (Do not enter negative value): ")

    while not dec_input.isdigit():
        print("Invalid input value. Please enter the valid integer value.")
        dec_input = input("Enter the decimal value (Do not enter negative value): ")

    dec_input = int(dec_input)

    while dec_input >= 0:
        hex_result = dec_hex(dec_input)
        print(f"The hexadecimal value is: {hex_result.upper()}")

        dec_input = input("Enter the decimal value (Do not enter negative value): ")

        while not dec_input.isdigit():
            print("Invalid input value. Please enter the valid integer value.")
            dec_input = input("Enter the decimal value (Do not enter negative value): ")

        dec_input = int(dec_input)

    print("Exiting the program.")

if __name__ == "__main__":
    main()
