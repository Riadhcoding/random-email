import random,string
"""
Youtube :
www.youtube.com/c/riadhcoding
www.youtube.com/c/pythonlife

Instagram :
https://www.instagram.com/riadh_coding

"""
email = [
    '@gmail.com',
    '@yahoo.com',
    '@outlook.com',
    'hotmail.com',
    '@hotmail.fr'
]
f = open('users.txt','r').readlines()
count = 0
while (count < len(f)):
    for i in f :
        print(i.strip() +str(random.randint(1000,99999)) + random.choice(email))
    count += 1



