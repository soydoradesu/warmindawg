# Warmindawg (A Warmindo with extra spice 🌶️)
Warmindawg is a very simple app made with django

**Link:** [http://valentino-kim-warmindawg.pbp.cs.ui.ac.id/](http://valentino-kim-warmindawg.pbp.cs.ui.ac.id/)

# Jawaban Tugas Individu (Update: Tugas Individu 5)

**Nama**: Valentino Kim Fernando <br />
**NPM**: 2306275771 <br />
**Kelas**: PBP F 

<details>
    <summary><h2>Tugas Individu 2</h2></summary>

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Berikut merupakan bagian pengimplementasian web:
- Buat directory terlebih dahulu, lalu install requirements pada `requirements.txt `Membuat sebuah proyek django baru dengan melakukan `django-admin startproject e_commerce_pbp .`
- Lalu dilanjut dengan membuat app main dengan `python manage.py startapp main`
- Melakukan routing dengan mengonfigurasi URL pada app main lalu tidak lupa, dilanjut dengan mengonfigurasi URL pada `urls.py`
- Model dibuat pada `models.py` dengan attribute wajib yaitu name, price dan description dengan tipe masing-masing CharField, IntegerField, TextField
- Setelah itu kita melakukan migrasi model supaya project mudah untuk dilacak dengan `python manage.py makemigrations` lalu dilanjut dengan `python manage.py migrate`. Dengan ini direktori migrasi sudah dibuat di database local
- Dilanjut dengan membuat template HTML yang berisi barang-barang yang akan ditunjukan pada app
- Tidak lupa kita membuat function pada `views.py` supaya bisa mengisi tampilan yang diinginkan
- Sebelum deploy, kita tambahkan URL deployment PWS pada `settings.py` di bagian `ALLOWED_HOSTS`
- Selanjutnya app dideploy ke PWS --> `(pbp.cs.ui.ac.id)` 
- App bisa dipakai :D!

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Bagan request-response dari client ke aplikasi Django:

   <img src="public/PBP_Tugas 2.png">

## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi untuk version control dalam pengembangan perangkat lunak. Di antaranya:
- Git memungkinkan pelacakan dan manajemen perubahan kode sumber secara efisien.
- Git memfasilitasi kerja sama antar pengembang dengan menggunakan cabang (branches) untuk memisahkan perubahan.
- Dengan adanya branching, git mendukung eksperimen dan pengembangan fitur baru tanpa mengganggu kode utama.
- Git Mnyediakan backup penuh dari semua history kode, memudahkan dilakukannya pemulihan data.

## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django menjadi framework awal yang dipelajari karena arsitekturnya yang terpadu, mudah digunakan (karena menggunakan python), mudah dibaca, serta memiliki struktur MVT (Model-View-Template) yang membantu memahami alur pengembangan web secara fundamental.

## 5. Mengapa model pada Django disebut sebagai ORM?
Model Django disebut ORM karena memetakan objek Python ke dalam tabel di database tanpa harus menulis query SQL secara langsung.
</details>

<details>
    <summary><h2>Tugas Individu 3</h2></summary>

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data merupakan elemen penting yang memungkinkan aplikasi untuk berfungsi. 
Alasan kita memerlukan data delivery adalah:
- Responsivitas: Platform modern memerlukan pengiriman data real-time atau near real-time untuk memastikan responsivitas yang cepat terhadap input pengguna atau perubahan kondisi.
- Keamanan: Proses data delivery yang terstruktur dan terkontrol memungkinkan pengelolaan data yang aman
- Integrasi: Data delivery memungkinkan integrasi dengan berbagai sumber data, Data delivery memungkinkan pertukaran data yang konsisten dan efisien di antara sistem yang berbeda.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya sendiri JSON lebih baik, hal ini disebabkan karena beberapa hal:
- Lebih Ringkas dan Mudah Dibaca: JSON memiliki struktur yang lebih sederhana dan lebih ringkas daripada XML, yang membuatnya lebih mudah dibaca, intuitif dan mudah dipahami, bahkan oleh orang yang belum terbiasa melihat layout coding.
- Lebih Cepat Diproses: JSON lebih efisien untuk diparsing oleh browser atau server, sehingga mempercepat pengiriman dan pemrosesan data.

## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dikirimkan melalui form memenuhi semua aturan dan persyaratan validasi yang telah ditentukan. Fungsi ini penting karena:
- Data Validation: `is_valid()` memastikan bahwa semua field form diisi dengan benar, sesuai dengan tipe data yang diharapkan (misalnya, angka, teks, email, dll.), dan mematuhi aturan validasi lainnya (misalnya, panjang minimum/maksimum).

- Keamanan: Dengan memvalidasi data, kita dapat mencegah input berbahaya atau tidak valid yang dapat menyebabkan serangan, seperti SQL Injection atau Cross Site Scripting (XSS).

- Feedback ke Pengguna: Jika data tidak valid, Django dapat mengembalikan pesan kesalahan yang relevan, sehingga memberikan umpan balik yang berguna bagi pengguna untuk memperbaiki input mereka.

## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` (Cross-Site Request Forgery token) diperlukan saat membuat form di Django untuk mencegah serangan CSRF. Serangan CSRF terjadi ketika seorang penyerang mengeksploitasi kredensial otentikasi pengguna tanpa sepengetahuan mereka dengan membuat mereka mengirim permintaan yang tidak sah ke situs web yang terotentikasi.

**Apa yang Dapat Terjadi Jika Tidak Ditambahkan?** Jika csrf_token tidak ditambahkan, penyerang dapat membuat HTTP request palsu atas nama pengguna yang telah terotentikasi, seperti mengirim formulir atau melakukan tindakan yang tidak diinginkan. Ini dapat mengakibatkan pencurian data atau pelanggaran hukum lainnya.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Berikut merupakan cara saya mengimplementasikan tugas-tugas pada Tugas Individu 3:
- Pertama buatlah `forms.py` pada direktori main, dan diisi sesuai dengan model yang sudah kita buat sebelumnya
- Setelah itu, masuk ke `views.py` dan import forms, HTTPResponse, redirect dan juga serializers 
- Buatlah fungsi untuk menambahkan object baru dengan POST
- Sekarang buatlah page baru untuk forms dengan menambahkan file HTML baru pada directory templates, dalam project saya `add_menu.html`
- Jangan lupa untuk memasukkan `{% csrf_token %}` dan button untuk submit form
- Kembali lagi ke `views.py` buatlah 4 fungsi untuk melihat data JSON dan XML. Pada project saya `menu_list_json`, `menu_list_xml`, `menu_details_json` dan `menu_details_xml`
- Setelah itu, masuk ke `urls.py` dan tambahkan route baru untuk menampilkan page forms, serta page untuk melihat database yang ditampilkan dalam JSON maupun XML
- Project sudah bisa dijalankan! :D

## Postman Documentation
`menu_list_json`:
<img src="public/apimenujson.png">
`menu_list_xml`:
<img src="public/apimenuxml.png">
`menu_details_json`:
<img src="public/apimenujsonpk.png">
`menu_details_xml`:
<img src="public/apimenuxmlpk.png">
</details>

<details>
    <summary><h2>Tugas Individu 4</h2></summary>

## 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
Method `HttpResponseRedirect()` hanya bisa menerima `url` sebagai argumen pertamanya. Sementara itu, `redirect()` akan mengembalikan `HttpResponseRedirect` yang dapat menerima argumen berupa `model`, `view`, atau `url`.

## 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
`Item` diberikan atribut ForeignKey ke `User`, yang menciptakan hubungan _Many-to-one_. `User` ini diambil dari package `django.contrib.auth.models`. Untuk melakukan _filtering_ pada object `Item`. Pada projek ini, ubah `models.py` menjadi berikut:
```py
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

## 3. Apa perbedaan antara _authentication_ dan _authorization_, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
*** Authenthication ***
_Authentication_ merupakan proses untuk memverifikasi identitas seorang _user_, 

*** Authorization ***
_Authorization_ adalah proses untuk memverifikasi hak akses yang dimiliki _user_.

*** Pengimplementasian pada Django ***
Proses _Authentication_ di Django dikelola menggunakan _model_ `User` serta method bawaan seperti `login`, `logout`, dan `authenticate`. Di sisi lain, _Authorization_ pada Django dilakukan dengan memanfaatkan _decorators_ seperti `login_required()`, yang berfungsi membatasi akses hanya untuk _user_ yang telah terautentikasi.

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari _cookies_ dan apakah semua _cookies_ aman digunakan?
Pertama, Ketika seorang pengguna berhasil login, Django menyimpan data _session_ di server, kemudian mengirimkan _cookie session_ ke browser pengguna. _Cookie_ ini berisi _ID session_ unik yang menghubungkan pengguna dengan _data session_ yang disimpan di server. Setiap kali pengguna mengirim _request_ baru ke server, _cookie_ ini dikembalikan ke server untuk memastikan bahwa pengguna tetap dikenali sampai mereka melakukan logout.

Visualisasi perjalanan _cookies_
<img src="public/kukiss.png">

*** Kegunaan lain _cookies_ ***
_Cookies_ digunakan untuk melacak preferensi dari _user_, mempersonalisasi konten—biasa digunakan pada _e-commerce_—, menampilkan iklan yang biasa kalian lihat pada website-website di internet.

*** Cookies digunakan untuk hal jahat ***
Tidak semua _cookies_ aman untuk digunakan. _Cookies_ yang tidak dilindungi enkripsi bisa rentan dicuri atau diakses oleh pihak ketiga, misalnya melalui serangan _XSS (Cross Site Scripting)_. Serangan _XSS_ dapat mengambil _cookie_-mu, hal ini berbahaya karena cookies bisa memberikan akses langsung ke situs web tanpa memerlukan proses login. Akibatnya, data-data penting dan juga informasi pribadimu dapat diakses oleh orang yang berhasil mendapatkan _cookie_.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
1. Pertama, membuat fungsi registrasi, login, logout 

*** Registrasi ***
- Pada `views.py`, import `UserCreationForm` dan `messages`. `UserCreationForm` memudahkan kita dalam membuat forms untuk pendaftaran pengguna.
- Tambahkan fungsi `register` pada `views.py`
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('home:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- Buatlah template `register.html` pada directory `main/templates` untuk menampilkan form
- Terakhir tambahkan path register pada `urls.py`
```py
urlpatterns = [
   ...
   path('register/', register, name='register'),]
```

*** Login ***
- Pada `views.py`, import `authenthicate`, `login` dan `AuthenticationForm`.
- Tambahkan fungsi `login_user` pada `views.py`
```py
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("home:show_home"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
- Buatlah template `login.html` pada directory `main/templates` untuk menampilkan form
- Terakhir tambahkan path register pada `urls.py`
```py
urlpatterns = [
   ...
   path('login/', login_user, name='login'),]
```

*** Logout ***
- Pada `views.py`, import `logout`
- Tambahkan fungsi `logout_user` pada `views.py`
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('home:login'))
    response.delete_cookie('last_login')
    return response
```
- Buatlah template `logout.html` pada directory `main/templates` untuk menampilkan form
- Terakhir tambahkan path register pada `urls.py`
```py
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),]
```

2. Jangan lupa untuk me-restrict user untuk masuk ke home sebelum login, hal ini bisa dilakukan dengan:
- Buka `views.py` dan import `login_required`.
- Tambahkan decorator `@login_required(login_url='/login')` tepat di atas fungsi `show_home`.
```py
@login_required(login_url='/login')
def show_home(request):
```

3. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Saya melakukan hal ini dengan meregister dengan langsung project saya di localhost dengan melakukan `py manage.py runserver`, lalu langsungkan fitur tambahkan akun. Saya membuat 2 akun, test & test2, lalu melancarkan fitur add menu dengan jumlah 3 menu ditambahkan. Berikut visualisasi tampilan kedua akun setelah menambahkan 3 menu untuk masing-masing akun:

layar user test
<img src="public/test.png">

layar user test2
<img src="public/test2.png">

contoh closeup look test2
<img src="public/closeuptest2.png">

4. Menghubungkan Model dengan User
- Pada `models.py`, masukkan `from djang.contrib.auth.models import User`
- Pada `models.py`, tambahkan kode untuk `user`
```py
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```
- Lakukan migration dengan melancarkan `py manage.py makemigrations` lalu dilanjut `py manage.py migrate`.
- Buka `views.py`, kemudian ubah fungsi `add_menu_item` menjadi:
```py
def add_menu_item(request):
    form = MenuForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('/')
    
    return render(request, 'add_menu.html', {'form': form})
