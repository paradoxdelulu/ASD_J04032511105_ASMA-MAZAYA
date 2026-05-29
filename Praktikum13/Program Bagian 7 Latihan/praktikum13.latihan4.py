# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 4 : Studi Kasus: Jaringan Nirkabel Antar Gedung
# ==========================================================
import heapq
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
    # Menambahkan edge yang terhubung ke node awal ke dalam heap
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0 # Variabel untuk menyimpan total bobot MST
    # Proses Prim untuk membangun MST
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)
        if v not in visited: # Memeriksa apakah node tujuan belum dikunjungi
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items(): # Menambahkan edge yang terhubung ke node baru yang dikunjungi
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'GedungA')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge) 
    
print("Total biaya minimum =", total)

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Prim.
# 2. Edge yang dipilih adalah:
#    - (2, 'GedungA', 'GedungC')
#    - (1, 'GedungC', 'GedungD')
#    - (3, 'GedungD', 'GedungB')
# 3. Total biaya minimum adalah 6, yang merupakan jumlah dari bobot edge yang dipilih (2 + 1 + 3).
# 4. MST cocok digunakan pada kasus ini karena kita ingin menghubungkan semua gedung dengan biaya minimum. MST memastikan bahwa semua node (gedung) terhubung tanpa membentuk siklus, sehingga menghasilkan jaringan yang efisien dan hemat biaya untuk komunikasi nirkabel antar gedung.       
