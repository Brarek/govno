import random
y = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("Каое длины пароль"))
r = ""
for i in range(x):
    r += random.choice(y)
print(r)    
