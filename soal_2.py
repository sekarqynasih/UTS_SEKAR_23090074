# buatlah program python yang dapat menentukan apakah suatu tahun adalah tahun kabisat atau bukan
# sebuah tahun disebut tahun kabisat jika memenuhi salah satu kondisi berikut : 
# 1. tahun tersebut habis di bagi 400
# 2. tahun tersebut habis di bagi 4 tapi tidak habis di bagi 100


jumlah_tahun = int(input('masukan tahun :'))
if jumlah_tahun % 400 == 0:
    print(f'tahun {jumlah_tahun} merupakan TAHUN KABISAT')
elif jumlah_tahun % 4 == 0 and jumlah_tahun % 100 != 0:
    print(f'tahun {jumlah_tahun} BUKAN tahun kabisat')
