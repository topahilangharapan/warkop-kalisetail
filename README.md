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

## Tugas 4
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1. **Registrasi**
   
   Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `register` dan memiliki parameter `request`. Lalu impor `redirect`, `UserCreationForm`, dan `messages`. Isi dari fungsi `register` adalah:
   ```
   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
   ```
   `form = UserCreationForm(request.POST)` untuk membuat variabel `form` yang dimana ia adalah `UserCreationForm` lalu kita masukkan QueryDict sesuai input dari user pada `request.POST`. `form.is_valid()` berguna untuk melakukan validasi pada input form. `form.save()` supaya data dari form dapat tersimpan. User dapat mengetahui apabila berhasil me-register dengan melihat pesan pada web karena kita menggunakan `messages.success(request, 'Your account has been successfully created!')`. Setelah user berhasil mendaftar, user akan kembali dari halaman register, jadi, kita menambahkan kode `return redirect('main:show_main')`.
   Halaman register akan kita buat dengan file `register.html` yang ada di folder `main/templates` dengan isi:
   ```
   {% extends 'base.html' %}
   
   {% block meta %}
       <title>Register</title>
   {% endblock meta %}
   
   {% block content %}  
   
   <div class = "login">
       
       <h1>Register</h1>  
   
           <form method="POST" >  
               {% csrf_token %}  
               <table>  
                   {{ form.as_table }}  
                   <tr>  
                       <td></td>
                       <td><input type="submit" name="submit" value="Daftar"/></td>  
                   </tr>  
               </table>  
           </form>
   
       {% if messages %}  
           <ul>   
               {% for message in messages %}  
                   <li>{{ message }}</li>  
                   {% endfor %}  
           </ul>   
       {% endif %}
   
   </div>  
   
   {% endblock content %}
   ```
   Tambahkan path url milik halaman register ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `register` dari `views.py` dan tambahkan `path('register/', register, name='register')` pada variabel `urlpatterns`.
   
   
2. **Login**
   
   Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `login_user` yang menerima parameter `request`. Lalu impor `authenticate` dan `login`. Isi dari fungsi `login` adalah:
   ```
   def login_user(request):
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('main:show_main')
           else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
       context = {}
       return render(request, 'login.html', context)
   ```
   `authenticate(request, username=username, password=password` berguna untuk melakukan autentikasi user dengan menggunakan username dan password yang diterima dari `request` yang dikirim user saat ingin login.
   Halaman login akan kita buat dengan file `login.html` yang ada di folder `main/templates` dengan isi:
   ```
   {% extends 'base.html' %}
   
   {% block meta %}
       <title>Login</title>
   {% endblock meta %}
   
   {% block content %}
   
   <div class = "login">
   
       <h1>Login</h1>
   
       <form method="POST" action="">
           {% csrf_token %}
           <table>
               <tr>
                   <td>Username: </td>
                   <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
               </tr>
                       
               <tr>
                   <td>Password: </td>
                   <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
               </tr>
   
               <tr>
                   <td></td>
                   <td><input class="btn login_btn" type="submit" value="Login"></td>
               </tr>
           </table>
       </form>
   
       {% if messages %}
           <ul>
               {% for message in messages %}
                   <li>{{ message }}</li>
               {% endfor %}
           </ul>
       {% endif %}     
           
       Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
   
   </div>
   
   {% endblock content %}
   ```
   Tambahkan path url milik halaman login ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `login` dari `views.py` dan tambahkan `path('login/', login_user, name='login')` pada variabel `urlpatterns`.

3. **Logout**
   
   Buka file `views.py` yang ada di folder `main` dan buat fungsi baru dengan nama `logout_user` yang menerima parameter `request`. Lalu impor `logout`. Isi dari fungsi `logout_user` adalah:
   ```
   def logout_user(request):
       logout(request)
       return redirect('main:login')
   ```
   `logout(request)` akan menghapus sesi pengguna yang saat ini sudah masuk. Lalu user akan kembali ke halaman login dengan `return redirect('main:login')`.
   Tambahkan:
   ```
   ...
   <a href="{% url 'main:logout' %}">
       <button>
           Logout
       </button>
   </a>
   ...
   ```
   Setelah hyperlink tag untuk Add New Product yang ada di file `main.html`.
   Tambahkan path url milik halaman logout ke file `urls.py` pada direktori `main` dengan mengimpor fungsi `logout_user` dari `views.py` dan tambahkan `path('logout/', logout_user, name='logout')` pada variabel `urlpatterns`.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

   Akun pertama:
   <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/e418e156-ee6b-4dc7-8b7d-0e141cc1c8e2">

   Akun kedua:
   <img width="1728" alt="image" src="https://github.com/topahilangharapan/warkop_kalisetail/assets/117751625/acece276-6f79-4d8f-bc27-b3b6f3b8c3c3">


