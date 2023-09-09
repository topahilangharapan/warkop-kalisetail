# Warkop Kalisetail
**Selamat datang di warkop _Stasiun Kalisetail_ (+272m)**

## Tautan Adaptable


## Tugas 2
- [x] **Membuat sebuah proyek Django baru.**

   Mengaktifkan Virtual Environment pada direktori warkop_kalisetail, hal ini dilakukan supaya kita berhati-hati saat memasang dependencies (yang berisi library, framework, atau package untuk membantu proses pengembangan) dengan         mengisolasi dependencies antara proyek proyek yang berbeda. Lalu, kita buat proyek Django dan mengonfigurasi proyek dengan mengubah `ALLOWED_HOSTS` di file `settings.py` supaya kita terdaftar menjadi host yang memiliki izin untuk mengakses aplikasi web.

- [x] **Membuat aplikasi dengan nama `main` pada proyek tersebut.**

  Jalankan perintah:
  ```
  python3 manage.py startapp main
  ```
  pada direktori utama warkop_kalisetail untuk membuat folder bernama `main` yang berisikan struktur awal aplikasi `main` milik kita. Lalu untuk memasukkan aplikasi `main` yang telah kita buat tadi ke dalam proyek _warkop kalisetail_, kita membuka file `settings.py` dan menambahkan `'main'` (nama aplikasi yang kita buat tadi) pada variabel `INSTALLED_APPS`.
      
- [x]  **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.**

  Kita mengkonfirugasi routing URL proyek warkop_kalisetail dengan menambahkan rute URL `urls.py` pada direktori proyek `shopping_list` yang akan kita hubungkan ke tampilan `main`. Impor fungsi `include` dari `django.urls`, fungsi ini akan mengimpor URL dari aplikasi lain (kasus ini aplikasi `main`) ke dalam file `urls.py` proyek warkop_kalisetail. Tambahkan rute URL `path('main/', include('main.urls'))` pada variabel `urlpatterns`, path URL `'main/'` akan diarahkan ke rute URL yang dibuat tadi pada file `urls.py` di aplikasi `main`. File `urls.py` pada aplikasi `main` bertugas untuk mengatur rute URL spesifik yang dibutuhkan oleh fitur-fitur aplikasi `main` sedangkan `urls.py` pada proyek warkop_kalisetail bertugas untuk mengarahkan rute URL proyek dan akan mengimpor rute URL dari file `urls.py` aplikasi-aplikasi bila dibutuhkan.
         
- [x]  **Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.**
      
  * `name` sebagai nama item dengan tipe `CharField`.
  * `amount` sebagai jumlah item dengan tipe `IntegerField`.
  * `description` sebagai deskripsi item dengan tipe `TextField`.
     
    Modifikasi file `models.py` pada aplikasi `main` untuk membuat model baru, kita membuat class Product sebagai nama model yang akan kita buat. Lalu kita menambahkan atribut `name`, `amount`, `description`, dan `price` pada model dengan tipe data (berurut) `CharField`, `IntegerField`, `TextField`, dan `IntegerField`. Supaya Django dapat mengetahui apabila ada perubahan pada model kita dapat melakukan migrasi, untuk membuat migrasi model, jalankan perintah:
    ```
    python3 manage.py makemigrations
    ```
    lalu untuk menerapkan migrasi tersebut ke dalam basis data lokal, kita jalankan:
    ```
    python3 manage.py migrate
    ```
    Sehingga perubahan model akan diketahui oleh Django.
    
- [x] **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**

  Buka file `views.py` pada aplikasi `main`, lalu impor fungsi `render` dari `django.shortcuts` untuk me-render tampilan HTML sesuai dengan data yang diberikan. Lalu buat fungsi `show_main` yang menerima parameter `request`, fungsi ini akan menguru permintaan HTTP dan memberikan tampilan yang sesuai. Buat variabel `context` sebagai _dictionary_ yang berisi data yang akan dikirimkan ke tampilan, dalam tugas ini ada dua data yaitu:
  * `name`: Data nama
  * `class`: Data kelas
  lalu untuk line return, tambahkan `return render(request, "main.html", context)` sehingga tampilan `main.html` akan ter-render dengan menggunakan fungsi `render` yang menggunakan parameter `context` sebagai data yang akan diteruskan ke tampilan sehingga penampilan dinamis.
      
- [x] **Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**
      
  Konfigurasikan routing URL aplikasi `main` yang telah kita buat tadi dengan membuat file `urls.py` pada direktori `main`, file ini yang akan mengatur rute URL milik aplikasi `main`. Impor fungsi `path` dari `django.urls`, fungsi ini berguna untuk membuat URL. Impor juga fungsi `show_main` dari `main.views` untuk menampilkan tampilan ketika URL terkait diakses. Buat nama `app_name` untuk memberikan nama unik pada pola URL pada aplikasi. Gunakan fungsi `show_main` untuk menampilkan URL terkait ketika diakses dengan membuat variabel `urlpatterns` menjadi:
```
urlpatterns = [
    path('', show_main, name='show_main'),
]
```

