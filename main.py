#Author Sinan ötük

import random


password = ""


length = int(input("Enter the desires length: "))

for i in range(length):
    password += chr(random.randint(33,125))

print(password)
