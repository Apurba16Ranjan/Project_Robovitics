from cryptography.fernet import Fernet
from File_Encryption import key

fernet=Fernet(key)

def decrypt(filename,key):
    # opening the encrypted file
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    print(encrypted)
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    print (decrypted)
    # opening the file in write mode and
    # writing the decrypted data
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)


decrypt('C:\\Users\\alok_\\Project_Robovitics\\File_Encryption\\N.txt', key)
