import random 

print('WELCOME TO YOUR PASSWORD GENERATOR')

chars = 'abcdefghijklmnoprstuvyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@*()^%.,?1234567890'

number = input('Amount of passwords to generate : ')

number = int(number)

length = input('Input yout password length : ')
length = int(length)

print('\n here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

