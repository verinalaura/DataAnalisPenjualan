import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data
data = pd.read_csv('data_penjualan.csv')

# Membuat DataFrame dari data yang diberikan
data = pd.DataFrame({
    'Faktur': ['F001', 'F002', 'F003', 'F004', 'F005', 'F006', 'F007', 'F008', 'F009', 'F010'],
    'Tanggal': ['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-07', '2023-01-08', '2023-01-10', '2023-01-12', '2023-01-14', '2023-01-16'],
    'Jenis Kelamin': ['Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita'],
    'Jenis Barang': ['Elektronik', 'Pakaian', 'Peralatan Rumah Tangga', 'Elektronik', 'Pakaian', 'Peralatan Rumah Tangga', 'Elektronik', 'Pakaian', 'Peralatan Rumah Tangga', 'Elektronik'],
    'Jumlah': [2, 3, 1, 1, 4, 2, 3, 2, 1, 2]
})

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

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(data.index, data['Jumlah'], color='blue', alpha=0.5)
plt.title('Scatter Plot Penjualan')
plt.xlabel('Index')
plt.ylabel('Jumlah')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(data['Jumlah'].dropna(), bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Jumlah Penjualan')
plt.xlabel('Jumlah')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(data['Jumlah'].dropna())
plt.title('Box Plot of Jumlah Penjualan')
plt.ylabel('Jumlah')

# Membuat data untuk barplot jenis kelamin
gender_data = data['Jenis Kelamin'].value_counts()

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(gender_data.index, gender_data.values, color=['blue', 'pink'])
plt.title('Barplot Jenis Kelamin Pelanggan')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
