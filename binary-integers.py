binary = ""
number = int(input("Give me a number :"))
while number > 0:
    binary = str(number % 2) + binary
    number = number // 2
print (binary)
    