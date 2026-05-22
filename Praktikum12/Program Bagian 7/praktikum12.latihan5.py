# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus  Studi Kasus dengan Program Shortest Path
# ==========================================================

import heapq

# Representasi graph berbobot menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}
def dijkstra(graph, start):
    # Inisialisasi jarak ke semua node sebagai tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue untuk menyimpan node yang akan diproses
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, lewati
        if current_distance > distances[current_node]:
            continue
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Bogor:")
for node, distance in hasil.items():
    print(f"Bogor -> {node} = {distance}")


# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari Bogor adalah Depok dengan jarak 2.
# 3. Node yang memiliki jarak paling besar dari Bogor adalah Bandung dengan jarak 7.
# 4. Algoritma Dijkstra bekerja dengan memulai dari node awal (Bogor) dan menginisialisasi jarak ke semua node lain sebagai tak hingga, kecuali jarak ke node awal yang diatur menjadi 0. Algoritma kemudian menggunakan priority queue untuk memproses node dengan jarak terpendek terlebih dahulu. Setiap kali sebuah node diproses, algoritma memeriksa semua tetangganya dan memperbarui jarak jika ditemukan jalur yang lebih pendek melalui node tersebut. Proses ini berlanjut hingga semua node telah diproses, menghasilkan jarak terpendek dari node awal ke semua node lainnya dalam graph.

