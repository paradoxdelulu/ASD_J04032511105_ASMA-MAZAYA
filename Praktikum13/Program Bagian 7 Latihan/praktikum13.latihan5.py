# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 5 : Membuat Program MST dengan Kasus Baru
# ==========================================================
import heapq
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},
    'Bandung': {'Jakarta': 6, 'Depok': 4}
    }

def prim(graph, start):
    visited = set([start]) # Set untuk menyimpan kota-kota yang sudah dikunjungi
    edges = []
    for neighbor, weight in graph[start].items():
    # Menambahkan edge yang terhubung ke kota awal ke dalam heap
        heapq.heappush(edges, (weight, start, neighbor)) 
    mst = [] 
    total_weight = 0 
    # Proses Prim untuk membangun MST
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges) 
        if v not in visited: # Memeriksa apakah kota tujuan belum dikunjungi
            visited.add(v) 
            mst.append((u, v, weight)) 
            total_weight += weight 
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: # Memeriksa apakah kota tetangga belum dikunjungi
                    heapq.heappush(edges, (w, v, neighbor)) 
    return mst, total_weight 

mst, total = prim(graph, 'Bogor') 

print("Minimum Spanning Tree:") 

for edge in mst:    
    print(edge) 

print("Total biaya minimum =", total)

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Jaringan Jalan Antar Kota
# 2. Algoritma yang digunakan adalah Prim.
# 3. Edge yang dipilih dalam MST adalah:
#    - (2, 'Bogor', 'Depok')
#    - (3, 'Depok', 'Jakarta')
#    - (4, 'Depok', 'Bandung')
# 4. Total bobot MST adalah 9, yang merupakan jumlah dari bobot edge yang dipilih (2 + 3 + 4).
# 5. Edge tertentu tidak dipilih karena mereka akan membentuk cycle jika ditambahkan ke MST. Misalnya, edge (5, 'Bogor', 'Jakarta') tidak dipilih karena kedua kota Bogor dan Jakarta sudah terhubung melalui edge (2, 'Bogor', 'Depok') dan (3, 'Depok', 'Jakarta'), sehingga menambahkan edge (5, 'Bogor', 'Jakarta') akan membentuk cycle. Demikian juga, edge (6, 'Jakarta', 'Bandung') tidak dipilih karena Jakarta dan Bandung sudah terhubung melalui edge (3, 'Depok', 'Jakarta') dan (4, 'Depok', 'Bandung'), sehingga menambahkan edge (6, 'Jakarta', 'Bandung') akan membentuk cycle.    
