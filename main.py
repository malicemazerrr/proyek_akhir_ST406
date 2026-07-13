from utils import (
    muat_data,
    bersihkan_data,
    hitung_per_dekade,
    buat_grafik,
    simpan_hasil_analisis
)


def main():
    path_dataset = "dataset/artists.csv"

    df = muat_data(path_dataset)
    df_bersih = bersihkan_data(df)
    hasil_dekade = hitung_per_dekade(df_bersih)

    print("\n=== 5 Data Pertama ===")
    print(df_bersih.head())
    print("\n=== Jumlah Seniman per Dekade ===")
    print(hasil_dekade)

    buat_grafik(
        hasil_dekade,
        "grafik_line.png",
        "grafik_bar.png"
    )

    simpan_hasil_analisis(
        df_bersih,
        hasil_dekade,
        "hasil_analisis.txt"
    )

    print("\nGrafik berhasil disimpan!")
    print("File hasil_analisis.txt berhasil dibuat.")
    print("Program selesai.")


if __name__ == "__main__":
    main()