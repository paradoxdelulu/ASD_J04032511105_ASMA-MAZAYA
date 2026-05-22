# Nama : Asma Mazaya
# NIM : J0403251105
# Kelas : A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
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


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3 (melalui C).
# 4. Jarak A ke D lebih kecil melalui C karena bobot pada edge A ke C (2) dan C ke D (1) lebih kecil dibandingkan bobot pada edge A ke B (4) dan B ke D (5). Sehingga total jarak melalui C adalah 3, sedangkan melalui B adalah 9.
# 5. Fungsi priority_queue dalam algoritma Dijkstra digunakan untuk menyimpan node-node yang akan diproses berdasarkan jarak terpendek yang ditemukan sejauh ini. Dengan menggunakan priority queue, algoritma dapat dengan cepat mengambil node dengan jarak terpendek untuk diproses selanjutnya.
# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengasumsikan bahwa setelah sebuah node diproses, jaraknya tidak akan berubah lagi. Jika terdapat edge dengan bobot negatif, jarak ke node yang sudah diproses bisa menjadi lebih kecil, yang menyebabkan algoritma memberikan hasil yang salah. Oleh karena itu, Dijkstra hanya dapat digunakan pada graph dengan bobot non-negatif.   