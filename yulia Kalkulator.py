bil1 = int(input("Bil 1 = "))
opr = input("Operator (+, -, *, /, %) = ")
bil2 = int(input("Bil 2 = "))

if opr == "+":
    print(bil1, "+", bil2, "=", bil1 + bil2)
elif opr == "-":
    print(bil1, "-", bil2, "=", bil1 - bil2)
elif opr == "*":
    print(bil1, "x", bil2, "=", bil1 * bil2)
elif opr == "/":
    print(bil1, ":", bil2, "=", bil1 / bil2)
elif opr == "%":
    print(bil1, "%", bil2, "=", bil1 % bil2)
else:
    print("Operasi tidak tersedia, error! Pilih +, -, *, /, %")