```

5. Menampilkan detail informasi pengguna yang sedang _logged in_ seperti _username_ dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- Pada `views.py`, tambahkan import `import datetime`, `from django.http import HttpResponseRedirect`, dan `from django.urls import reverse`
- Pada fungsi `login_user`, ubah bagian `form.is_valid()`-mu menjadi seperti ini sehingga kamu bisa melihat kapan terakhir kali melakukan login
```py
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("home:show_home"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
- Pada fungsi `logout_user`, ubah kodemu menjadi seperti ini
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('home:login'))
    response.delete_cookie('last_login')
    return response
```
- Pada fungsi `show_main`, tambahkan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`
- Tambahkan `last_login` ke dalam `home.html`
- Untuk melihat `username` sekaligus `last_login` pada home, buka `home.html` lalu tambahkan kode berikut:
```py
<h5>Username: {{ user.username }}</h5>
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
Secara otomatis, Django akan mengambil username dari active user dan juga variabel last_login dari context pada fungsi `show_home`

- Website bisa dipakai :D
</details>

<details>
    <summary><h2>Tugas Individu 5</h2></summary>

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Ketika beberapa pengaturan CSS diterapkan pada elemen HTML yang sama, CSS akan menentukan pengaturan mana yang akan diutamakan menggunakan sistem keutamaan atau specificity. Berikut adalah urutan keutamaan tersebut:

1. *** Gaya Inline *** (contoh: `style="color: red;"`) dianggap memiliki tingkat prioritas yang paling tinggi.
2. *** Selector ID *** (contoh: `#header`) memiliki tingkat prioritas yang lebih tinggi dibandingkan class atau elemen.
3. *** Selector Class *** (contoh: `.menu`) memiliki tingkat prioritas yang lebih tinggi daripada selector tag HTML.
4. *** Selector Tag *** (contoh: `h1`, `p`) memiliki tingkat prioritas yang paling rendah.
5. *** Aturan Important *** (`!important`) dapat mengabaikan semua tingkatan prioritas di atas dan memberikan prioritas tertinggi pada properti tertentu.

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Dengan meningkatnya penggunaan perangkat mobile seperti smartphone dan tablet, situs web perlu dapat diakses dan berfungsi dengan baik di berbagai ukuran layar dan resolusi. Responsive design akan menciptakan inklusivitas perangkat, sehingga seluruh perangkat dapat menggunakan app dengan maksimal.

