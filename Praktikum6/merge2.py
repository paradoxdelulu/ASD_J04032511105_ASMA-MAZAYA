# MERGE SORT DESCENDING
def mergeSort(data):
    print("Splitting ",data)
    if len(data)>1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]: # Ubah tanda <= menjadi >= untuk mengurutkan secara descending
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",data)

data = [54,26,93,17,77,31,44,55,20]
mergeSort(data)
print(data)

#BANDINGKAN OUTPUT DENGAN REPRESENTASI POHON DI ATAS, PERHATIKAN BAGAIMANA PROSES SPLITTING DAN MERGING BERJALAN SESUAI DENGAN STRUKTUR POHON !
# Pada proses splitting, data dibagi menjadi dua bagian secara rekursif hingga mencapai elemen tunggal. 
# Pada proses merging, elemen-elemen tersebut digabungkan kembali dengan urutan yang benar sesuai dengan 
# aturan pengurutan (ascending atau descending).
# jika ingin mengurutkan secara descending, gunakan tanda >= pada kondisi perbandingan saat merging