- [x] **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

  Pastikan file proyek warkop_kalisetail sudah memiliki repositori di `GitHub` dengan nama `warkop_kalisetail`. Kita buka website Adaptable lalu pilih `Create New App` dan pilih opsi `Connect Git Repository` lalu pilih repository `warkop_kalisetail`, pilih branch `main` lalu pilih `Python App Template` sebagai Deploy Template-nya, Gunakan Database Type `Postgre SQL` dan pilih python version sesuai dengan yang digunakan (`3.11`) dan mengisi start command dengan perintah `python manage.py migrate && gunicorn shopping_list.wsgi`. Masukkan nama aplikasi, yaitu `warkop_kalisetail`, nama ini juga akan menjadi nama domainnya, terakhir centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment.
      
- [x] **Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**

  * **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
    
     <img width="841" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/dd394a74-3496-499f-a4cf-c09a8765f74d">

    Penjelasan:
    1. `Client (browser)` mengirimkan HTTP request ke URL tertentu dan ditangkap oleh `urls.py`
    2. `urls.py` mencocokkan URL yang diterima dari request dengan pola URL yang didefinisikan dalam file ini. Jika URL cocok dengan salah satu pola yang ada, `urls.py` mengarahkan request ke `views.py` yang sesuai.
    3. `views.py` dapat berinteraksi dengan `models.py` (jika diperlukan) untuk mengambil atau memanipulasi data dari database.
    4. `models.py` mengembalikan data dari database ke `views.py`
    5. `views.py` akan merender (memproses) berkas `HTML` dengan menggunakan data yang telah diperoleh dari `models.py`
    6. Hasil render `HTML` oleh `views.py` akan menghasilkan response yang dikirim kembali ke `Client (browser)`
    
  * **Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
    
    Kita menggunakan virtual environment dalam pengembangan aplikasi web berbasis Django karena:
      1. **Isolasi Proyek**: Ini memungkinkan environment yang terisolasi untuk setiap proyek, menghindari konflik dependencies.
      2. **Manajemen Dependensi**: Memudahkan pengelolaan paket Python yang digunakan oleh proyek.
      3. **Keamanan**: Mencegah paket antar proyek tercampur dan mengurangi risiko masalah yang tidak diketahui.
      4. **Portabilitas**: Memudahkan berbagi proyek dengan orang lain.
      5. **Pengujian**: Membantu pengujian proyek dalam environment yang terisolasi.
   
    Meskipun kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, mengelola dependencies dan proyek-proyek Anda akan lebih rumit dan berpotensi tinggi menimbulkan masalah. Oleh karena itu, sangat disarankan untuk selalu menggunakan virtual environment dalam pengembangan Django atau proyek Python lainnya.
    
  * **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
    
    MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi. Mereka memiliki konsep dasar yang serupa, yaitu memisahkan komponen aplikasi menjadi bagian-bagian yang berbeda untuk membantu pemahaman, pemeliharaan, dan pengujian. Namun, ada perbedaan penting dalam cara masing-masing pola ini diimplementasikan.
    1. **MVC (Model-View-Controller)**:
 
        * Model: Mewakili data dan logika aplikasi.
        * View: Bertanggung jawab untuk tampilan grafis atau antarmuka pengguna.
        * Controller: Mengatur interaksi antara Model dan View serta mengatur alur aplikasi.
   
        **Perbedaan**:
      
        * MVC adalah pola arsitektur yang umum digunakan dalam pengembangan perangkat lunak tradisional, seperti aplikasi desktop.
        * Controller adalah inti dari MVC dan berfungsi sebagai penghubung antara Model dan View.

    2. **MVT (Model-View-Template)**:
       
        * Model: Mewakili data dan logika aplikasi.
        * View: Menangani tampilan pengguna, tetapi dalam kerangka kerja Django, sebagian besar logika tampilan dikendalikan oleh Template.
        * Template: Bertanggung jawab untuk merender tampilan dan menggabungkan data dari Model.
      
        **Perbedaan**:
    
        * MVT adalah variasi dari MVC yang diterapkan secara khusus dalam kerangka kerja Django untuk pengembangan web.
        * Pada MVT, Template memiliki peran yang lebih besar dalam menangani tampilan dibandingkan dengan View.
      
    3. **MVVM (Model-View-ViewModel)**:
       
        * Model: Mewakili data dan logika aplikasi.
        * View: Merupakan tampilan grafis yang dilihat oleh pengguna.
        * ViewModel: Bertanggung jawab untuk mengelola data yang akan ditampilkan di View dan berfungsi sebagai jembatan antara Model dan View.
      
        **Perbedaan**:
    
        * MVVM adalah pola arsitektur yang umum digunakan dalam pengembangan aplikasi berbasis pemrograman berorientasi objek, seperti aplikasi desktop dan aplikasi mobile.
        * ViewModel adalah inti dari MVVM dan berperan sebagai penghubung antara Model dan View dengan cara yang lebih terstruktur dan terkendali dibandingkan dengan Controller dalam MVC.
      
    Perbedaan utama antara ketiga pola ini adalah cara mereka mengelola tampilan dan koneksi antara Model dan View/Template/ViewModel. MVC adalah pola yang umum digunakan dalam pengembangan tradisional, MVT adalah varian dari MVC yang digunakan dalam kerangka kerja web Django, dan MVVM adalah pola yang sering digunakan dalam pengembangan aplikasi berbasis objek, terutama di lingkungan seperti aplikasi desktop atau mobile. Pemilihan pola tergantung pada jenis aplikasi dan kerangka kerja yang digunakan.