*** Responsive ***
1. WhatsApp
2. Discord
3. Instagram

*** Tidak responsive ***
1. Web tua yang outdated
2. https://dequeuniversity.com/library/responsive/1-non-responsive

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

**Margin** adalah ruang yang memisahkan elemen dari elemen lain di sekitarnya. Margin berada di luar batas border. Margin tidak memiliki warna dan sering digunakan untuk menciptakan ruang ekstra antara elemen.

``` css
div {
  margin: 20px; /* Memberikan margin seragam di semua sisi */
  margin-top: 10px; /* Memberikan margin khusus pada sisi atas */
}
```

**Border** adalah garis yang mengelilingi elemen, berada di antara margin dan padding. Border bisa diatur ketebalan, gaya, dan warnanya. Border bisa digunakan untuk memberi definisi visual pada elemen.

```css
div {
  border: 2px solid black; /* Membuat border solid dengan ketebalan 2px dan warna hitam */
  border-width: 5px; /* Mengatur ketebalan border */
  border-style: dashed; /* Membuat border bergaris putus-putus */
  border-color: red; /* Memberikan warna merah pada border */
}
```

**Padding** adalah ruang antara isi dari sebuah elemen dengan batas (border) elemen tersebut. Padding digunakan untuk memberi ruang bernapas di dalam elemen, mempengaruhi ukuran visual elemen tersebut tetapi tidak mengubah dimensi elemen seperti yang ditampilkan oleh browser.

