import pandas as pd
import matplotlib.pyplot as plt


def muat_data(path):
    df = pd.read_csv(path)
    return df


def bersihkan_data(df):
    print("Missing values per kolom: ")
    print(df.isnull().sum())

    df['Nationality'] = df['Nationality'].fillna('Unknown')
    df['Gender'] = df['Gender'].fillna('Unknown')
    df_bersih = df.dropna(subset=['Birth Year'])
    return df_bersih


def hitung_per_dekade(df):
    df['Dekade'] = (df['Birth Year'] // 10 * 10).astype(int)
    hasil = df.groupby('Dekade').size()
    return hasil


def buat_grafik(hasil_dekade, path_output_line, path_output_bar):
    plt.figure(figsize=(10, 6))
    hasil_dekade.plot(kind='line', marker='o')
    plt.title('Tren Jumlah Kelahiran Seniman per Dekade')
    plt.xlabel('Dekade')
    plt.ylabel('Jumlah Seniman')
    plt.grid(True)
    plt.savefig(path_output_line)
    plt.close()

    plt.figure(figsize=(10, 6))
    hasil_dekade.plot(kind='bar', color='skyblue')
    plt.title('Jumlah Kelahiran Seniman per Dekade')
    plt.xlabel('Dekade')
    plt.ylabel('Jumlah Seniman')
    plt.savefig(path_output_bar)
    plt.close()


def simpan_hasil_analisis(df_bersih, hasil_dekade, path_output):
    dekade_puncak = hasil_dekade.idxmax()
    jumlah_puncak = hasil_dekade.max()

    with open(path_output, 'w') as f:
        f.write("HASIL ANALISIS DATA SENIMAN MOMA\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total data seniman (setelah dibersihkan): {len(df_bersih)}\n\n")
        f.write("Jumlah seniman per dekade:\n")
        f.write(str(hasil_dekade))
        f.write(f"\n\nDekade dengan kelahiran seniman terbanyak: {dekade_puncak}")
        f.write(f"\nJumlah seniman lahir di dekade tsb: {jumlah_puncak}")