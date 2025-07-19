import string
import random

def multiplePass(length):
    allChar=string.ascii_letters+string.digits+string.punctuation
    newPass=''.join(random.choice(allChar) for _ in range(length))
    return newPass

try:
    passLength=int(input('Please enter pass length: '))
    totalPass=int(input('Please enter how many pass to be generated: '))
    if passLength<4:
        print('Pass length must be more than 4')
    else:
        print('\nGenerated password:')
        for i in range(totalPass):
            print(f"{i+1}: ",multiplePass(passLength))
except Exception:
    print('something went wrong')

def multiplePass(length):
    upper=random.choice(string.ascii_uppercase)
    lower=random.choice(string.ascii_lowercase)
    symbol=random.choice(string.punctuation)
    digits=random.choice(string.digits)

    password=[upper, lower, digits, symbol]

    print(f"upper:  {upper}")
    print(f"lower:  {lower}")
    print(f"symbol:  {symbol}")
    print(f"digits:  {digits}")
    print(f'created stock pass is: ', password)

    allChar=string.ascii_letters+string.digits+string.punctuation
    for _ in range(length-4):
        passWithExistingChar=random.choice(allChar)
        password.append(passWithExistingChar)

        print(f'added -→ {passWithExistingChar} ={password}')

    print(f'\nbefore shuffle: {password}')
    random.shuffle(password)
    print(f'\nafter shuffle: {password}')
    finalPass=''.join(password)
    print(f'final password: {finalPass}')

multiplePass(10)


#..........................create multiple pass and save it to lalmohan.txt file........................

import string
import random

def createPass(length):
    upper=random.choice(string.ascii_uppercase)
    lower=random.choice(string.ascii_lowercase)
    digits=random.choice(string.digits)
    symbol=random.choice(string.punctuation)

    password=[upper, lower, digits, symbol]

    char=string.digits+string.ascii_letters+string.punctuation
    for _ in range(length-4):
        password+=random.choice(char)

    finalPass=''.join(password)
    return finalPass

passLength=int(input('Please enter pass length: '))
totalPass=int(input('please input how many pass you want: '))
if passLength<8:
    print('\nPass length must be more than 8')

with open('lalmohan.txt', 'w') as file:
    for i in range(totalPass):
        newPass=createPass(passLength)
        file.write(f'{newPass}\n')
    print('\nPass is saved successfully in lalmohan.txt file\n')


#this is a simple comments