```css
div {
  padding: 15px; /* Memberikan padding seragam di semua sisi */
  padding-left: 5px; /* Memberikan padding khusus pada sisi kiri */
}
```

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid Layout adalah dua sistem tata letak CSS yang memudahkan pengaturan elemen dalam halaman web. Berikut merupakan penjelasan dari masing-masing Flexbox dan Grid Layout:

**Flexbox** (Flexible Box) dirancang untuk mengelola tata letak satu dimensi, baik dalam baris maupun kolom, memudahkan penyusunan, penyelarasan, dan distribusi ruang antar item secara fleksibel. Flexbox sangat berguna untuk navigasi, menu, atau elemen yang membutuhkan penyesuaian responsif dalam satu arah. **Grid Layout**, di sisi lain, memungkinkan pembuatan tata letak dua dimensi dengan mengatur baris dan kolom secara simultan, cocok untuk desain kompleks seperti layout halaman utama, galeri foto, atau dashboard aplikasi. Dengan memanfaatkan kedua konsep ini, kita dapat menciptakan desain yang responsif, terstruktur, dan mudah disesuaikan sesuai kebutuhan berbagai perangkat.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Implementasikan fungsi untuk menghapus dan mengedit product.
- Buatlah fungsi `edit_product_entry` pada `views.py`
    ```py
    def edit_menu(request, pk):
    menu = Item.objects.get(pk=pk)

    form = MenuForm(request.POST or None, instance=menu)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('home:show_home'))

    context = {'form': form}
    return render(request, "edit_menu.html", context)
    ```
