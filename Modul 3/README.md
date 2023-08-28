## **Saudi Arabia Used Cars**

Source: [Saudi Arabia Used Cars Dataset](https://www.kaggle.com/datasets/turkibintalib/saudi-arabia-used-cars-dataset)

**Context**

Sebagai negara terbesar di Timur Tengah, Arab Saudi terkenal akan harga bahan bakar yang rendah. Bahkan, harga bahan bakarnya termasuk yang terendah di skala global. Selain itu, Arab Saudi juga terkenal akan cuacanya yang panas. Hal ini menjadikan mobil menjadi pilihan utama untuk mobilitas sehari-hari bagi sebagian besar orang di Arab Saudi. Akan tetapi, harga mobil baru akan lebih mahal jika dibandingkan dengan mobil bekas. Sejumlah artikel pun mengindikasikan bahwa pasar mobil bekas di Arab Saudi mengalami permintaan dua kali lipat lebih tinggi dibandingkan mobil baru. Permintaan yang signifikan terhadap mobil bekas telah menciptakan sejumlah platform daring (online platform) untuk jual beli mobil bekas, seperti halnya pada e-commerce syarah.com.

Syarah.com merupakan suatu platform yang menghadirkan dan menjual lebih dari 50 merek mobil yang tersebar di lebih dari 20 kota di Arab Saudi. Platform ini berfungsi sebagai perantara antara pemilik mobil dan calon pembeli mobil. Model bisnis yang diadopsi oleh platform ini mengizinkan para pemilik mobil untuk menetapkan harga jual mobil mereka secara mandiri, namun hal ini dapat memberikan tantangan tersendiri bagi para pemilik mobil. Kumpulan data yang digunakan dalam analisis ini terdiri dari 5624 entri mobil bekas yang terhimpun melalui Syarah.com. Setiap baris data mewakili sebuah mobil bekas dan mencakup informasi mengenai nama merk, model, tipe transmisi (gear type), tahun pembuatan, asal, opsi, kapasitas mesin, jarak yang ditempuh mobil, harga mobil, dan status negosiasi.

Melalui platform ini, konsumen memiliki kesempatan untuk memilih mobil yang sesuai dengan preferensi mereka. Harga yang ditawarkan berkaitan dengan spesifikasi pada setiap mobil. Ragam jenis mobil yang beragam juga tersedia dengan berbagai spesifikasi unik. Penentuan harga yang tepat sangatlah penting dalam proses jual beli mobil, baik dari sisi penjual maupun pembeli, guna menghindari kesalahan dalam pengambilan keputusan. Langkah ini sangat krusial, karena penetapan harga terlalu tinggi dapat menghambat proses penjualan, sementara penetapan harga terlalu rendah dapat mengurangi potensi keuntungan yang diperoleh.

**Problem Statement**


Bagi CEO perusahaan syarah.com, salah satu tantangan utama dalam penjualan mobil bekas adalah menemukan solusi yang menguntungkan secara finansial antara pemilik mobil (penjual) serta pembeli (harga yang sesuai) dan juga memberikan pengalaman yang positif bagi pembeli maupun penjual. Menjaga keseimbangan harga menjadi hal krusial karena harga yang terlalu tinggi (overprice) berisiko mengurangi minat pembeli dan mendorong mereka mencari alternatif platform lain, tetapi harga yang terlalu rendah (underprice) dapat mengakibatkan kerugian atau keuntungan yang tak memadai bagi pemilik mobil.

**Goals**

Menghadapi tantangan dari stakeholder kali ini, CEO syarah.com, goal yang diharapkan adalah memiliki alat yang mampu memprediksi harga mobil bekas yang kompetitif dan akurat berdasarkan spesifikasi yang diinginkan oleh pembeli. Alat ini akan membantu pelanggan dalam menemukan mobil bekas impian mereka secara aman dan nyaman dengan spesifikasi yang diharapkan, sekaligus harga yang sesuai dengan preferensi mereka. Faktor-faktor yang dapat mempengaruhi harga mobil, seperti merk mobil, tipe mobil, gear type, asal mobil, tahun mobil, jarak tempuh, hingga engine size, diharapkan mampu memberikan tingkat akurasi yang tinggi dalam penentuan harga mobil. Dengan cara ini, diharapkan bahwa harga yang ditawarkan akan tetap bersaing dan terjangkau bagi pembeli, sementara tetap memberikan keuntungan bagi pemilik mobil dan juga syarah.com.

**Analytic Approach**

Dalam menghadapi permasalahan tersebut, tindakan yang dapat dilakukan adalah melakukan analisis data dengan tujuan mengidentifikasi pola-pola dalam fitur-fitur yang membedakan satu mobil dari yang lain. Selanjutnya, mengembangkan suatu model regresi yang bertujuan untuk memberikan perusahaan alat prediksi harga bagi mobil bekas yang baru ditambahkan ke dalam daftar. Alat ini akan menjadi sumber yang berharga bagi syarah.com dalam menetapkan harga mobil bekas dengan kompetitif dan akurat, sehingga risiko underprice atau overprice dapat dihindari.

**Metric Evaluation**

Pada model kali ini, penghapusan outlier hanya dilakukan pada data outlier dengan nilai yang ekstrem dan kurang sesuai dengan domain knowledge. Dengan demikian, sejumlah outlier masih akan terdapat dalam data. Hal ini menyebabkan metrik evaluasi model yang akan digunakan tidak begitu sensitif terhadap adanya outlier.

Oleh karena itu, beberapa metrik evaluasi yang relevan dalam model ini mencakup:

- MAPE (Mean Absolute Percentage Error)

Mengukur rata-rata persentase selisih absolut antara prediksi dan nilai aktual. MAPE berbeda dari MAE, karena MAPE akan mengubah selisih menjadi persentase. Dikarenakan dalam bentuk persentase, nilai metrik ini berada dalam rentang 0 hingga 1.

- MAE (Mean Absolute Error)

Mengukur selisih rata-rata absolut antara nilai prediksi dan nilai aktual. Metrik ini direkomendasikan untuk digunakan karena data masih mengandung outlier. MAE tidak memperhatikan selisih yang menghasilkan nilai negatif. Semakin kecil nilai MAE, maka semakin baik prediksi model.

- RMSLE (Root Mean Squared Log Error)

Direkomendasikan untuk digunakan ketika data memiliki skewness yang tinggi dengan variasi yang bervariasi dari kecil hingga besar. RMSLE mengubah data menjadi skala logaritmik, lalu menghitung rata-ratanya dan mengambil akar kuadrat. Karena sifat logaritmik, metrik ini cenderung lebih tahan terhadap perbedaan yang besar.

- R-Squared

Metrik ini mengukur seberapa besar proporsi varians dalam data target dapat dijelaskan oleh model. Semakin tinggi nilainya, semakin baik model mampu menjelaskan variasi dalam data observasi. Metrik ini lebih sesuai digunakan saat memilih model dasar karena dapat menunjukkan seberapa besar pengaruh fitur terhadap target.

Metrik lainnya seperti RMSE (Root Mean Squared Error), MSE (Mean Squared Error), RMPSE (Root Mean Square Percentage Error) kurang cocok digunakan dalam konteks ini karena sensitivitas terhadap adanya outlier. Outlier memiliki dampak signifikan pada metrik-metrik tersebut karena mereka menghitung perbedaan kuadrat atau persentase antara prediksi dan aktual. Dalam hal ini, menggunakan metrik evaluasi yang lebih stabil terhadap outlier seperti MAE merupakan pendekatan yang lebih tepat. Dengan demikian, evaluasi kualitas prediksi model akan lebih akurat dan informatif.

**Data Understanding**

- Dataset merupakan data mobil bekas di Arab Saudi.
- Setiap baris data merepresentasikan informasi terkait mobil bekas yang akan dijual seperti, harga, tipe, dan beberapa spesifikasi lainnya.
