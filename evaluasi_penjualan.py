import pandas as pd
import matplotlib.pyplot as plt

# Membuat DataFrame dari data yang diberikan
data = pd.DataFrame({
    'Faktur': ['F001', 'F002', 'F003', 'F004', 'F005', 'F006', 'F007', 'F008', 'F009', 'F010'],
    'Tanggal': ['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-07', '2023-01-08', '2023-01-10', '2023-01-12', '2023-01-14', '2023-01-16'],
    'Jenis Kelamin': ['Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita'],
    'Jenis Barang': ['Elektronik', 'Pakaian', 'Peralatan Rumah Tangga', 'Elektronik', 'Pakaian', 'Peralatan Rumah Tangga', 'Elektronik', 'Pakaian', 'Peralatan Rumah Tangga', 'Elektronik'],
    'Jumlah': [2, 3, 1, 1, 4, 2, 3, 2, 1, 2]
})

# Mengubah kolom 'Tanggal' menjadi tipe data datetime
data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# Evaluasi terhadap jumlah transaksi dan total barang yang terjual
total_transaksi = data['Faktur'].count()
total_barang_terjual = data['Jumlah'].sum()

print(f"\nTotal transaksi: {total_transaksi}")
print(f"Total barang terjual: {total_barang_terjual}")

# Mengelompokkan data berdasarkan jenis barang dan jenis kelamin
grouped_data = data.groupby(['Jenis Kelamin', 'Jenis Barang'])['Jumlah'].sum()

print("\nJumlah barang terjual berdasarkan jenis kelamin dan jenis barang:")
print(grouped_data)

# Mengelompokkan data berdasarkan tanggal untuk melihat tren penjualan
trend_penjualan = data.groupby('Tanggal')['Jumlah'].sum()

print("\nTren penjualan berdasarkan tanggal:")
print(trend_penjualan)

# Visualisasi tren penjualan
plt.figure(figsize=(10, 6))
plt.plot(trend_penjualan.index, trend_penjualan.values, marker='o', linestyle='-')
plt.title('Tren Penjualan Berdasarkan Tanggal')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Barang Terjual')
plt.grid(True)
plt.show()
