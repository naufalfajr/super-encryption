def msg_and_key(msg, key):
    # variable untuk menyimpan key yang sudah di map
    key_map = ""

    j=0
    for i in range(len(msg)):
        if ord(msg[i]) == 32:
            # abaikan spasi
            key_map += " "
        else:
            if j < len(key):
                key_map += key[j]
                j += 1
            else:
                j = 0
                key_map += key[j]
                j += 1

    # print(key_map)
    return msg, key_map

def create_vigenere_table():
    tabel = []
    for i in range(26):
        tabel.append([])

    for baris in range(26):
        for kolom in range(26):
            if (baris + 65) + kolom > 90:
                # kembali ke A setelah sampai Z
                # setelah baris pertama, setiap huruf akan digeser kekiri satu kali dibandingkan dengan baris atasnya
                tabel[baris].append(chr((baris+65) + kolom - 26))
            else:
                # setelah baris pertama, setiap huruf akan digeser kekiri satu kali dibandingkan dengan baris atasnya
                tabel[baris].append(chr((baris+65)+kolom))

    # cek tabel
    # for row in table:
    #     for column in row:
    #         print(column, end=" ")
    #     print(end="\n")

    return tabel

def cipher_encryption(message, mapped_key):
    tabel = create_vigenere_table()
    encrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignoring space
            encrypted_text += " "
        else:
            # mendapatkan elemen tabel pada posisi tertentu
            baris = ord(message[i])-65
            kolom = ord(mapped_key[i]) - 65
            encrypted_text += tabel[baris][kolom] # mendapatkan perpotongan row dan column pada tabel vigenere

    print("Encrypted Message: {}".format(encrypted_text))
    return encrypted_text

def itr_count(mapped_key, message):
    counter = 0
    result = ""

    # dimulai dari huruf yang ada di mapped_key kemudian diiterasi sampai 26 huruf (setelah z kembali ke a)
    for i in range(26):
        if mapped_key + i > 90:
            result += chr(mapped_key+(i-26))
        else:
            result += chr(mapped_key+i)

    # menghitung iterasi dari huruf mapped_key hingga sama dengan huruf chipertext
    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1

    return counter

def cipher_decryption(message, mapped_key):
    decrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignoring space
            decrypted_text += " "
        else:
            # menambahkan iterasi dengan 65 untuk mendapatkan huruf dalam ASCII
            # dengan ini kita mendapatkan huruf yang telah didekripsi
            decrypted_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))

    print("Decrypted Message: {}".format(decrypted_text))
    return decrypted_text

def main():
    print("Key dan Message hanya bisa huruf")
    pilihan = int(input("1. Encryption\n2. Decryption\nPilih(1,2): "))
    if pilihan == 1:
        print("---Encryption---")
        msg = input("Masukkan message: ").upper()
        key = input("Masukkan key: ").upper()
        message, mapped_key = msg_and_key(msg, key)
        cipher_encryption(message, mapped_key)

    elif pilihan == 2:
        print("---Decryption---")
        msg = input("Masukkan message: ").upper()
        key = input("Masukkan key: ").upper()
        message, mapped_key = msg_and_key(msg, key)
        cipher_decryption(message, mapped_key)

    else:
        print("Pilihan Salah")

if __name__ == "__main__":
    main()