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
    df['Dekade'] = (df['Birth Year'] // 10*10).astype(int)
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