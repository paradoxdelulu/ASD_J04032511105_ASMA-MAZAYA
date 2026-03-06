# Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
# saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
# mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
# Berikut adalah data hasil tes potensi akademik yang tersedia:
# [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
# Soal:
# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
# skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
# 2. Kandidat berapa saja yang lolos?
#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# Memakai metode shellsort
def shellSort(data):
    n = len(data)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] < temp:  # Ubah tanda < menjadi > untuk mengurutkan secara descending
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        print("Gap:", gap, "Data:", data)
        gap //= 2

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
shellSort(data)
print("Skor lima kandidat dengan nilai tertinggi:", data[:5])  # Output:
print("Kandidat yang lolos: 7, 4, 2, 9, 6")