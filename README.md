# Fadhli-Tes-Teknis
A. Membuat Env python
    1. Masuk CMD
    2. python venv Env
B. Mengaktifkan Env
    1. Masuk ke folder env/scripts
    2. ketik activate
C. Memubat superuser
    1. Masuk ke cmd dalam folder project
    2. ketik python manage.py createsuperuser
    3. masukkan username dengan nama admin, email, dan password
D. Memulai server
    1. Masuk ke folder project
    2. ketik python manage.py migrate
    3. ketik python manage.py runserver
E. Masukkan admin ke group Admin
    1. masuk ke website 127.0.0.1:8000/admin
    2. login menggunakan akun superuser yang telah dibuat
    3. masuk ke halaman user
    4. pilih admin dan masukkan admin ke grup Admin

    Website dapat dijalankan