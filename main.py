from encryption import encryptPlaintext
from decryption import decryptCiphertext
# main function                 
def main():
    choice = int(input("Welcome to AES Program!!\nIMPORTANT: case encryption, enter plaintext firstly in plaintext.txt file and the output will be returnted in ciphertxt.txt file, while case decryption, enter ciphertext in ciphertxt.txt file and the ouput will be returned to plaintext.txt file.\nPlz, enter 1 for encryption and 2 for decryption: "))
    while True:
        if choice==1:
            encryptPlaintext()
            break
        elif choice==2:
            decryptCiphertext()
            break
        else:
            choice = int(input("Error!!\nchoice must be 1 or 2\nPlz, enter 1 for encryption and 2 for decryption: "))



# derive main 

main()    