- Kemudian, tambahkan fungsi ini pada `urls.py` main
    ```py
    ...
    path('edit-menu/<int:pk>', edit_menu, name='edit_menu'),
    ...
    ```
- Buatlah fungsi `delete_item` pada `views.py`
    ```py
    def delete_item(request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return HttpResponseRedirect(reverse('home:show_home'))
    ```
- Kemudian, tambahkan fungsi ini pada `urls.py` main
    ```py
    ...
        path('delete/<int:pk>/', delete_item, name='delete_item'),
    ...
    ```

2. Menambahkan tailwind ke project
- Ubah `base.html`-mu menjadi seperti ini
    ``` html
    ...
    <head>
        {% block meta %} 
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% endblock meta %}
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{% static '/css/global.css' %}"/>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body>
        {% block content %} {% endblock content %}
    </body>
    ...
    ```

3. Atur `settings.py` sedemikian rupa
- pada `MIDDLEWARE`, ubah menjadi seperti ini
    ```py
    MIDDLEWARE = [
                'django.middleware.security.SecurityMiddleware',
                'whitenoise.middleware.WhiteNoiseMiddleware',
                ...
                ]
    ```
- ubah juga `STATIC_URL`mu menjadi
    ```py
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static'
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static'
    ```

4. Buat direktori `static/css/global.css` untuk file styling sesuai dengan yang diinginkan

