import networkx as nx
import matplotlib.pyplot as plt
import random

print("Memprediksi Penyebaran Penyakit Menular melalui Model Jaringan")

# Fungsi untuk meminta input probabilitas dari user
def input_probabilitas(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 1:  # Memastikan input antara 0 dan 1
                return value
            else:
                print("Input tidak valid. Silakan masukkan nilai antara 0 dan 1 (0-100%).")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka desimal.")

# Mengambil input dari pengguna
while True:
    try:
        num_nodes = int(input("Masukkan jumlah node (individu dalam populasi): "))
        if num_nodes > 0:
            break
        else:
            print("Jumlah node harus lebih dari 0.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka bulat positif.")
        print(f"populasi yang akan dianalisis terdiri dari {num_nodes} individu, ini akan merepresentasikan jumlah individu dalam simulasi.")

infection_prob = input_probabilitas("Masukkan probabilitas infeksi (0-1): ")
print(f"Probabilitas infeksi yang dimasukkan: {infection_prob * 100}%. Ini adalah kemungkinan bahwa individu yang terinfeksi akan menularkan penyakit ke individu yang rentan saat berinteraksi.")

recovery_prob = input_probabilitas("Masukkan probabilitas pemulihan (0-1): ")
print(f"Probabilitas pemulihan yang dimasukkan: {recovery_prob * 100}%. Ini adalah kemungkinan bahwa individu yang terinfeksi akan sembuh setiap langkah simulasi, semakin tinggi nilai ini, semakin cepat individu yang terinfeksi akan sembuh dari penyakit.")

# Validasi input untuk jumlah individu terinfeksi pada awalnya
while True:
    try:
        initial_infected = int(input("Masukkan jumlah individu terinfeksi pada awalnya: "))
        if 0 <= initial_infected <= num_nodes:
            break
        else:
            print(f"Input tidak valid. Silakan masukkan nilai antara 0 dan {num_nodes}.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka bulat.")

print(f"Jumlah individu terinfeksi pada awalnya yang dimasukkan: {initial_infected}. Ini adalah jumlah node yang akan mulai sebagai terinfeksi dalam simulasi.")
print(f"Jadi, {initial_infected} individu ini akan memengaruhi penyebaran penyakit ke individu lain dalam populasi.")

# Status node
SUSCEPTIBLE = "S"
INFECTED = "I"
RECOVERED = "R"

# Membangun graf dengan node yang ditentukan
G = nx.erdos_renyi_graph(num_nodes, 0.1)

# Menginisialisasi status semua node menjadi rentan (S)
nx.set_node_attributes(G, SUSCEPTIBLE, "status")

# Menetapkan beberapa node sebagai terinfeksi pada awalnya
initial_infected_nodes = random.sample(list(G.nodes()), initial_infected)
for node in initial_infected_nodes:
    G.nodes[node]["status"] = INFECTED

# Fungsi untuk visualisasi graf
def plot_graph(G, step):
    color_map = {"S": "blue", "I": "red", "R": "green"}
    colors = [color_map[G.nodes[node]["status"]] for node in G.nodes()]
    plt.figure(figsize=(8, 6))
    nx.draw(G, node_color=colors, with_labels=True)
    plt.title(f"Step {step}")
    plt.show()

# Simulasi penyebaran penyakit
def simulate_spread(G, steps=10):
    for step in range(steps):
        new_status = {}

        # Memproses setiap node
        for node in G.nodes:
            status = G.nodes[node]["status"]
            if status == INFECTED:
                # Setiap node terinfeksi memiliki kemungkinan sembuh
                if random.random() < recovery_prob:
                    new_status[node] = RECOVERED
                else:
                    new_status[node] = INFECTED
                # Menyebarkan infeksi ke tetangga rentan
                for neighbor in G.neighbors(node):
                    if G.nodes[neighbor]["status"] == SUSCEPTIBLE and random.random() < infection_prob:
                        new_status[neighbor] = INFECTED
            elif status == SUSCEPTIBLE:
                new_status[node] = SUSCEPTIBLE
            elif status == RECOVERED:
                new_status[node] = RECOVERED

        # Memperbarui status setiap node
        for node, status in new_status.items():
            G.nodes[node]["status"] = status

        # Plot graf setiap iterasi
        plot_graph(G, step)

# Menjalankan simulasi
simulate_spread(G, steps=10)

# Penjelasan setelah simulasi
print("\nSimulasi selesai.")
print("Berikut adalah ringkasan hasil dari simulasi:")
print(f"1. Jumlah individu dalam populasi: {num_nodes}")
print(f"2. Jumlah individu terinfeksi pada awalnya: {initial_infected}")
print(f"3. Probabilitas infeksi: {infection_prob * 100}%")
print(f"4. Probabilitas pemulihan: {recovery_prob * 100}%")

print("\nPenjelasan:")
print(f"Dari total individu yang ada, sebanyak {initial_infected} individu mulai terinfeksi.")
print("Probabilitas infeksi yang Anda masukkan menunjukkan kemungkinan bahwa setiap interaksi antara individu terinfeksi dan yang rentan dapat menghasilkan infeksi baru.")
print("Sebaliknya, probabilitas pemulihan menunjukkan seberapa cepat individu terinfeksi dapat sembuh dalam setiap langkah waktu.")

# KELOMPOK 3
# Penerapan metode graph dalam memprediksi penyebaran penyakit menular melalui model jaringan
# untuk mendukung kebijakan kesehatan publik menggunakan bahasa pemrograman python
# 
#     NAMA               NIM
# M. ALBI FEBRIANO    230504025
# NURUL HUSNA         230504022