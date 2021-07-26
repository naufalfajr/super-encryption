import re

def cipher_encryption(msg, rails):

    # menghapus spasi dari msg
    msg = msg.replace(" ", "")

    # membuat matrix kosong dan diisi dengan titik
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for baris in range(rails):
        for kolom in range(len(msg)):
            railMatrix[baris].append('.')

    # mencoba matrix
    # for baris in railMatrix:
    #     for kolom in baris:
    #         print(kolom, end="")
    #     print("\n")

    # menaruh message di matrix huruf per huruf berbentuk zig-zag
    baris = 0
    cek = 0
    for i in range(len(msg)):
        if cek == 0:
            railMatrix[baris][i] = msg[i]
            baris += 1
            if baris == rails:
                cek = 1
                baris -= 1
        elif cek == 1:
            baris -= 1
            railMatrix[baris][i] = msg[i]
            if baris == 0:
                cek = 0
                baris = 1

    # mencoba matrix yang telah diisi huruf
    # for baris in railMatrix:
    #     for kolom in row:
    #         print(kolom, end="")
    #     print("\n")

    encryp_text = ""
    for i in range(rails):
        for j in range(len(msg)):
            encryp_text += railMatrix[i][j]

    # menghapus '.' dari encrypted message
    encryp_text = re.sub(r"\.", "", encryp_text)
    print("Encrypted Text by Railfence: {}".format(encryp_text))
    return encryp_text

def cipher_decryption(msg, rails):

    # menghapus spasi dari msg
    msg = msg.replace(" ", "")

    # membuat matrix kosong dan diisi dengan titik
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for baris in range(rails):
        for kolom in range(len(msg)):
            railMatrix[baris].append('.')

    # mencoba matrix
    # for baris in railMatrix:
    #     for kolom in baris:
    #         print(kolom, end="")
    #     print("\n")

    # menaruh message di matrix huruf per huruf berbentuk zig-zag
    baris = 0
    cek = 0
    for i in range(len(msg)):
        if cek == 0:
            railMatrix[baris][i] = msg[i]
            baris += 1
            if baris == rails:
                cek = 1
                baris -= 1
        elif cek == 1:
            baris -= 1
            railMatrix[baris][i] = msg[i]
            if baris == 0:
                cek = 0
                baris = 1

    # mencoba matrix yang telah diisi huruf
    # for baris in railMatrix:
    #     for kolom in baris:
    #         print(kolom, end="")
    #     print("\n")

    # mengurutkan ulang huruf-huruf di matrix
    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                # abaikan '.'
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1

    # mencoba matrix yang telah diurutkan ulang
    # for i in railMatrix:
    #     for kolom in i:
    #         print(kolom, end="")
    #     print("\n")

    # mengambil huruf-huruf dari matrix untuk dibentuk menjadi decrypted text dalam string
    cek = 0
    baris = 0
    decryp_text = ""
    for i in range(len(msg)):
        if cek == 0:
            decryp_text += railMatrix[baris][i]
            baris += 1
            if baris == rails:
                cek = 1
                baris -= 1
        elif cek == 1:
            baris -= 1
            decryp_text += railMatrix[baris][i]
            if baris == 0:
                cek = 0
                baris = 1

    decryp_text = re.sub(r"\.", "", decryp_text)
    print("Decrypted Text by Railfence: {}".format(decryp_text))
    return decryp_text

def main():
    pilihan = int(input("1. Encryption\n2. Decryption\nPilih(1,2): "))
    if pilihan == 1:
        print("---Encryption---")
        msg = input("Masukkan Text: ")
        rails = int(input("Masukkan Rails: "))
        cipher_encryption(msg, rails)
    elif pilihan == 2:
        print("---Decryption---")
        msg = input("Masukkan Text: ")
        rails = int(input("Masukkan Rails: "))
        cipher_decryption(msg, rails)
    else:
        print("Pilihan Salah")

if __name__ == "__main__":
    main()