5. Buat template baru untuk edit item bernama `edit_menu.html` dengan isi
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Ubah Menu</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center" style="background-image: url('/static/bg.svg'); background-size: 1600px;">
  <div class="p-8 bg-white rounded-lg shadow-lg max-w-sm w-full form-style my-20">
    <img src="{% static 'Warmindawg_logo.png' %}" alt="Warmindawg Logo">
    <h1 class="text-xl font-bold mb-4 mt-4 text-center">
      <span class="text-2xl font-extrabold text-red-500">Edit Menu</span>
    </h1>
    <form method="POST" action="" class="flex flex-col gap-5">
      {% csrf_token %}
      <div class="grid grid-cols-2 gap-4">
        {% for field in form %}
        <div class="flex flex-col gap-2 {% if field.name == 'description' %}col-span-2{% endif %}">
          <label for="{{ field.id_for_label }}" class="font-bold">
            {{ field.label }}
          </label>
          <div>{{ field }}</div>
          {% if field.errors %}
          <ul class="list-disc bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 mt-2">
            {% for error in field.errors %}
            <li>{{ error }}</li>
            {% endfor %}
          </ul>
          {% endif %}
          {% if field.help_text %}
          <p class="text-xs text-gray-600">{{ field.help_text }}</p>
          {% endif %}
        </div>
        {% endfor %}
      </div>
      <div class="add-menu text-center pt-5">
        <button type="submit" class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600 focus:outline-none focus:shadow-outline">
          <strong>Simpan Menu</strong>
        </button>
      </div>
    </form>
  </div>
</div>
{% endblock content %}
```
7. Style page" lain supaya lebih estetik

8. Buatlah navbar dengan pertama membuat `navbar.html` pada templates di root. lalu diisi dengan:
```html
<nav class="relative flex flex-col">
    <div class="h-24 flex justify-between items-center px-100 px-12" style="background-color:#E82E31;">
        <img src="../static/Warmindawg_blue.svg">

        <!-- Hamburger Menu Button for Mobile -->
        <div class="md:hidden">
            <button id="menu-toggle" class="text-white focus:outline-none">
                <!-- Icon for the Hamburger Menu -->
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
            </button>
        </div>

        <!-- Menu Links (Shown on Medium Screens and Above) -->
        <div class="hidden md:flex space-x-12">
            <a href="#" class="text-white text-xl font-bold hover:text-gray-300 hover:underline transition duration-300">Home</a>
            <a href="#" class="text-white text-xl font-bold hover:text-gray-300 hover:underline transition duration-300">Menus</a>
            <a href="#" class="text-white text-xl font-bold hover:text-gray-300 hover:underline transition duration-300">Profile</a>
        </div>
    </div>

    <!-- Dropdown Menu for Mobile (Absolute) -->
    <div id="menu" class="hidden absolute top-32 right-12 rounded-lg w-40 bg-red-600 md:hidden flex flex-col space-y-2 py-4 px-4 border-4 border-red-800">
        <a href="#" class="text-white text-xl font-bold hover:text-gray-300 transition duration-300">Home</a>
        <a href="#" class="text-white text-xl font-bold hover:text-gray-300 transition duration-300">Menus</a>
        <a href="#" class="text-white text-xl font-bold hover:text-gray-300 transition duration-300">Profile</a>
    </div>

    <img src="../static/Warmindawg_bwh.svg" class="-translate-y-2">
</nav>

<script>
    // JavaScript to toggle the visibility of the menu on smaller screens
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.getElementById('menu');

    menuToggle.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });
