import pandas as pd

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

