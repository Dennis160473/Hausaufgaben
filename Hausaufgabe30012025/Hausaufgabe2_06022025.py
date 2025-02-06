from cryptography.fernet import Fernet

import rsa


# Generiert einen Verschlüsselungsschlüssel (in einem realen Szenario sollte dieser sicher gespeichert werden)
key = Fernet.generate_key()
cipher = Fernet(key)

encMessage = cipher.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = cipher.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)

publicKey, privateKey = rsa.newkeys(512)

encMessage = rsa.encrypt(message.encode(), publicKey)
message = "hello geeks"
print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("decrypted string: ", decMessage)


text = "Hallo Welt!"
encrypted_text = cipher_suite.encrypt(text.encode())
print("Encrypted:", encrypted_text)

decrypted_text = cipher_suite.decrypt(encrypted_text)
print("Decrypted:", decrypted_text.decode())

#################################################################


# Simulierte Datenbank
users = []


def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    for u in users:
        if u["username"] == musername and decrypt_password(u["password"]) == mpassword:
            user = u
    return user


def signup(musername, mpassword):
    new_user_id = len(users) + 1
    encrypted_password = encrypt_password(mpassword)
    users.append(
        {"id": new_user_id, "username": musername, "password": encrypted_password}
    )


username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")

signup(username, password)
current_user = login(username, password)

print(f"My Logged in user with {username} and {password} is {current_user}")
