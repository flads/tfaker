#!/usr/bin/env python3

import click
import pyperclip
import random

def generateCPF(separators):
    firstSet = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    secondSet = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    cpf = [random.randint(1, 9) for _ in range(9)]

    # Calculate first verifying digit
    firstResultSumValues = 0

    for x in range(len(cpf)):
        firstResultSumValues += cpf[x] * firstSet[x]

    firstVerifyingDigit = 11 - (11 if (firstResultSumValues % 11) < 2 else (firstResultSumValues % 11))

    cpf.append(firstVerifyingDigit)

    # Calculate second verifying digit
    secondResultSumValues = 0

    for x in range(len(cpf)):
        secondResultSumValues += cpf[x] * secondSet[x]

    secondVerifyingDigit = 11 - (11 if (secondResultSumValues % 11) < 2 else (secondResultSumValues % 11))

    cpf.append(secondVerifyingDigit)

    cpf = ''.join(str(x) for x in cpf)

    if (separators):
        cpf = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)

    pyperclip.copy(cpf)
    pyperclip.paste()

def generateCNPJ(separators):
    firstSet = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    secondSet = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    cnpj = [random.randint(1, 9) for _ in range(12)]

    # Calculate first verifying digit
    firstResultSumValues = 0

    for x in range(len(cnpj)):
        firstResultSumValues += cnpj[x] * firstSet[x]

    firstVerifyingDigit = 11 - (11 if (firstResultSumValues % 11) < 2 else (firstResultSumValues % 11))

    cnpj.append(firstVerifyingDigit)

    # Calculate second verifying digit
    secondResultSumValues = 0

    for x in range(len(cnpj)):
        secondResultSumValues += cnpj[x] * secondSet[x]

    secondVerifyingDigit = 11 - (11 if (secondResultSumValues % 11) < 2 else (secondResultSumValues % 11))

    cnpj.append(secondVerifyingDigit)

    cnpj = ''.join(str(x) for x in cnpj)

    if (separators):
        cnpj = '{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}'.format(*cnpj)

    pyperclip.copy(cnpj)
    pyperclip.paste()

@click.group()
def tf():
    pass

@click.command()
@click.option('--separators', '-s', is_flag=True)
def cpf(separators):
    generateCPF(separators)
    click.echo(click.style('CPF copied!', bg='green', fg='black'))

@click.command()
@click.option('--separators', '-s', is_flag=True)
def cnpj(separators):
    generateCNPJ(separators)
    click.echo(click.style('CNPJ copied!', bg='green', fg='black'))

tf.add_command(cpf)
tf.add_command(cnpj)

if __name__ == '__main__':
    tf()
