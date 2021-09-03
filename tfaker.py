#!/usr/bin/env python3
import pyperclip
import random

def generateCNPJ():
    firstSet = [5 ,4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    secondSet = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    cnpj = [random.randint(1, 9) for _ in range(12)]

    # Calculate first verifying digit
    firstResult = []

    for x in range(len(cnpj)):
        firstResult.append(cnpj[x] * firstSet[x])

    firstResultSumValues = 0
    for x in range(len(firstResult)):
        firstResultSumValues += firstResult[x]

    firstVerifyingDigit = 11 - (11 if (firstResultSumValues % 11) < 2 else (firstResultSumValues % 11))

    cnpj.append(firstVerifyingDigit)

    # Calculate second verifying digit
    secondResult = []

    for x in range(len(cnpj)):
        secondResult.append(cnpj[x] * secondSet[x])

    secondResultSumValues = 0
    for x in range(len(secondResult)):
        secondResultSumValues += secondResult[x]

    secondVerifyingDigit = 11 - (11 if (secondResultSumValues % 11) < 2 else (secondResultSumValues % 11))

    cnpj.append(secondVerifyingDigit)

    cnpj = ''.join(str(x) for x in cnpj)

    pyperclip.copy(cnpj)
    pyperclip.paste()

    print('CNPJ copied!')

if __name__ == '__main__':
    generateCNPJ()
