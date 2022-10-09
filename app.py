decimal_number = int (input("Enter a decimal number :"))
hex_number = hex(decimal_number).replace("0x","")
print("The octal value for {} is {}".format(decimal_number, hex_number ))

