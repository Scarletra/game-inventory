
1. Perbedaan form POST dan GET dalam konteks Django umunya terletak pada fungsinya yang mana POST berguna 
   untuk mengirim data baru ke DB. Sedangkan, GET digunakan untuk mengambil data yang sudah disimpan
   Perbedaan lainnya terletak pada visibilitas dan panjang data. GET biasanya biasanya digunakan untuk       
   mengambil data yang tidak _private_ dan memiliki batas data yang dapat diambil sekaligus. Di sisi lain, 
   POST biasanya digunakan untuk mengirim data yang bersifat _sensitive_ seperti username ataupun password dan 
   juga dapat mengirim data dalam jumlah yang tidak ada batasan.

2. XML biasanya digunakan untuk mengirim data yang kompleks dan perlu validasi
   JSON biasanya digunakan untuk mengirim data yang ringan. Disajikan dalam bentuk key:value
   HTML biasanya digunakan untuk memproses pembuatan website

3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena sifatnya yang ringan, mudah dibaca, dan terintegrasi dengan baik dengan 
   bahasa JavaScript.

4. a. Membuat folder _templates_ yang isinya adalah base.html sebagai template untuk file html lainnya. Lalu, buat file forms.py
   b. Menambahkan semua fungsi yang dibutuhkan pada file views.py. Sebagai contoh funct show_xml yang akan mengambil semua data dan ditampilkan dalam bentuk 
      xml. Contoh lain adalah funct show_xml_by_id yang akan mengambil data berdasarkan id dari objek yang disimpan dan akan ditampilkan di web
   c. Menambahkan path baru yang disesuaikan dengan bagian yang ingin kita tampilkan pada website di file urls.py yang ada di dalam direktori main


1. ![image](https://github.com/Scarletra/game-inventory/assets/112821721/b761da56-2eb8-4d46-903c-2f1944f1097e)
2. ![image](https://github.com/Scarletra/game-inventory/assets/112821721/2bdf72da-d58c-4df9-a11e-851fdeeb66c1)
3. ![image](https://github.com/Scarletra/game-inventory/assets/112821721/c99a2502-99b8-4df2-bd23-a9d4f80bdd97)
4. ![image](https://github.com/Scarletra/game-inventory/assets/112821721/b134552e-90d0-43f9-ade5-346b2aa9977a)
5. ![image](https://github.com/Scarletra/game-inventory/assets/112821721/cdc4b4c9-943a-448a-a9fc-c4f5b012d5ba)
