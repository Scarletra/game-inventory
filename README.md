# game-inventory
Tugas 5 PBP

Name: Fernando Valentino Sitinjak
Class: PBP F
Student ID: 2206081332

Tautan aplikasi: https://growtopia-shop.adaptable.app/

1. + Universal selector (*), berguna untuk memilih semua elemen pada file. Waktu yang tepat untuk menggunakannya adalah pada saat ingin memodifikasi file secara keseluruhan/global.
   + Type selector (<div>, <h1>, <p>, dll), berguna untuk memilih elemen sesuai tipe. Waktu yang tepat digunakan adalah saat ingin memodifikasi tipe tertentu.
   + Class selector (class="" -> .classname), berguna untuk memilih elemen sesuai dengan nama class yang ingin dimodifikasi. Waktu yang tepat digunakan adalah saat ingin memodifikasi elemen dengan nama kelas tertentu yang sudah ditentukan.
   + ID selector (id="" -> #id), berguna untuk memilih elemen sesuai dengan ID unik yang sudah ditentukan. Waktu yang tepat digunakan adalah saat ingin memodifikasi elemen dengan ID yang diinginkan.
   + Attribute selector ("[attribute]"), berguna untuk memilih elemen sesuai atribut atau nilai atribut yang dipilih. Waktu yang tepat digunakan adalah saat ingin memodifikasi elemen dengan atribut atau nilai atribut tertentu.
   + Descendant selector ('parent child'), berguna untuk memilih elemen anak yang ada dalam element parent. Waktu yang tepat digunakan adalah saat ingin memodifikasi elemen anak yang ada di dalam elemen parent tertentu.
   + Pseudo-class selector (":hover", dll), berguna untuk memilih elemen dengan kondisi tertentu. Waktu yang tepat digunakan adalah saat ingin memodifikasi elemen pada suatu kondisi tertentu.

2. + <html>, tag yang berfungsi menandakan awal dan akhir dari suatu file HTML. Semua elemen HTML yang kita ingin tampilkan akan dibuat di dalam tag ini.
   + <head>, tag yang berisikan informasi tentang dokumen kita, seperti judul laman, referensi file, dan lainnya.
   + <body>, tag yang berisikan elemen yang akan ditampilkan di laman web kita.
   + <a>, tag untuk menandakan teks yang mereferensikan ke suatu URL.
   + <p>, tag untuk menampilkan teks dalam bentuk paragraf.
   + <h1, ...., h5>, tag untuk menampilkan teks dalam ukuran tertentu.
   + <img>, tag yang berguna untuk menampilkan sebuah gambar.
   + <ul>, tag untuk membuat daftar yang tidak memiliki urutan (unordered list).
   + <li>, tag untuk membuat daftar dengan sebuah urutan (ordered list).
   + <table>, tag untuk membuat suatu table dengan baris dan kolom.

3. Margin :

   Padding :

4. **Bootstrap**
   Bootstrap merupakan framework yang lebih mudah digunakan bagi orang yang kurang memiliki pengalaman dalam menggunakan CSS. Bootstrap menyediakan banyak komponen yang dapat disesuaikan dengan mudah. Namun, jika ingin memodifikasi apa yang sudah disediakan, diperlukan adanya kustomisasi CSS lebih lanjut.

   **Tailwind CSS**
   Tailwind CSS merupakan framework yang mengutamakan utilitas, sehingga hal ini menyebabkan kita menjadi lebih fleksibel dalam membuat atau memodifikasi sesuatu, tetapi memerlukan pengetahuan CSS yang luas. Kita juga dapat dengan mudah melakukan kustomisasi terhadap komponen-komponen yang ingin kita modifikasi.

5. + Kustomisasi halaman login, register, dan tambah inventori

      1. Menambahkan link yang menunjuk ke file CSS yang bersesuaiaan
      ```html
      <link rel="stylesheet" href="{% static 'login.css' %}">
      <link rel="stylesheet" href="{% static 'register.css' %}">
      <link rel="stylesheet" href="{% static 'myfirst.css' %}">
      ```

      2. Mengatur isi CSS sesuai dengan keinginan kita e.g login.css
      ```css
      ## login.css file
      * {
         background-color: #74FCB8;
      }
      ```

      3. Kustomisasi halaman daftar item menjadi lebih menarik dengan menggunakan Card

      Mengganti isi for loop dari Items yang awalnya menggunakan tabel menjadi bentuk Card
