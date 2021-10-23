#!/usr/bin/env python3

import click
import pyperclip
import random
import secrets
import string
from uuid import uuid4

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

    return cpf

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

    return cnpj

def generatePassword():
    alphabet = string.ascii_letters + string.digits + '!@#$%()[]~_-'
    password = ''.join(secrets.choice(alphabet) for i in range(20))

    pyperclip.copy(password)
    pyperclip.paste()

    return password;

def generateUuid():
    uuid = str(uuid4())

    pyperclip.copy(uuid)
    pyperclip.paste()

    return uuid;

@click.group()
def tf():
    pass

@click.command()
@click.option('--separators', '-s', is_flag=True)
def cpf(separators):
    cpf = generateCPF(separators)
    click.echo(cpf)
    click.echo(click.style(' Copied! ', bg='green', fg='black'))

@click.command()
@click.option('--separators', '-s', is_flag=True)
def cnpj(separators):
    cnpj = generateCNPJ(separators)
    click.echo(cnpj)
    click.echo(click.style(' Copied! ', bg='green', fg='black'))

@click.command()
def password():
    password = generatePassword()
    click.echo(password)
    click.echo(click.style(' Copied! ', bg='green', fg='black'))

@click.command()
def uuid():
    uuid = generateUuid()
    click.echo(uuid)
    click.echo(click.style(' Copied! ', bg='green', fg='black'))

tf.add_command(cpf)
tf.add_command(cnpj)
tf.add_command(password)
tf.add_command(uuid)

if __name__ == '__main__':
    tf()
