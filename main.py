from utils import (
    muat_data,
    bersihkan_data,
    hitung_per_dekade,
    hitung_per_negara,
    buat_grafik,
    simpan_hasil_analisis
)


def main():
    path_dataset = "dataset/artists.csv"

    
    df = muat_data(path_dataset)
    df_bersih = bersihkan_data(df)

    
    hasil_dekade = hitung_per_dekade(df_bersih)
    hasil_negara = hitung_per_negara(df_bersih)

    
    print("\n=== 5 Data Pertama ===")
    print(df_bersih.head())

    print("\n=== Jumlah Seniman per Dekade ===")
    print(hasil_dekade)

    print("\n=== Top 10 Negara dengan Seniman Terbanyak ===")
    print(hasil_negara)

    
    buat_grafik(
        hasil_dekade,
        hasil_negara,
        "grafik_line.png",
        "grafik_bar.png"
    )

    
    simpan_hasil_analisis(
        df_bersih,
        hasil_dekade,
        hasil_negara,
        "hasil_analisis.txt"
    )

    print("\nGrafik berhasil disimpan!")
    print("File hasil_analisis.txt berhasil dibuat.")
    print("Program selesai.")


if __name__ == "__main__":
    main()