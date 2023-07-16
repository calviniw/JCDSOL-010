# **New York City TLC Trip Record**

## **Latar Belakang**
Di Amerika Serikat lebih tepatnya di kota New York, semua kendaraan taksi dikelola oleh TLC (Taxi and Limousine Commission). Didirikan sejak tahun 1971, Komisi Taksi dan Limusin Kota New York (TLC) adalah agensi yang bertanggung jawab untuk melisensikan dan mengatur taksi Medallion di kota New York (berwarna kuning), kendaraan untuk disewa secara khusus (khusus komunitas, mobil hitam dan limusin mewah), van komuter, dan kendaraan paratransit (untuk disabilitas/berkebutuhan khusus).

Sebuah perusahaan yang menjadi salah satu vendor dari TLC di kota New York, Amerika Serikat adalah VeriFone Inc. dimana perusahaan ini memfasilitasi pencatatan data setiap trip taxi yang berada di kota tersebut.

Dari banyaknya area lokasi penjemputan penumpang (pickup customer location) di kota New York, pada umumnya tidak semua area lokasi penjemputan tersebut ramai penumpang.


## **Pernyataan Masalah**
Stackholder adalah seorang manajer dari perusahaan VeriFone Inc.

Stackholder ingin meningkatkan profit perusahaan dengan cara mengetahui area lokasi penjemputan penumpang manakah yang paling teramai di kota New York. Informasi ini akan membantu perusahaan untuk meningkatkan efektifitas penempatan taksi di area yang memiliki jumlah penjemputan tertinggi sehingga harapannya mampu meningkatkan profit perusahaan.

Sebagai seorang Data Analyst, kita akan mencoba menjawab pertanyaan berikut:

Bagaimanakah cara meningkatkan profit perusahaan dan meningkatkan efektifitas lokasi pickup customer?


## **Data**
Untuk menjawab pertanyaan di atas,
Kita akan melakukan analisa data New York City TLC Trip Record.

Dataset dapat diakses [di sini](https://drive.google.com/drive/folders/1NYHIL-RgVPW-HONz4pdzlcbIChF-c37N).

## Kesimpulan dan Rekomendasi

### Kesimpulan
1. Lokasi pickup saat ini masih kurang efisien (48%).
2. Id Lokasi Pickup 74 memiliki jumlah trip tertinggi dari yang lainnya.
3. Terdapat sebanyak 18 lokasi area yang berbeda yang jumlah tripnya hanya 1x dan masih kurang efisien.
4. Jumlah Trip Dispatch (memesan terlebih dahulu) sangat sedikit (2.5%) jika dibandingkan dengan Street-hail (memesan langsung di jalan).
5. Hari selasa merupakan hari paling ramai berdasarkan jumlah trip dan hari minggu adalah hari yang paling sepi.
6. Jam trip paling ramai dari jumlah trip mulai dari jam 12 siang hingga 20 malam dan jam paling sepi dari jumlah trip dari jam 0 dini hari hingg 6 pagi.
7. Jumlah penumpang yang hanya berisi 1 penumpang dengan 1x Trip menjadi yang paling banyak dengan 46,465 orang.
8. ID lokasi pickup 74 dan 75 adalah lokasi yang memiliki jumlah trip terbanyak dengan jumlah customer lebih dari 4 orang per 1x trip nya.
9. Terdapat peningkatan income secara perlahan di setiap minggu nya pada bulan January 2023.


### Rekomendasi
Berdasarkan hasil analisa pada data New York City TLC Trip Record, untuk meningkatkan efektifitas lokasi pickup customer dan dapat meningkatkan profit perusahaan, dapat dilakukan beberapa cara seperti:

1. Mengalokasikan lebih banyak jumlah taksi pada lokasi pickup dengan jumlah trip tertinggi seperti pada ID Lokasi Pickup 74.
2. Memfokuskan pada waktu paling ramai mulai pukul 12 siang hingga 20 malam terutama pada hari selasa karena merupakan hari paling ramai berdasarkan jumlah trip.
3. Meningkatkan kualitas dan performa aplikasi maupun layanan pesan terlebih dahulu agar dapat meningkatkan profit dan efektifitas lokasi pickup customer.
4. Memfokuskan pada ID Lokasi Pickup 74 dan 75 untuk jumlah customer lebih dari 4 orang per 1x tripnya karena memiliki jumlah trip terbanyak dibanding lainnya.
