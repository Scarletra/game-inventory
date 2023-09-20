# game-inventory
Tugas 3 PBP

Tautan aplikasi: https://growtopia-shop.adaptable.app/

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

4. a.
   b. Menambahkan semua fungsi yang dibutuhkan pada file views.py. Sebagai contoh funct show_xml yang akan mengambil semua data dan ditampilkan dalam bentuk 
      xml. Contoh lain adalah funct show_xml_by_id yang akan mengambil data berdasarkan id dari objek yang disimpan dan akan ditampilkan di web
   c. Menambahkan path baru yang disesuaikan dengan bagian yang ingin kita tampilkan pada website di file urls.py yang ada di dalam direktori main


1. [/create_product] (html.jpg)
2. [/json] (json.jpg)
3. [/xml] (xml.jpg)
4. [/json/<int:id>] (json_byid.jpg)
5. [/xml/<int:id>] (xml_byid.jpg)
6.    
