# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal
# ==========================================================
# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)


# Jawaban Analisis:
# 1. Edge yang dipilih pertama kali adalah (1, 'C', 'D') karena memiliki bobot terkecil yaitu 1.
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu karena algoritma Krus  kal bertujuan untuk membangun MST dengan total bobot yang minimal. Memilih edge dengan bobot terkecil memastikan bahwa kita selalu menambahkan edge yang paling efisien dalam hal bobot ke dalam MST, sehingga membantu mencapai total bobot yang minimal.
# 3. Total bobot MST yang dihasilkan adalah 6, yang terdiri dari edge (1, 'C', 'D'), (2, 'A', 'C'), dan (3, 'B', 'D').
# 4. Edge tertentu tidak dipilih karena mereka akan membentuk cycle jika ditambahkan ke MST. Misalnya, edge (4, 'A', 'B') tidak dipilih karena kedua node A dan B sudah terhubung melalui edge (2, 'A', 'C') dan (3, 'B', 'D'), sehingga menambahkan edge (4, 'A', 'B') akan membentuk cycle. Demikian juga, edge (5, 'A', 'D') tidak dipilih karena A dan D sudah terhubung melalui edge (2, 'A', 'C') dan (1, 'C', 'D').      