- [x] Menghubungkan model Item dengan User.

   Buka `models.py` yang ada di direktori `main` lalu impor `User` dari `django.contrib.auth.models`. Pada model `Product` yang ada tambahkan kode:
   ```
   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
   ```
   Hal ini dilakukan supaya kita menghubungkan satu produk dengan satu user menggunakan relationship, jadi sebuah produk pasti terasosiasi dengan user.
   Buka `viwes.py` yang ada di direktori `main` dan modifikasi fungsi `create_product` menjadi:
   ```
   def create_product(request):
   form = ProductForm(request.POST or None)
   
   if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
   ...
   ```
   `commit=False` berfungsi supaya Django tidak langsung menyimpan objek yang dibuat dari form ke database sehingga kita dapat memodifikasi objek tersebut dahulu. Kita mengisi field `user` dengan objek `User` dari return nilai `request.user` yang sudah terautentikasi untuk menandakan bahwa objek tersebut milik pengguna yang sedang login.
   Ubah fungsi `show_main` menjadi:
   ```
   def show_main(request):
       products = Product.objects.filter(user=request.user)
   
       context = {
           'name': request.user.username,
       ...
   ...
   ```
   Hal ini dilakukan agar objek `Product` yang terasosiasi dengan user yang sedang login dapat ditampilkan. Kita menyaring seluruh objek dan hanya mengambil `Product` yang field `user` terisi dengan objek `User` yang sama dengan user yang sedang login. Untuk menampilkan username user yang login pada halaman main kita menggunakan `request.user.username`.
   Kita lakukan migrasi model dengan `python manage.py makemigration` dan muncul error, untuk mengatasinya pilih 1 supaya kita menetapkan default value untuk field user pada semua row yang dibuat pada di basis data, ketik angka 1 untuk menetapkan user dengan ID 1 (user yang baru kita buat tadi) pada model yang ada. Lakukan `python manage.py migrate` untuk mengaplikasikan migrasi.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

   Buka file `views.py` yang ada di direktori `main` dan impor `HttpResponseRedirect`, `reverse`, dan `datetime`. Kita tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` pada fungsi `login_user`, fungsi `last_login` digunakan untuk mengetahui kapan terakhir kali user login. Cara ini dilakukan dengan mengganti kode yang ada pada conditional `if user is not None` menjadi:
   ```
   ...
   if user is not None:
       login(request, user)
       response = HttpResponseRedirect(reverse("main:show_main")) 
       response.set_cookie('last_login', str(datetime.datetime.now()))
       return response
   ...
   ```
   `login(request, user)` berguna supaya logint terlebih dahulu. Untuk membuat response, kita menggunakan variabel `response` dan mengisinya dengan `HttpResponseRedirect(reverse("main:show_main"))`. `response.setcookie('last_login', str(datetime.datetime.now()))` berfungsi untuk membuat cookie `last_login` dan menambahkannya ke response tadi.
   Pada fungsi `show_main` tambahkan `'last_login': request.COOKIES['last_login']` pada variabel `context` supaya kita bisa menambahkan informasi cookie last_login pada response yang akan ditampilkan di web `main.html`.
   Untuk menghapus cookie `last_login` ketika user `logout` kita modifikasi code `logout_user` menjadi:
   ```
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```
   Lalu pada `main.html` tambahkan:
   ```
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```
   Untuk menampilkan data last login.
   
- [x] Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

   UserCreationForm adalah salah satu komponen yang disediakan oleh Django, sebuah framework develop web berbasis Python, yang digunakan untuk membuat formulir pendaftaran atau registrasi pengguna (user registration form). Form ini mempermudah developer untuk membuat halaman pendaftaran pengguna dalam aplikasi web Django dengan sangat cepat.

   **Kelebihan dari UserCreationForm:**
   
   1. Mudah Digunakan
     
      UserCreationForm telah terintegrasi dengan Django's authentication system, sehingga developer dapat dengan mudah membuat halaman pendaftaran pengguna tanpa harus menulis kode dari awal.
      
   2. Validasi Otomatis
     
      Form ini memiliki validasi otomatis untuk memastikan bahwa pengguna mengisi semua kolom yang diperlukan dengan benar, seperti alamat email yang valid dan kata sandi yang memenuhi kriteria keamanan.
      
   3. Customizable
      Meskipun form ini sudah siap pakai, developer masih bisa menyesuaikannya dengan kebutuhan aplikasi. Developer dapat menambahkan kolom tambahan atau mengubah validasi sesuai dengan kebutuhan.
   
   **Kekurangan dari UserCreationForm:**
   
  1. Tidak Fleksibel
     
      Form ini dirancang khusus untuk kebutuhan autentikasi pengguna Django, sehingga jika developer membutuhkan fitur pendaftaran pengguna yang berbeda, developer mungkin perlu menulis formulir khusus sendiri.
   
  2. Tidak Memungkinkan Pendaftaran Eksternal
     
     Jika developer ingin mengintegrasikan pendaftaran pengguna melalui penyedia eksternal (misalnya, login dengan Google atau Facebook), developer perlu menulis kode tambahan untuk mengimplementasikannya.
   
   3. Tidak Memungkinkan Pendaftaran secara Anonim
      
      UserCreationForm dirancang untuk pendaftaran pengguna yang terautentikasi. Jika developer membutuhkan pendaftaran secara anonim (misalnya, untuk pengguna yang belum memiliki akun), developer perlu membuat formulir tambahan atau memodifikasi form ini secara ekstensif.
      
- [x] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
      
  * **Autentikasi**
    
     * Autentikasi adalah proses untuk mengidentifikasi pengguna dan memverifikasi mereka. Ini umumnya terjadi saat pengguna mencoba masuk ke sistem dengan menyediakan informasi kredensial, seperti nama pengguna dan kata sandi.
     * Dalam Django, autentikasi umumnya diimplementasikan menggunakan sistem autentikasi bawaan Django, yang mencakup model pengguna (user model) dan berbagai alat untuk mengelola autentikasi, termasuk User model dan formulir autentikasi seperti UserCreationForm dan AuthenticationForm.
     * Autentikasi menghasilkan sesi atau token autentikasi yang digunakan untuk mengidentifikasi pengguna yang sudah masuk dalam sesi selanjutnya. Ini memungkinkan pengguna untuk mengakses bagian tertentu dari aplikasi yang diberikan izin akses.
       
   * **Otorisasi**

      * Otorisasi adalah proses untuk mengontrol apa yang diizinkan atau dilarang oleh pengguna yang sudah diotentikasi. Ini berarti menentukan apakah pengguna memiliki izin untuk melakukan tindakan tertentu dalam aplikasi, seperti membaca, menulis, atau menghapus data.
      * Dalam Django, otorisasi biasanya diimplementasikan menggunakan sistem otorisasi berdasarkan peran (role-based) dan izin (permission-based). Anda dapat menetapkan peran kepada pengguna (misalnya, pengguna biasa, admin, atau moderator) dan kemudian memberikan izin kepada peran tersebut untuk melakukan tindakan tertentu di dalam aplikasi.
      * Otorisasi memastikan bahwa pengguna hanya dapat mengakses data atau fitur yang sesuai dengan peran dan izin yang mereka miliki.
        
   * **Pentingnya autentikasi dan otorisasi**
     
      * Autentikasi penting untuk mengidentifikasi pengguna dengan aman dan memastikan bahwa hanya pengguna yang benar-benar berwenang yang dapat masuk ke sistem.
      * Otorisasi penting untuk mengendalikan akses pengguna ke berbagai bagian dan fungsionalitas aplikasi. Ini membantu melindungi data sensitif, mengatur hak akses, dan memastikan bahwa pengguna hanya dapat melakukan tindakan yang diizinkan.
      
- [x] Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
      
   Cookies dalam konteks aplikasi web adalah file kecil yang disimpan pada perangkat pengguna oleh server web saat pengguna mengunjungi situs web. Cookies digunakan untuk menyimpan data khusus dalam bentuk pasangan "nama-nilai" yang dapat diakses oleh server web saat pengguna kembali mengunjungi situs yang sama. Cookie ini dikirim dari server ke perangkat pengguna melalui respons HTTP dan kemudian dikirim kembali ke server oleh perangkat pengguna melalui permintaan HTTP saat kunjungan berikutnya. Cookies digunakan untuk berbagai tujuan dalam aplikasi web, termasuk menyimpan informasi sesi pengguna.
   Django menggunakan cookies untuk mengelola data sesi pengguna. Django memiliki sistem autentikasi yang mengintegrasikan pengguna dengan sesi, dan cookies digunakan untuk menyimpan identifikasi sesi tersebut. Berikut adalah cara Django menggunakan cookies untuk mengelola sesi pengguna:

   1. Autentikasi dan Sesi Pengguna
         Ketika seorang pengguna berhasil login ke aplikasi web Django, server akan membuat sesi pengguna untuk mereka. Informasi autentikasi pengguna, seperti ID pengguna atau nama pengguna akan disimpan dalam sesi ini.

   2. Penyimpanan Data Sesuai Cookie
         Django secara otomatis menyimpan ID sesi ini dalam bentuk cookie pada perangkat pengguna. Cookie ini biasanya disebut "sessionid" secara default.

   3. Kirim Cookie dalam Setiap Permintaan
         Setiap kali pengguna membuat permintaan HTTP ke aplikasi web Django, cookie "sessionid" akan dikirimkan kembali ke server sebagai bagian dari permintaan. Ini memungkinkan server Django untuk mengidentifikasi sesi pengguna yang sesuai.

   4. Akses Data Sesuai Cookie
         Dengan menggunakan nilai cookie "sessionid", Django dapat mengambil data sesi pengguna yang sesuai dari penyimpanan sesi (biasanya dalam database atau cache). Ini memungkinkan Django untuk menyimpan dan mengakses data sesi pengguna, seperti keranjang belanja, preferensi pengguna, atau informasi login.

   5. Keamanan
         Django secara otomatis menangani keamanan dari penggunaan cookie sesi. Ini termasuk mengamankan cookie melalui mekanisme seperti HTTP-only, Secure Flag (untuk HTTPS), dan signing (penandatanganan) yang menghindari perubahan yang tidak sah oleh pengguna.

- [x] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
      
   Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang harus diwaspadai, dan keamanannya sangat tergantung pada bagaimana cookies digunakan dan dikonfigurasi dalam aplikasi web Anda. Berikut adalah beberapa risiko potensial terkait dengan penggunaan cookies:

   1. Cookies Tampering
         Pengguna dapat mencoba memodifikasi nilai cookies yang tersimpan di perangkat mereka untuk mengakses atau memanipulasi data sesi atau informasi lain yang disimpan dalam cookies. Oleh karena itu, penting untuk mengamankan cookies dan menerapkan tanda tangan (signing) pada cookies.

   2. Cookie Sniffing
         Penyadap (sniffer) di jaringan dapat mencoba mencuri informasi cookies saat dikirimkan antara perangkat pengguna dan server. Untuk mengatasi ini, cookies harus dienkripsi jika berisi informasi sensitif.

   3. Cross-Site Scripting (XSS)
         Penyerangan XSS dapat memungkinkan penyerang menyuntikkan kode berbahaya ke dalam halaman web yang akan diakses oleh pengguna lain. Kode berbahaya ini dapat digunakan untuk mencuri cookies pengguna. Mencegah XSS adalah penting untuk melindungi cookies dan data sensitif lainnya.

   4. Cross-Site Request Forgery (CSRF)
         Penyerangan CSRF dapat memaksa pengguna yang sudah diautentikasi untuk melakukan tindakan tertentu tanpa izin mereka, seperti mengirim permintaan yang menggunakan cookies mereka. Menggunakan mekanisme anti-CSRF adalah penting untuk melindungi cookies dari penyerangan ini.

   5. Privasi Pengguna
         Cookies dapat digunakan untuk melacak aktivitas pengguna secara online, yang dapat menciptakan masalah privasi. Oleh karena itu, penting untuk memiliki kebijakan privasi yang jelas dan memberikan pengguna opsi untuk mengontrol cookies.
      
## Tugas 5

 - [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
       
     Pertama, kita mengimpor font "Plus Jakarta Sans" yang terlihat bagus dan cocok dari Google Fonts ke dalam halaman HTML dengan menyalin kode yang mereka berikan dan menempelkannya di bagian atas halaman.

      Kemudian, lanjutkan dengan membuat gaya khusus menggunakan CSS langsung di halaman HTML. Ini memungkinkan kita untuk mengubah warna, bentuk tombol, dan elemen lainnya sesuai dengan keinginan. Misalnya, mengganti font untuk seluruh halaman agar menggunakan "Plus Jakarta Sans", mengubah warna latar belakang, dan menambahkan padding serta margin agar tampilan lebih rapi.

      Selain itu, gunakan display flex dan display grid untuk mengatur tata letak elemen dengan lebih fleksibel dan efisien. Sekaligus kita menambahkan shadow dan radius pada elemen tertentu untuk memberikan sentuhan desain yang lebih menarik dan profesional.
      
 - [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

      Ubah tampilan daftar produk dalam inventori warkop Kalisetail. Sebelumnya, ditampilkan menggunakan tabel, namun saya ubah ke tampilan card yang lebih modern dan estetis.

      Untuk membuat tampilan card ini, saya menggunakan referensi kode card dari Bootstrap.Lalu modifikasi pada kode card tersebut agar sesuai dengan keinginan. Setelah card-card berhasil dibuat sesuai dengan keinginan, saya memasukkan card-card ini ke dalam sebuah container-card. Dengan cara ini, saya dapat mengelompokkan produk-produk tersebut dengan rapi dalam satu wadah.

      Terakhir, untuk menampilkan card-card ini dengan tampilan yang rapi dan dinamis, saya memanfaatkan fitur display grid dan justify evenly. Dengan menggunakan display grid, saya dapat mengatur tata letak card-card ini secara efisien dan memastikan tampilan yang terorganisir. Sementara itu, penggunaan justify evenly membantu agar card-card tersebut tersebar secara merata di dalam container, menciptakan tampilan yang teratur dan menarik. Dengan langkah-langkah ini, saya berhasil menciptakan tampilan yang lebih menarik dan efisien untuk daftar produk inventori warkop Kalisetail.
       
 - [x] Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

   1. Element Selectors
      
         Ini adalah selektor paling dasar dalam CSS, memilih elemen HTML berdasarkan nama elemennya. Contoh:
         ```
         p {
           color: blue;
         }
         ```
         Semua elemen p pada halaman akan memiliki warna teks biru.
      
   2. Class Selectors
      
         Class adalah atribut yang dapat ditambahkan ke elemen HTML. Elemen dapat dipilih dengan menggunakan selektor kelas. Contoh:
         ```
         .highlight {
           background-color: yellow;
         }
         ```
         Semua elemen dengan class="highlight" akan memiliki latar belakang berwarna kuning.
   
   3. ID Selectors
      
         ID adalah atribut yang unik pada elemen HTML. Elemen dapat dipilih berdasarkan ID dengan tanda pagar (#). Contoh:
         ```
         #header {
           font-size: 24px;
         }
         ```
         Elemen dengan id="header" akan memiliki ukuran font 24px.
         
   4. Pseudo-class Selectors

         Digunakan untuk menargetkan elemen dalam keadaan tertentu atau saat interaksi pengguna, seperti :hover, :active, dan :focus. Contoh:
         ```
         a:hover {
           text-decoration: underline;
         }
         ```
         Ini akan memberikan garis bawah saat kursor berada di atasnya.

   5. Pseudo-element Selectors
      
         Pseudo-element digunakan untuk menargetkan dan memodifikasi bagian-bagian spesifik dari elemen. Contoh:
         ```
         p::first-line {
           font-weight: bold;
         }
         ```
         Ini akan membuat baris pertama dalam setiap elemen p menjadi tebal.
      
 - [x] Jelaskan HTML5 Tag yang kamu ketahui.

   * !DOCTYPE: Digunakan untuk mendefinisikan jenis dokumen HTML yang digunakan.
   * html: Menandai awal dan akhir keseluruhan dokumen HTML.
   * head: Berisi informasi terkait dokumen HTML, seperti meta informasi dan tautan ke stylesheet.
   * title: Menentukan judul yang akan ditampilkan di bilah judul browser atau tab.
   * body: Menandai area utama dokumen yang berisi konten yang ditampilkan kepada pengguna.
   * h1 - h6: Digunakan untuk menandai tingkat kepentingan judul dengan ukuran yang berbeda.
   * p: Menandai paragraf dalam dokumen.
   * a: Membuat tautan ke halaman web lain atau alamat email.
   * img: Menampilkan gambar dalam dokumen HTML.
   * button: Digunakan untuk membuat tombol yang dapat di-klik oleh pengguna.
   * div: Menandai sebagian dokumen yang dapat digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML.

 - [x] Jelaskan perbedaan antara margin dan padding.

   * Margin:
     
      * Margin adalah ruang di luar elemen, yaitu ruang antara elemen tersebut dengan elemen-elemen lain di sekitarnya.
      * Margin digunakan untuk mengontrol jarak antara elemen dan elemen-elemen lainnya di dalam layout halaman.
      * Margin dapat digunakan untuk memberikan jarak vertikal atau horizontal antara elemen-elemen.
      * Margin dengan nilai negatif dapat digunakan untuk mengalap elemen-elemen.
        
   * Padding:
     
      * Padding adalah ruang di dalam elemen, yaitu ruang antara batas elemen dan kontennya sendiri.
      * Padding digunakan untuk mengontrol jarak antara konten elemen dan batas elemen tersebut.
      * Padding dapat digunakan untuk memberikan ruang di sekitar konten elemen.
      * Padding tidak mempengaruhi jarak antara elemen-elemen lain di luar elemen tersebut.
       
 - [x] Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

   * Tailwind CSS
     
      *  Menggunakan banyak kelas utilitas untuk membangun tampilan. Fleksibel, memerlukan kurva belajar lebih tinggi, dan menghasilkan file CSS yang lebih besar. Bagus jika menginginkan penyesuaian yang tinggi dan ingin mengendalikan setiap aspek tampilan.
        
   *  Bootstrap
     
      *  Menyediakan komponen dan gaya yang telah dirancang sebelumnya. Lebih mudah dipelajari dan menghasilkan file CSS yang lebih kecil. Cocok jika ingin membangun dengan cepat dan memerlukan banyak komponen siap pakai.

   Kapan Menggunakannya ?

   * Bootstrap: Ketika Anda butuh cepat, nyaman dengan kerangka kerja tradisional, dan membutuhkan banyak komponen.

   * Tailwind CSS: Ketika Anda ingin kontrol yang lebih besar, mengurangi ukuran file, dan suka pendekatan utility-first dalam CSS.
       
 - [x] Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.

   Pada bagian loop product di file `main.html` (`{% for product in products %}`). Untuk mengecek apakah ini adalah baris terakhir atau item terakhir pada inventori kita tambahkan kode:
   ```
   ...
      {% if forloop.last %}
         #item_terakhir

      {% else %}
         #item_selain_terakhir

      {% endif %}
   ...
   ```
   pada bagian #item_terakhir kita ubah style dari card, ubah warna dari background dan fontnya sehingga berbeda dari card sebelumnya.

## Tugas 6

- [x]  Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
      
   - [x] AJAX GET
         
      - [x] Ubahlah kode tabel data item agar dapat mendukung AJAX GET.

         Sebelumnya pada `main.html` saya menggunakan cards untuk menampilkan list product, ubah menjadi:
         ```
         <table class="product-table" id="product_table"></table>
         ```
      
      - [x] Lakukan pengambilan task menggunakan AJAX GET.

         Buat fungsi di `views.py`:
         ```
         def get_product_json(request):
          product_item = Product.objects.all()
          return HttpResponse(serializers.serialize('json', product_item))
         ```
         Buat routing di `urls.py`, impor `get_product_json` dan tambahkan:
         ```
         path('get-product/', get_product_json, name='get_product_json'),
         ```
         Tambahkan `<script>` di `main.html`:
         ```
          async function getProducts() {
              return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
          }
         ```
         
      - [x] AJAX POST
            
         - [x] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
        
            Buat modal:
            ```
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form id="form" onsubmit="return false;">
                                {% csrf_token %}
                                <div class="mb-3">
                                    <label for="name" class="col-form-label">Name:</label>
                                    <input type="text" class="form-control" id="name" name="name"></input>
                                </div>
                                <div class="mb-3">
                                    <label for="price" class="col-form-label">Amount:</label>
                                    <input type="number" class="form-control" id="amount" name="amount"></input>
                                </div>
                                <div class="mb-3">
                                    <label for="price" class="col-form-label">Price:</label>
                                    <input type="number" class="form-control" id="price" name="price"></input>
                                </div>
                                <div class="mb-3">
                                    <label for="description" class="col-form-label">Description:</label>
                                    <textarea class="form-control" id="description" name="description"></textarea>
                                </div>
                            </form>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                        </div>
                    </div>
                </div>
            </div>
            ```
            Buat tombol untuk membuka modal:
            ```
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Add Product by AJAX
            </button>
            ```

         - [x] Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
           
            Pada `views.py` impor `from django.views.decorators.csrf import csrf_exempt` dan buat fungsi:
            ```
            @csrf_exempt
            def add_product_ajax(request):
                if request.method == 'POST':
                    name = request.POST.get("name")
                    amount = request.POST.get("amount")
                    price = request.POST.get("price")
                    description = request.POST.get("description")
                    user = request.user
            
                    new_product = Product(name=name,amount=amount, price=price, description=description, user=user)
                    new_product.save()
            
                    return HttpResponse(b"CREATED", status=201)
                return HttpResponseNotFound()
            ```

         - [x] Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
           
            Pada `urls.py` impor `add_product_ajax` dan tambahkan path url:
            ```
            path('create-ajax/', add_product_ajax, name='add_product_ajax'),
            ```

         - [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
           
            Pada `main.html` buat fungsi di`<script>`:
            ```
            function addProduct() {
                 fetch("{% url 'main:add_product_ajax' %}", {
                     method: "POST",
                     body: new FormData(document.querySelector('#form'))
                 }).then(refreshProducts)
         
                 document.getElementById("form").reset()
                 return false
             }
         
             document.getElementById("button_add").onclick = addProduct
            ```

         - [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.
           
            Pada `main.html` buat fungsi di`<script>`:
            ```
            async function refreshProducts() {
                 document.getElementById("product_table").innerHTML = ""
                 const products = await getProducts()
                 let htmlString = `<tr>
                     <th>Name</th>
                     <th class="table-head-amount">Amount</th>
                     <th>Price</th>
                     <th>Description</th>
         
                 </tr>`
                 products.forEach((item) => {
                     htmlString += `\n<tr>
                     <td>${item.fields.name}</td>
                     <td class="table-field-amount">${item.fields.amount}</td>
                     <td>Rp ${item.fields.price}</td>
                     <td class="table-field-description">
                         <div class="table-field-description-value">
                             ${item.fields.description}
                         </div>
                         <div class="table-product-edit">
                              <a href="inc_product_amount/${item.pk}">
                                 <button>
                                     Add
                                 </button>
                             <a/>
         
                             <a href="dec_product_amount/${item.pk}">
                                 <button>
                                     Take One
                                 </button>
                             </a>
                             <button type="button" class="btn btn-primary" id="button_delete" onClick="deleteProduct(${item.pk})">
                                 Remove
                             </button>
                         </div>
                     </td>
         
                 </tr>`
                 })
         
                 document.getElementById("product_table").innerHTML = htmlString
             }
            ```
   - [x] Melakukan perintah `collectstatic`.
      
      Pada `settings.py` tambahkan:
      ```
      STATIC_URL = 'static/'

      STATIC_ROOT = os.path.join(BASE_DIR, 'static')
      ```
      Lalu jalankan `python3 manage.py collectstatic`

* Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

   * **Synchronous Programming**

      1. Sequential Execution: Dalam Synchronous Programming, tugas atau operasi dieksekusi secara berurutan, satu per satu. Program akan menunggu satu tugas selesai sebelum melanjutkan ke tugas berikutnya.
      2. Blocking: Jika ada tugas atau operasi memakan waktu, program akan terblokir (blocking). Artinya, program akan berhenti bekerja atau tidak responsif selama tugas tersebut sedang berjalan.
      3. Sederhana: Synchronous programming lebih mudah dipahami dan di-debug karena alur eksekusinya linear dan berurutan.
      4. Tidak Efisien: Dalam aplikasi yang harus menangani banyak operasi bersamaan, synchronous programming mungkin kurang efisien dalam pengelolaan sumber daya.
         
   * **Asynchronous Programming**
      1. Concurrent Execution: Dalam Asynchronous Programming, tugas atau operasi dapat dieksekusi secara bersamaan. Program tidak perlu menunggu tugas selesai sebelum melanjutkan ke tugas berikutnya.
      2. Non-blocking: Program tidak terblokir saat tugas atau operasi yang memakan waktu. Sebaliknya, program melanjutkan eksekusi dan mungkin kembali ke tugas tersebut ketika sudah selesai.
      3. Kompleks: Asynchronous programming bisa lebih kompleks karena Anda perlu mengelola alur eksekusi dan menangani callback atau promise untuk menangani tugas yang belum selesai.
      4. Efisien dalam Mengelola Sumber Daya: Pemrograman asinkron dapat lebih efisien dalam mengelola sumber daya karena program dapat melanjutkan bekerja pada tugas lain saat tugas yang memakan waktu sedang berjalan.

* Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
   Paradigma event-driven programming adalah cara berpikir dalam pemrograman yang berfokus pada penggunaan peristiwa (events) sebagai pemicu eksekusi kode. Dalam paradigma ini, program tidak dieksekusi secara berurutan dari atas ke bawah seperti dalam pemrograman berbasis prosedur yang tradisional. Sebaliknya, program menunggu peristiwa tertentu terjadi, dan ketika peristiwa tersebut terjadi, kode yang sesuai akan dijalankan.
   Contoh penerapannya dalam tugas ini ada ketika kita menggunakan button untuk menjalankan fungsi `addProduct()`, kita menggunakan onclick dari `button_add` sebagai event yang menjalankan `addProduct()`.

* Jelaskan penerapan asynchronous programming pada AJAX.

  1. XMLHttpRequest Object atau Fetch API: Objek XMLHttpRequest atau Fetch API digunakan untuk membuat permintaan HTTP asynchronous ke server.
  2. Callback Functions: Untuk menangani respons dari server,digunakan callback functions. Fungsi-fungsi ini dijalankan ketika respons dari server telah tiba. Contoh callback functions dalam AJAX adalah .success(), .error(), dan .done() yang digunakan untuk menangani berbagai kondisi seperti respons sukses, kesalahan, atau penyelesaian permintaan.
  3. Promise: Promise adalah objek yang mewakili nilai yang mungkin akan tersedia di masa depan (ketika tugas atau operasi sudah selesai). Dengan promise, Anda dapat menjalankan kode setelah permintaan selesai, baik berhasil maupun gagal.
  4. Non-blocking: Kode JavaScript tetap responsif dan tidak terblokir selama proses pengiriman permintaan ke server atau saat menunggu respons dari server. Ini memungkinkan aplikasi web untuk tetap berfungsi dengan baik tanpa terasa "menggantung" saat menunggu respons dari server.

* Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

  1. Fetch API:

      * Native JavaScript: Fetch API adalah bagian dari JavaScript yang disediakan secara native oleh browser modern.
      * Promise-Based: Fetch API menggunakan promise, yang membuatnya lebih mudah untuk menangani permintaan asinkron dan meresponsnya dengan jelas.
      * Lebih Ringan: Fetch API lebih ringan daripada jQuery karena fokus pada AJAX dan tidak memiliki fitur-fitur lain yang dimiliki oleh jQuery.
      * Terbaru: Fetch API merupakan teknologi terbaru yang diperbarui dan dikelola oleh W3C, sehingga Anda dapat mengharapkan perkembangan dan dukungan yang baik dari browser modern.

   2. jQuery:

      * Kompatibilitas: jQuery dirancang seragam dan mudah digunakan di semua browser, termasuk yang lebih lama. Ini memastikan kompatibilitas lintas browser yang baik.
      * Plugin: jQuery memiliki banyak plugin yang dapat digunakan untuk berbagai keperluan, termasuk animasi, manipulasi DOM, dan banyak lagi. Ini bisa menghemat waktu dalam pengembangan.
      * Sintaks Yang Mudah Dipahami: jQuery sering dianggap lebih mudah dipelajari dan dimengerti oleh pemula karena memiliki sintaks yang lebih sederhana daripada Fetch API.
     
   Saya berpendapat bahwa Fetch API lebih baik daripada jQuery karena Fetch API fokus pada AJAX dan tidak memiliki fitur tambahan yang dimiliki jQuery, sehingga lebih ringan dalam penggunaan memori dan kecepatan. ia juga merupakan bagian dari JavaScript yang tersedia secara native di browser modern. Digunakannya promise untuk menangani permintaan asinkron dengan cara yang lebih jelas dan mudah dipahami. Fetch API adalah Teknologi terbaru sehingga dapat diharapkan perkembangan dan dukungan yang baik dari browser modern. Menggunakan Fetch API, kita memiliki kontrol yang lebih besar terhadap permintaan dan respons HTTP, memungkinkan pengoptimalan yang lebih baik.

- [x] Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE

   Buat fungsi baru di `views.py`:
   ```
   @csrf_exempt
   def delete_product_ajax(request, id):
       product = Product.objects.get(pk=id)
       product.delete()
       response = HttpResponseRedirect(reverse("main:show_main"))
       return response
   ```
   Tambahkan routing untuk fungsi tersebut dengan mengimpor `delete_product_ajax` dan menambahkan path url baru di `urls.py`:
   ```
   path('delete_product_ajax/<int:id>', delete_product_ajax, name='delete_product_ajax')
   ```
   Buat button di `main.html` sebagai pembuat events:
   ```
   <button type="button" class="btn btn-primary" id="button_delete" onClick="deleteProduct(${item.pk})">
      Remove
   </button>
   ```
   Events yang dibuat oleh buttont tersebut akan memicu eksekusi kode fungsi `deleteProduct(id)` yang ada di `<script>` pada `main.html` sebagai berikut:
   ```
   function deleteProduct(pk) {
        var action = confirm("Are you sure you want to delete this product?");
        if (action) {
            fetch(`/delete_product_ajax/${pk}`, {
                method: 'DELETE',
            }).then(refreshProducts);
            alert("product has been deleted");
        }
   }
   ```