</script>
```
Lalu menggunakan {% include navbar.html %} pada template yang ingin dipakaikan navbar

Page dapat digunakan!
</details>

<details open>
    <summary><h2>Tugas Individu 5</h2></summary>

## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- Membuat web menjadi interaktif: JavaScript memungkinkan developer untuk membuat halaman web yang interaktif. Contoh simpelnya adalah aksi klik tombol, pengiriman form, animasi, dan respon terhadap event keyboard atau mouse bisa dihandle secara dinamis tanpa perlu memuat ulang halaman.
- Menyambung dari yang sebelumnya, JavaScript dapat menjalankan proses secara asinkronus menggunakan AJAX, memungkinkan aplikasi web untuk memuat data di background. Hal ini mengurangi waktu tunggu dan mempercepat respons aplikasi.
- Peningkatan UX: Dengan JavaScript, pengembang dapat merancang UI yang responsif dan dinamis yang meningkatkan UX secara keseluruhan.
- Ekosistem yang Luas: JavaScript memiliki ekosistem yang besar termasuk library, frameworks, dan tools yang mendukung berbagai jenis pengembangan aplikasi.

## 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?
- `await` digunakan dalam function `async` untuk menunda eksekusi fungsi sampai `Promise` yang di-return oleh `fetch()` diselesaikan, artinya kode setelah `await` tidak akan dieksekusi sampai data yang di-fetch diterima.
- Jika kita tidak menggunakan  `await` dengan `fetch()`, kode berikutnya akan terus berjalan tanpa menunggu `fetch()` selesai. Ini berarti bahwa operasi yang bergantung pada data yang di-fetch mungkin akan gagal atau mengakses data yang belum siap/tersedia, mengakibatkan bug atau perilaku-perilaku tidak terduga lainnya dalam aplikasi.

## 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX `POST`?
- `csrf_exempt`: Decorator ini digunakan untuk menandai view tertentu agar terkecualian dari pemeriksaan CSRF, yang berguna untuk endpoint API yang mungkin dipanggil oleh klien yang tidak menyediakan CSRF token secara default, seperti pada beberapa implementasi AJAX atau ketika API dipanggil dari luar domain. Django secara default menggunakan CSRF token untuk mencegah serangan Cross-Site Request Forgery, di mana token ini harus disertakan dalam setiap permintaan POST untuk verifikasi.

## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
- Validasi atau pembersihan data di frontend bisa di-bypass atau dimodifikasi oleh pengguna, sehingga melakukan validasi lagi di backend menambah lapisan keamanan tambahan.
- Pencegahan Serangan: Melakukan pembersihan dan validasi di backend membantu mencegah serangan seperti SQL Injection, Cross-Site Scripting (XSS), dan serangan injeksi lain yang bisa mengeksploitasi input pengguna yang tidak aman.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. AJAX `GET`:
- Menambahkan import pada `views.py`
    ```python
    from django.views.decorators.csrf import csrf_exempt
    from django.views.decorators.http import require_POST
    ```

- Menambahkan fungsi baru pada `views,py` bernama  `add_menu_item_ajax`
    ```python
    @csrf_exempt
    @require_POST
    def add_menu_item_ajax(request):
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.POST.get("image")
        user = request.user
        username = user

        new_food = Item(name=name, price=price,
                        description=description, image=image, 
                        user=user, username=username)
        new_food.save()

        return HttpResponse(b"CREATED", status=201)
    ```
- Jangan lupa untuk menambah route ke `urls.py` sebelum menambah route juga jangan lupa untuk meng-import fungsi yang ingin ditambahkan rutenya pada `urls.py`
    ```python
    urlpatterns = [
        ...
        path('add-menu-ajax/', add_menu_item_ajax, name='add_menu_item_ajax'),   
        ]
    ```
- Untuk menghubungkan `add_menu_item_ajax`, kita membuat fungsi di dalam tag JavaScript pada `home.html`
```javascript
    function addItemEntry() {
        fetch("{% url 'home:add_menu_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#itemEntryForm')),
        })
        .then(response => refreshItemEntries())

        document.getElementById("itemEntryForm").reset(); 
        document.querySelector("[data-modal-toggle='crudModal']").click();

        return false;
    }
    
    document.getElementById("itemEntryForm").addEventListener("submit", (e) => {
            e.preventDefault();
            addItemEntry();
        })
