import hashlib

selectedpassword = input("Wpisz hasło: ")
confirm = input("Potwierdź hasło: ")

hash = hashlib.sha256()
buffer = confirm.encode('utf-8')
hash.update(buffer)
result = hash.hexdigest()

if confirm == selectedpassword:
    with open('pws.txt', 'a+') as file:
        if result in file:
            print("Hasło już jest w bazie!")
        else:
            file.write("\n" + result)
else:
    print("Potwierdzenie hasła się nie zgadza!")