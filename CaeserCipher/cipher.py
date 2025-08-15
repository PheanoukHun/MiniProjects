
message = "hello world"
key = 3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
shifted = alphabet[key:] + alphabet[:key]

def encrypt(message):
    encrypt = ""
    for character in message:
        if character in alphabet:
            index = alphabet.index(character)
            encrypt += shifted[index]
        else:
            encrypt += character

    message = encrypt
    print(message)
    return message

def decrypt(message):
    decrypt = ""
    for character in message:
        if character in alphabet:
            index = shifted.index(character)
            decrypt += alphabet[index]
        else:
            decrypt += character

    message = decrypt
    print(message)

encrypted = encrypt(message)
decrypt(encrypted)