```
- Input dari `add_menu_item_ajax` dilakukan dengan modul, berikut merupakan kode html dan juga logic untuk `showModal` dan `closeModal`
```html
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
          <!-- Modal header -->
          <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
              Add New Mood Entry
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
              <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <div class="px-6 py-4 space-y-6 form-style">
            <form id="itemEntryForm">
                <div class="mb-4">
                    <label for="name" class="block text-sm font-medium text-gray-700">Nama</label>
                    <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-red-700" placeholder="Masukkan nama produk" required>
                  </div>
                
                  <!-- Price Field -->
                  <div class="mb-4">
                    <label for="price" class="block text-sm font-medium text-gray-700">Harga (Rp[HARGAMU].000)</label>
                    <input type="number" id="price" name="price" min="1" max="100000" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-red-700" placeholder="Masukkan harga produk" required>
                  </div>
                
                  <!-- Description Field -->
                  <div class="mb-4">
                    <label for="description" class="block text-sm font-medium text-gray-700">Deskripsi</label>
                    <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-red-700" placeholder="Masukkan deskripsi produk" required></textarea>
                  </div>
                
                  <!-- Image Field -->
                  <div class="mb-4">
                    <label for="image" class="block text-sm font-medium text-gray-700">Image (URL)</label>
                    <input type="text" id="image" name="image" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-red-700" placeholder="Masukkan URL gambar" required>
                  </div>
            </form>
          </div>
          <!-- Modal footer -->
          <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitItemEntry" form="itemEntryForm" class="bg-red-700 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
          </div>
        </div>
      </div>
```
```javascript
        const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
            modalContent.classList.remove('opacity-0', 'scale-95');
            modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
            modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);
```
- Selanjutnya tambahkan fungsi `refreshItemEntries` dan juga `getItemEntries` sehingga update dari modul bisa ditampilkan secara asinkronus
```javascript
    async function getItemEntries(){
        return fetch("{% url 'home:menu_list_json' %}").then((res) => res.json())
    }

    async function refreshItemEntries(){
        document.getElementById("item_entry_cards").innerHTML = "";
        document.getElementById("item_entry_cards").className = "";
        const itemEntries = await getItemEntries();
        let htmlString = "";
        let classNameString = "";

        if (itemEntries.length === 0 ) {
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
                <h3 class="text-center pt-4">
                    <strong>Kamu belum memasukkan menu!</strong>
                </h3>
            `;
        }
        else {
            classNameString = "flex flex-wrap justify-center list-none";
            itemEntries.forEach((item) => {
                htmlString += `
                <li>
                    <img src="${item.fields.image}" alt="${item.fields.name}" class="fixed-image">
                    <p class="pt-4">
                        <strong>${item.fields.name}</strong>
                    </p>
                    <p class="text-red-500 font-bold">
                        Rp${item.fields.price}.000
                    </p>
                    <p class="product-description pt-4">
                        ${item.fields.description}
                    </p>
                    <p class="product-description pt-4">
                        <strong>Added by:</strong> ${item.fields.username}
                    </p>
                    <div style="justify-content: center; text-align: center; display: flex; gap: 12px; margin-bottom: 20px" class="pt-4">
                        <a href="/edit-menu/${item.pk}">
                            <button class="w-full px-10 py-2 text-white bg-orange-500 hover:bg-orange-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-600 focus:ring-opacity-50">
                                <strong>Ubah</strong>
                            </button>
                        </a>
                        <a href="/delete/${item.pk}">
                            <button class="w-full px-10 py-2 text-white bg-red-500 hover:bg-red-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50">
                                <strong>Hapus</strong>
                            </button>
                        </a>
                    </div>
                </li>
            `;
        })}
        document.getElementById("item_entry_cards").className = classNameString;
        document.getElementById("item_entry_cards").innerHTML = htmlString;
    }
    refreshItemEntries();
```
- Web dapat digunakan :D
</details>