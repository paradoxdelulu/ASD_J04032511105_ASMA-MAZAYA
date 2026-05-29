# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 1 : Memahami Konsep Spanning Tree
# ==========================================================
# Graph dengan daftar edge
edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('a', 'd'),
    ('b', 'd'),
    ('c', 'd')
]
# Menampilkan daftar edge pada graph
print("Daftar edge pada graph:")
for edge in edges:
    print(edge)

# Contoh spanning tree yang valid
spanning_tree = [
    ('a', 'b'),
    ('a', 'c'),
    ('a', 'd')
]

# Menampilkan contoh spanning tree yang valid
print("\nContoh spanning tree yang valid:")

for edge in spanning_tree:
    print(edge) 

# Menampilkan jumlah edge pada graph awal
print("\nJumlah edge pada graph awal:", len(edges))

# Menampilkan jumlah edge pada spanning tree
print("Jumlah edge pada spanning tree:", len(spanning_tree))


# Jawaban Analisis:
# 1. Graph awal memiliki semua edge yang menghubungkan node-node, sedangkan spanning tree hanya memiliki subset dari edge tersebut yang menghubungkan semua node tanpa membentuk cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena cycle akan menyebabkan redundansi dalam koneksi antara node-node. Spanning tree harus menghubungkan semua node dengan jumlah edge yang minimal, dan cycle akan menambah jumlah edge yang tidak diperlukan.
# 3. Jumlah edge pada spanning tree selalu lebih sedikit karena spanning tree hanya menyert akan edge yang diperlukan untuk menghubungkan semua node tanpa membentuk cycle. Dalam sebuah graph dengan n node, spanning tree akan selalu memiliki n-1 edge, sedangkan graph awal dapat memiliki lebih banyak edge tergantung pada jumlah koneksi antara node-node.       

