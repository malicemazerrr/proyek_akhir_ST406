from utils import (
    muat_data,
    bersihkan_data,
    hitung_per_dekade,
    buat_grafik
)

def main():
    # Lokasi dataset
    path_dataset = "dataset/artists.csv"

    # Memuat data
    df = muat_data(path_dataset)

    # Membersihkan data
    df_bersih = bersihkan_data(df)

    # Menghitung jumlah seniman per dekade
    hasil_dekade = hitung_per_dekade(df_bersih)

    # Menampilkan hasil
    print("\n=== 5 Data Pertama ===")
    print(df_bersih.head())

    print("\n=== Jumlah Seniman per Dekade ===")
    print(hasil_dekade)

    # Membuat grafik
    buat_grafik(
        hasil_dekade,
        "grafik_line.png",
        "grafik_bar.png"
    )

    print("\nGrafik berhasil disimpan!")
    print("Program selesai.")

if __name__ == "__main__":
    main()
