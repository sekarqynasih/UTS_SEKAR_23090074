# buatkan sebuah program yang meminta pengguna untuk memasukkan harga barang dari beberapa barang, kemudian program akan menghitung total harga dari seluruh barang 
# berikut adalah langkah langkahnya :
# program meminta pengguna untuk memasukan jumlah barang 
# kemudian meminta pengguna untuk memasukkan harga barang untuk setiap barang sebanyak yang telah di tentukan 
# setelah memasukan semua harga, program akan menghitung total harga belanjaan dari seluruh jumlah barang 
# tampilkan total harga belanjaan

import jumlah_barang as math

def eksekusi():
    print('Masukan jumlah belanjaan :')
    print('masukan harga baranag pertama')
    print('masukan harga barang ke 2')
    print("Keluar")

    pilihan = input("Masukkan jumlah belanjaan: ")

    if pilihan == '0':
        print("Terima kasih telah berbelanja.")
        exit()
    elif pilihan in {'1', '2'}:
        angka1 = float(input("Masukkan harga barang pertama : "))
        angka2 = float(input("Masukkan harga barang kedua : "))

        if pilihan == '1':
            hasil = math.penjumlahan(angka1, angka2)
            print("Hasil penjumlahan:", hasil)
        elif pilihan == '2':
            hasil = math.pengurangan(angka1,angka2)
            print("Hasil pengurangan:", hasil)
        else:
            print("pilihan tidak tersedia")
            