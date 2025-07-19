import string
import random
# print(string.ascii_letters)
# print(string.digits)
# print(len(string.punctuation))
 
# print(' '.join(string.ascii_letters))
# p=(random.choice(string.ascii_letters))
# print('p:',p)
# print('type:',type(p))
# letter=(''.join(random.choice(string.ascii_letters)))
# print(letter)
# print(type(letter))
# all_chars = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(all_chars) for _ in range(10))
# Password = ''.join(random.choice(all_chars) for _ in range(20))
# # print(password)

# print('password:',Password)

def createPass(length):
    allLetters=string.ascii_letters+string.digits+string.punctuation
    pas = ''.join(random.choice(allLetters) for _ in range(length))
    return pas

try:
    userInput=int(input('Please enter password length: '))
    if userInput<8:
        print('Password length should be at least 8 character')
    else:
        newPass=createPass(userInput)
        print('Your pass is:', newPass)

        with open('strong_pass.txt', 'w') as file:
            file.write(newPass)
            print('Pass is saved strong_pass.txt file successfully')
except ValueError:
    print('Please enter a valid number')


# .............................user will input pass length and characters..........................
# def createPass(characters,length):
#     pas = ''.join(random.choice(characters) for _ in range(length))
#     return pas

# try:
#     passLength=int(input('Please enter password length: '))
#     passCharacter=input('Enter your pass characters: ')
#     if passLength<8:
#         print('Password length must be 8 or above')
#     else:
#         newPass=createPass(passCharacter, passLength)
#         print('Your pass is:', newPass)

#         with open('password.txt', 'w') as file:
#             file.write(newPass)
#             print('pass is successfully saved to password.txt file')
# except ValueError:
#     print('Please enter a valid number')

