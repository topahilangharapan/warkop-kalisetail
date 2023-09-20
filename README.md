# Warkop Kalisetail
**Selamat datang di warkop _Stasiun Kalisetail_ (+272m)**

## Tautan Adaptable
https://warkop-kalisetail.adaptable.app

## Tugas 2
- [x] **Membuat sebuah proyek Django baru.**

   Mengaktifkan Virtual Environment pada direktori warkop_kalisetail, hal ini dilakukan supaya kita berhati-hati saat memasang dependencies (yang berisi library, framework, atau package untuk membantu proses pengembangan) dengan mengisolasi dependencies antara proyek proyek yang berbeda. Lalu, kita buat proyek Django dan mengonfigurasi proyek dengan mengubah `ALLOWED_HOSTS` di file `settings.py` supaya kita terdaftar menjadi host yang memiliki izin untuk mengakses aplikasi web.

- [x] **Membuat aplikasi dengan nama `main` pada proyek tersebut.**

  Jalankan perintah:
  ```
  python3 manage.py startapp main
  ```
  pada direktori utama warkop_kalisetail untuk membuat folder bernama `main` yang berisikan struktur awal aplikasi `main` milik kita.
      
- [x]  **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.**
   
   Untuk memasukkan aplikasi `main` yang telah kita buat tadi ke dalam proyek _warkop kalisetail_, kita membuka file `settings.py` dan menambahkan `'main'` (nama aplikasi yang kita buat tadi) pada variabel `INSTALLED_APPS`.
         
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
      
   Kita mengkonfirugasi routing URL proyek warkop_kalisetail dengan menambahkan rute URL `urls.py` pada direktori proyek `warkop_kalisetail` yang akan kita hubungkan ke tampilan `main`. Impor fungsi `include` dari `django.urls`, fungsi ini akan mengimpor URL dari aplikasi lain (kasus ini aplikasi `main`) ke dalam file `urls.py` proyek warkop_kalisetail. Tambahkan rute URL `path('main/', include('main.urls'))` pada variabel `urlpatterns`, path URL `'main/'` akan diarahkan ke rute URL yang dibuat tadi pada file `urls.py` di aplikasi `main`. File `urls.py` pada aplikasi `main` bertugas untuk mengatur rute URL spesifik yang dibutuhkan oleh fitur-fitur aplikasi `main` sedangkan `urls.py` pada proyek warkop_kalisetail bertugas untuk mengarahkan rute URL proyek dan akan mengimpor rute URL dari file `urls.py` aplikasi-aplikasi bila dibutuhkan.

  Konfigurasikan routing URL aplikasi `main` yang telah kita buat tadi dengan membuat file `urls.py` pada direktori `main`, file ini yang akan mengatur rute URL milik aplikasi `main`. Impor fungsi `path` dari `django.urls`, fungsi ini berguna untuk membuat URL. Impor juga fungsi `show_main` dari `main.views` untuk menampilkan tampilan ketika URL terkait diakses. Buat nama `app_name` untuk memberikan nama unik pada pola URL pada aplikasi. Gunakan fungsi `show_main` untuk menampilkan URL terkait ketika diakses dengan membuat variabel `urlpatterns` menjadi:
   ```
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```

- [x] **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

  Pastikan file proyek warkop_kalisetail sudah memiliki repositori di `GitHub` dengan nama `warkop_kalisetail`. Kita buka website Adaptable lalu pilih `Create New App` dan pilih opsi `Connect Git Repository` lalu pilih repository `warkop_kalisetail`, pilih branch `main` lalu pilih `Python App Template` sebagai Deploy Template-nya, Gunakan Database Type `Postgre SQL` dan pilih python version sesuai dengan yang digunakan (`3.11`) dan mengisi start command dengan perintah `python manage.py migrate && gunicorn warkop_kalisetail.wsgi`. Masukkan nama aplikasi, yaitu `warkop_kalisetail`, nama ini juga akan menjadi nama domainnya, terakhir centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment.
      
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

## Tugas 3
- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

   Buat file di direktori `main` bernama `forms.py` lalu tambahkan `Product` (yang ada pada `models.py`) supaya isi dari form akan disimpan menjadi objek `Product` dengan meminta              `fields` yang sesuai pada `models.py`.
   Buka file `views.py` di direktori `main` juga dan meng-import beberapa fungsi:
   ```
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse
   ```
   Lalu buat fungsi baru bernama `create_product` yang menerima parameter `request`, isi dari `create_product` adalah:
   ```
   def create_product(request):
      form = ProductForm(request.POST or None)
      
      if form.is_valid() and request.method == "POST":
         form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
      
      context = {'form': form}
      return render(request, "create_product.html", context)
   ```
   `form = ProductForm(request.POST or None)` berguna untuk membuat `ProductForm` baru dengan cara memasukkan QueryDict sesuai pada input _user_ di `request.POST`. `form.is_valid()` ditambahkan supaya dapat mengecek apakah isi input di form tersebut valid atau tidak. `form.save()` berguna untuk membuat sekaligus menyimpan data dari form. `return HttpResponseRedirect(reverse('main:show_main'))` untuk me-redirect user kembali ke halaman utama setelah menyimpan data form.
   
 
- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
      
   * **HTML**

      Dalam folder `templates` di root folder dan buat file HTML baru dengan nama `base.html` sebagai template dasar yang digunakan sebagai kerangka umum untuk halaman-halaman web lainnya pada proyek. Pada `base.html` isi dengan:
      ```
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
          <head>
              <meta charset="UTF-8" />
              <meta
                  name="viewport"
                  content="width=device-width, initial-scale=1.0"
              />
              {% block meta %}
              {% endblock meta %}
          </head>
      
          <body>
              {% block content %}
              {% endblock content %}
          </body>
      </html>
      ```
      Buka file `settings.py` yang ada di subdirektori `warkop_kalisetail` dan cari variabel `TEMPLATES` lalu tambahkan code ini supaya `base.html` data dideteksi sebagai template:
      ```
      'DIRS': [BASE_DIR / 'templates']
      ```
      Pada subdirektori `templates` yang ada di `main` ubah `main.html` menjadi:
      ```
      {% extends 'base.html' %}
      
      {% block content %}
         <h1>Warkop Kalisetail</h1>
         
         <h3>Appname: </h3>
         <p>{{ appname }}</p>
         
         <h5>Name:</h5>
         <p>{{ nama }}</p>
         
         <h5>Kelas:</h5>
         <p>{{ kelas }}</p>
      {% endblock content %}
      ```
      Pada file `views.py` ubah fungsi `show_main` dengan menambahkan `products = Product.objects.all()` untuk mengambil seluruh objek Product yang ada di _database_ lalu tambahkan `'products': products` pada variabel `context` untuk menampilkan seluruh objek Product yang ada di _database
      Buat file baru dengan nama `create_product.html` di direktori `main/templates`. Isi dengan kode:
      ```
      {% extends 'base.html' %} 
   
      {% block content %}
      <h1>Add New Product</h1>
      
      <form method="POST">
          {% csrf_token %}
          <table>
              {{ form.as_table }}
              <tr>
                  <td></td>
                  <td>
                      <input type="submit" value="Add Product"/>
                  </td>
              </tr>
          </table>
      </form>
      
      {% endblock %}
      ```
      `<form method="POST">` untuk menandakan block mana yang digunakan untuk form dengan metode POST. `{% csrf_token %}` bertanggung jawab menjadi token untuk menjaga keamanan supaya tercegah dari serangan berbahaya. `{{ form.as_table }}` untuk menampilan fields pada form yang sudah dibuat di file `forms.py` sebagai tabel. `<input type="submit" value="Add Product"/>` menjadi tombol submit untuk mengirimkan request ke view `create_product(request)`.
      Buka file `main.html` dan tambahkan kode di dalam `{% block content %}` supaya dapat menampilkan data produk dalam bentuk tabel sekaligus tombol "Add New Product" yang akan me-redirect ke halaman form:
      ```
      ...
      <table>
          <tr>
              <th>Name</th>
              <th>Amount</th>
              <th>Price</th>
              <th>Description</th>
          </tr>
      
          {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
      
          {% for product in products %}
          <tr>
              <td>{{product.name}}</td>
              <td>{{product.amount}}</td>
              <td>{{product.price}}</td>
              <td>{{product.description}}</td>
          </tr>
          {% endfor %}
      </table>
      
      <br />
      
      <a href="{% url 'main:create_product' %}">
          <button>
              Add New Product
          </button>
      </a>
      
      {% endblock content %}
      ```

   * **Serializer untuk XML dan JSON**
     
        Buka file `views.py` pada direktori `main` lalu impor fungsi `HttpResponse` dan fungsi `Serializer` yang digunakan untuk menerjemahkan objek model menjadi format lain (seperti XML atau JSON).

   * **XML**

        Buat fungsi `show_xml` yang menerima parameter _request_ dan buat variabel `data` yang akan menyimpan hasil query dari seluruh data yang ada di `Product` lalu return functionnya adalah `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi dalam format XML dan parameter `content_type="application/xml".`.

   * **JSON**
     
        Buka file `views.py` di folder `main` lalu buat fungsi baru bernama `show_json` dengan variabel `data` yang akan menyimpan seluruh hasil query data yang ada pada `Product`. Tambahkan return function berupa `HttpResponse` yang memiliki paramater data hasil query yang udah diserialisasi menjadi JSON dan parameter `content_type="application/json"`.

   * **ID XML dan JSON**
     
        Buka file `views.py` di folder `main` lalu buat fungsi baru bernama `show_xml_by_id` dan `show_json_by_id` dengan variabel `data` yang akan menyimpan hasil query data dengan id tertentu yang ada pada `Product`. Tambahkan return function berupa `HttpResponse` yang memiliki paramater data hasil query yang udah diserialisasi menjadi JSON atau XML dan parameter `content_type` yang sesuai dengan format XML atau JSON (format XML: `"application/xml"` atau format JSON: `"application/json"`).

- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.

    Buka file `urls.py` pada folder `main` dan impor fungsi `create_product, show_xml, show_json` tadi dari `views.py` sekaligus tambahkan path url:
   ```
   ...
   path('create-product', create_product, name='create_product'),
   path('xml/', show_xml, name='show_xml'),
   path('json/', show_json, name='show_json')
   path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
   ...
   ```
   ke dalam variabel `urlpatterns` untuk bisa menggunakan fungsi yang sudah diimpor tadi.

- [x] Apa perbedaan antara form `POST` dan form `GET` dalam Django?
   1. **PENGGUNAAN**
        * GET
          
             Digunakan untuk mengambil data dari server. Data yang dikirimkan melalui metode GET akan muncul dalam URL, sehingga lebih mudah dilihat oleh pengguna dan dapat dibagikan. GET sering digunakan untuk permintaan pencarian atau navigasi halaman web.
        * POST
          
            Digunakan untuk mengirim data ke server. Data yang dikirimkan melalui metode POST tidak terlihat dalam URL, sehingga lebih aman dan sesuai digunakan untuk mengirim data sensitif seperti kata sandi atau informasi pribadi.

   2. **METODE PENGIRIMAN**
        * GET
          
             Data dikirim sebagai parameter dalam URL. Data ini akan terlihat di baris URL dan biasanya digunakan untuk mengirim data yang tidak sensitif, seperti parameter pencarian atau filter.    
        * POST
          
             Data  dikirim sebagai bagian dari permintaan HTTP POST. Data ini tidak akan muncul di URL dan biasanya digunakan untuk mengirim data yang bersifat sensitif atau besar, seperti kata sandi atau unggahan file.
   3. **KEAMANAN**
        * GET
       
             Kurang aman karena data dikirimkan dalam URL dan dapat terlihat oleh orang lain. Tidak boleh digunakan untuk data sensitif.
        * POST
          
             Lebih aman karena data tidak terlihat dalam URL dan tidak mudah diakses oleh pihak ketiga

   4. **CACHING**
        * GET
          
             GET dapat disimpan dalam cache, karena permintaan GET bersifat idempoten (tidak mengubah data server). Namun, ini juga berarti bahwa permintaan GET dapat disajikan dari cache dan tidak selalu mengambil data terbaru dari server.
        * POST
          
             POST tidak dapat disimpan dalam cache, karena permintaan POST dapat mengubah data server.

- [x] Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
   1. **XML (eXtensible Markup Language)**

         * XML adalah bahasa yang dirancang untuk mendefinisikan struktur dokumen. XML menggunakan tag untuk menandai elemen-elemen dalam dokumen dan menggambarkan hierarki data.
         * XML biasanya digunakan untuk pertukaran data antar aplikasi dan platform yang berbeda. Ini digunakan dalam berbagai domain, termasuk sebagai format penyimpanan data, konfigurasi, dan dalam protokol web services.
         * XML digunakan ketika perlu mendefinisikan struktur data yang kompleks, sering kali dengan skema yang telah ditentukan sebelumnya.
   2. **JSON (JavaScript Object Notation)**

         * JSON adalah format data yang menggunakan pasangan nama dan nilai untuk merepresentasikan objek. Ini lebih mudah dibaca oleh manusia dan lebih sederhana dibandingkan dengan XML.
         * JSON digunakan untuk pertukaran data antar aplikasi, terutama dalam lingkungan web. Ini adalah format yang umum digunakan dalam komunikasi antara perangkat lunak berbasis JavaScript (seperti aplikasi web) dan server web.
         * JSON sering digunakan untuk mengirim data dinamis dari server ke browser atau antar server dalam format yang mudah diurai oleh perangkat lunak.
   3. **HTML (Hypertext Markup Language)**
         * HTML adalah bahasa markup yang digunakan untuk membuat dokumen web. Ini berfokus pada merepresentasikan konten dan struktur halaman web.
         * HTML digunakan untuk membuat tampilan halaman web yang dapat diakses oleh pengguna melalui browser web. Ini adalah bahasa yang digunakan untuk mendefinisikan elemen-elemen tampilan web seperti teks, gambar, tautan, formulir, dll.
         * HTML seringkali digunakan dalam pengembangan web, untuk membuat halaman web yang dapat diakses dan diinterpretasi oleh peramban web. HTML bukan format yang digunakan untuk pertukaran data, melainkan untuk membuat antarmuka pengguna atau UI.

- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.

   * **HTML**
        <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/01053ec2-1798-4b63-b054-00aef7dd63d5">

   * **XML**
        <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/a8faeee9-19d7-4667-81f6-5ba450bce8bd">

   * **JSON**
        <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/c0226f96-afbb-410f-aa22-83eb68439466">

   * **XML by ID**
        <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/d250a5fb-a4b3-4dec-b5e1-f4b702fc78f3">

   * **JSON by ID**
        <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/7d2c10a0-3ac9-4b8c-a44f-f6e62476053d">

     
   
   
        
        
