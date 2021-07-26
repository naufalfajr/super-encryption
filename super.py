# ************************ #
# Super Enkripsi           #
# Vigenere + Railfence     #
# ************************ #

import railfence
import vigenere

def main():
    print("Key and Message can only be alphabetic")
    pilihan = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if pilihan == 1:
        print("---Encryption---")
        msg = input("Masukkan plaintext: ").upper()
        key = input("Masukkan key: ").upper()
        rails = int(input("Enter rails: "))
        message, mapped_key = vigenere.msg_and_key(msg, key)
        encryptedMsg = vigenere.cipher_encryption(message, mapped_key)
        railfence.cipher_encryption(encryptedMsg, rails)

    elif pilihan == 2:
        print("---Decryption---")
        msg = input("Masukkan ciphertext: ").upper()
        key = input("Masukkan key: ").upper()
        rails = int(input("Enter rails: "))
        message, mapped_key = vigenere.msg_and_key(msg, key)
        decryptedMsg = railfence.cipher_decryption(message, rails)
        vigenere.cipher_decryption(decryptedMsg, mapped_key)

    else:
        print("Pilihan Salah")


if __name__ == "__main__":
    main()