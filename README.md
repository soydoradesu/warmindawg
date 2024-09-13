# Warmindawg (A Warmindo with extra spice 🌶️)
Warmindawg is a very simple app made with django

**Link:** [http://valentino-kim-warmindawg.pbp.cs.ui.ac.id/](http://valentino-kim-warmindawg.pbp.cs.ui.ac.id/)

# Jawaban Soal Tugas 2

**Nama**: Valentino Kim Fernando <br />
**NPM**: 2306275771 <br />
**Kelas**: PBP F 

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