# BepeShop (an e-commerce django app)

Bepeshop is a very simple app created using django

**Link:** [http://pbp.cs.ui.ac.id/valentino.kim/ecommercepbp/](http://pbp.cs.ui.ac.id/valentino.kim/ecommercepbp/)

## Jawaban Pertanyaan

### Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Jawaban
1. Berikut merupakan bagian pengimplementasian web:
- Membuat sebuah proyek django baru dengan melakukan startproject
- Lalu dilanjut dengan membuat app main dengan startapp
- Melakukan routing dengan mengonfigurasi URL pada app main lalu tidak lupa, dilanjut dengan mengonfigurasi URL pada project
- Model dibuat pada models.py dengan attribute wajib yaitu name, price dan description dengan tipe masing-masing CharField, IntegerField, TextField
- Dilanjut dengan membuat file HTML yang berisi barang-barang yang akan ditunjukan pada app
- Selanjutnya app dideploy ke pws(pbp.cs.ui.ac.id)
- App bisa dipakai :D!

### Pertanyaan
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
### Jawaban
2. Bagan request-response dari client ke aplikasi Django:

   [lorem ipsum pokonya nanti tarok sini]

### Pertanyaan
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
### Jawaban
3. Git berfungsi untuk version control dalam pengembangan perangkat lunak. Git membantu melacak perubahan kode, berkolaborasi, dan memudahkan rollback jika ada kesalahan secara efisien.

### Pertanyaan
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
### Jawaban
4. Django menjadi framework awal yang dipelajari karena arsitekturnya yang terpadu, mudah digunakan (karena menggunakan python), mudah dibaca, serta memiliki struktur MVC (Model-View-Controller) yang membantu memahami alur pengembangan web secara fundamental.

### Pertanyaan
5. Mengapa model pada Django disebut sebagai ORM?
### Jawaban
5. Model Django disebut ORM karena memetakan objek Python ke dalam tabel di database tanpa harus menulis query SQL secara langsung.