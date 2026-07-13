========================================================
README - ANALISIS DATA SENIMAN MUSEUM OF MODERN ART (MoMA)
========================================================

JUDUL PROYEK
------------
Analisis Pola Perkembangan Jumlah Seniman di Koleksi MoMA
Berdasarkan Dekade Kelahiran Dan juga Kebangsaan (Nationality)

NAMA DAN NIM ANGGOTA
---------------------
1. Renna Sahda Paramitha       - 25.11.6516
2. Putri Rizki Aprilia Harahap - 25.11.6518
3. Devano Putwa Damsuki        - 25.11.6431
4. Fasih Arya Utama            - 25.11.6500

DESKRIPSI SINGKAT
-----------------
Proyek ini menganalisis dataset seniman koleksi Museum of Modern
Art (MoMA) (artists.csv) untuk menelusuri pola kelahiran seniman
berdasarkan dekade, guna menemukan periode puncak produktivitas
seni modern, sekaligus melihat sebaran kebangsaan (nationality)
seniman dalam koleksi tersebut.

Dataset mentah berisi 15.091 baris data seniman dari berbagai
negara, mencakup atribut kebangsaan (Nationality), gender
(Gender), tahun lahir (Birth Year), dan tahun wafat (Death Year).
Proses pembersihan data dilakukan dengan mengisi nilai kosong
pada kolom Nationality dan Gender menjadi "Unknown", serta
membuang baris yang tidak memiliki data Birth Year, sehingga
diperoleh 11.237 data seniman dengan tahun lahir yang tercatat,
mencakup rentang tahun 1730-2010 (29 dekade).

Hasil analisis menunjukkan bahwa dekade 1940 merupakan periode
dengan jumlah kelahiran seniman terbanyak, yaitu 1.535 orang,
dengan lima dekade tersibuk (masing-masing di atas 800 seniman)
berada pada rentang 1920-1970. Tren menunjukkan pertumbuhan
pesat sejak pertengahan abad ke-19 hingga mencapai puncaknya
pada pertengahan abad ke-20, yang dapat dipandang sebagai zaman
keemasan seni modern dalam koleksi MoMA. Penurunan jumlah
seniman pada dekade-dekade terakhir (1980-2010) lebih
mencerminkan keterbatasan pencatatan koleksi ketimbang penurunan
aktivitas seni yang sesungguhnya. Selain itu, program juga
menampilkan 10 negara (kebangsaan) dengan jumlah seniman
terbanyak dalam koleksi MoMA, dengan peringkat yang paling mendominasi adalah Negara Amerika.

Tahapan analisis yang dilakukan program (main.py & utils.py):
1. Memuat dataset dari file dataset/artists.csv.
2. Membersihkan data (menangani nilai kosong pada kolom
   Nationality dan Gender, serta membuang baris tanpa Birth Year).
3. Menghitung jumlah kelahiran seniman per dekade.
4. Menghitung top 10 negara (kebangsaan) dengan jumlah seniman
   terbanyak.
5. Membuat visualisasi berupa grafik garis (tren kelahiran per
   dekade) dan grafik batang (top 10 negara), disimpan sebagai
   grafik_line.png dan grafik_bar.png.
6. Menyimpan ringkasan hasil analisis ke dalam file
   hasil_analisis.txt.

PANDUAN SINGKAT MENJALANKAN PROGRAM
------------------------------------
1. Pastikan Python 3 sudah terinstal di komputer Anda.
2. Install pustaka (library) yang dibutuhkan, contoh:
   pip install pandas matplotlib
3. Pastikan struktur file adalah:
   proyek akhir st406
   |-dataset
   |  |-artists.csv
   |-main.py
   |-README.txt
   |-utils.py
4. Buka VS Code atau software semacamnya.
5. Buka file main.py lalu run sebagai python file.
6. Program analisis dan grafik akan tampil pada folder
   (grafik_line.png, grafik_bar.png, dan hasil_analisis.txt).

========================================================
