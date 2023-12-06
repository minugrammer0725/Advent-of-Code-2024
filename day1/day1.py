sum = 0

with open("input.txt") as input:
    for line in input:
        firstDigit = ""
        lastDigit = ""
        for char in line:
            if char.isdigit():
                if firstDigit == "":
                    firstDigit = char
                else:
                    lastDigit = char
        digit = int(firstDigit + firstDigit) if lastDigit == "" else int(firstDigit + lastDigit)
        sum += digit

print(sum)
