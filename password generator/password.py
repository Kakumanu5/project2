import random
print('Welcome to the Password Generator!')
input_letter=int(input('How many letters would you like in your password?'))
input_symbol=int(input('How many symbols would you like in your password?'))
input_number=int(input('How many numbers would you like in your password?'))
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
symbols='!@$%^&*()_+=-?'
numbers='1234567890'
password=[]
for i in range(0,input_letter):
    i=random.choice(letters)
    password+=i
for i in range(0,input_symbol):
    i=random.choice(symbols)
    password+=i
for i in range(0,input_number):
    i=random.choice(numbers)
    password+=i
random.shuffle(password) #for high level protection
final_output=''
for i in password:
    final_output+=i
print(final_output)
