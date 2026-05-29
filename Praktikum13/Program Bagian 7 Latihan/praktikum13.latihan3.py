# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 3 : Implementasi Algoritma Prim
# ==========================================================
import heapq
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])

    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

    if v not in visited:
       
        visited.add(v)

        mst.append((u, v, weight))
        total_weight += weight

        for neighbor, w in graph[v].items():
            
            if neighbor not in visited:
                heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)


# Jawaban Analisis:
# 1. Node awal yang digunakan adalah node 'A'.      
# 2. Edge yang dipilih pertama kali adalah (2, 'A', 'C') karena memiliki bobot terkecil yaitu 2.
# 3. Prim menentukan edge berikutnya dengan memilih edge yang memiliki bobot terkecil dari antara node yang sudah dikunjungi dan node yang belum dikunjungi. Dalam hal ini, setelah memilih edge (2, 'A', 'C'), Prim akan mempertimbangkan edge yang terhubung ke node 'C' dan memilih edge dengan bobot terkecil berikutnya, yaitu (1, 'C', 'D').
# 4. Total bobot MST yang dihasilkan adalah 6, yang terdiri dari edge (2, 'A', 'C'), (1, 'C', 'D'), dan (3, 'B', 'D').
# 5. Perbedaan pendekatan Prim dan Kruskal adalah:
#    - Prim membangun MST dengan memulai dari satu node dan menambahkan edge yang terhubung ke node tersebut secara bertahap, sedangkan Kruskal membangun MST dengan mengurutkan semua edge berdasarkan bobot dan menambahkan edge ke MST jika tidak membentuk cycle. 
#    - Prim lebih fokus pada node dan edge yang terhubung langsung, sementara Kruskal lebih fokus pada edge secara keseluruhan.  
#    - Prim menggunakan struktur data seperti priority queue untuk memilih edge dengan bobot terkecil yang terhubung ke node yang sudah dikunjungi, sedangkan Kruskal menggunakan struktur data seperti union-find untuk memastikan bahwa penambahan edge tidak membentuk cycle.     
#    - Prim lebih efisien untuk graph yang padat, sedangkan Kruskal lebih efisien untuk graph yang jarang.
#    - Prim dapat digunakan untuk graph yang tidak terhubung, sedangkan Kruskal hanya dapat digunakan untuk graph yang terhubung.
