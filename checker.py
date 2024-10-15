import hashlib

userinput = input("Wpisz hasło: ")

sha256hash = hashlib.sha256()

bufferuserinput = userinput.encode('utf-8')

sha256hash.update(bufferuserinput)

result = sha256hash.hexdigest()

with open('pws.txt', 'r') as file:
    content = file.readlines()

content = [line.strip() for line in content]

if result in content:
    print("correct")
else:
    print("incorrect")