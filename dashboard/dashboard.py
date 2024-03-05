import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load Data
bike_sharing = pd.read_csv("all_data.csv")

# Sidebar
with st.sidebar:
    st.title("Bike Sharing")
    st.markdown("""Berikut adalah Tren Penggunaan Sepeda saat ini""")


# Title
st.header("Dashboard :bike:")

# 1. Apakah ada korelasi antara musim dan jumlah sewa sepeda harian?
st.subheader("Tren Penggunaan Sepeda per Musim")
st.markdown("""
Dari visualisasi tren penggunaan sepeda per Musim, terlihat bahwa penggunaan sepeda cenderung meningkat dari musim semi (biasanya bulan Maret hingga May), kemudian mulai menurun menjelang akhir tahun. Ini menunjukkan bahwa cuaca dan musim memiliki pengaruh signifikan terhadap permintaan sepeda.
""")

# Visualisasi
seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
plt.bar(season_names, seasonal_data)
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Sewa Harian')
plt.title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
st.pyplot()


# 2. Apakah ada pola berdasarkan waktu dalam jumlah sewa sepeda harian??
st.subheader("Pola berdasarkan bulan")
st.markdown("""
Berdasarkan deskripsi yang Anda berikan, terdapat dua grafik yang menunjukkan pola waktu sewa sepeda. Waktu sewa lebih banyak terjadi pada bulan Juni dan September, sementara jumlah sewa sepeda meningkat sekitar jam 8 pagi dan sekitar jam 5 atau 6 sore.
""")

# Visualisasi
# Pola berdasarkan bulan
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, ci=None)
plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Sewa Sepeda Harian")

# Pola berdasarkan jam
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt_hourly", data=bike_sharing, ci=None)
plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Jam")
plt.xlabel("Jam")
plt.ylabel("Jumlah Sewa Sepeda Harian")

st.pyplot()



# 3. Bagaimana pengaruh cuaca terhadap jumlah sewa sepeda harian?
st.subheader("Bagaimana pengaruh cuaca terhadap jumlah sewa sepeda harian?")

st.markdown("""
Dari visualisasi penggunaan jumlah sewa sepeda mengingkat ketika cuaca Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian.
""")

# Visualisasi
plt.figure(figsize=(10, 6))
sns.boxplot(x="weathersit_daily", y="cnt_daily", data=bike_sharing)
plt.title("Pengaruh Weathersit Terhadap Jumlah Sewa Sepeda Harian")
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")

plt.grid(axis='y')

    
# Menyimpan gambar Matplotlib ke dalam variabel fig
st.pyplot()




# 4. Apakah ada perbedaan antara hari kerja dan hari libur dalam jumlah sewa sepeda harian?
st.subheader("Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur")

st.markdown("""
Berdasarkan perbandingan Ada perbedaan jumlah sewa sepeda lebih banyak ketika hari kerja daipada hari libur.
""")

# Visualisasi
plt.figure(figsize=(8, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_sharing)
plt.title("Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian")
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")


# Menampilkan visualisasi dengan st.pyplot(fig)
st.pyplot()

