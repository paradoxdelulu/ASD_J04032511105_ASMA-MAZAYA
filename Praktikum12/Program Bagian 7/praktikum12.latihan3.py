# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
       
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B adalah 4 (A ke C) + (-2) (C ke B) = 2.
# 3. Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B (2) dibandingkan jalur langsung A -> B (5).
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini melakukan relaksasi edge secara berulang, sehingga dapat menangani perubahan jarak yang terjadi akibat bobot negatif. Dijkstra tidak dapat menangani bobot negatif karena menggunakan priority queue yang mengasumsikan bahwa jarak yang sudah ditemukan tidak akan berubah.
# 5. Proses relaksasi edge adalah proses di mana algoritma memeriksa setiap edge dan memperbarui jarak ke node tetangga jika ditemukan jarak yang lebih kecil melalui edge tersebut. Ini dilakukan dengan membandingkan jarak saat ini ke node tetangga dengan jarak yang dihitung melalui edge yang sedang diperiksa. Jika jarak yang dihitung lebih kecil, maka jarak ke node tetangga diperbarui.
# 6. Perbedaan utama antara Bellman-Ford dan Dijkstra adalah bahwa Bell
