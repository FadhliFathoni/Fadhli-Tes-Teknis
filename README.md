# Fadhli-Tes-Teknis

A. Membuat Env python
    <ol>
        <li>Masuk CMD</li>
        <li>python venv Env</li>
    </ol>
    
    

B. Mengaktifkan Env
    1. Masuk ke folder env/scripts
    2. ketik activate

C. Membuat superuser
    1. Masuk ke cmd dalam folder project
    2. ketik python manage.py createsuperuser
    3. masukkan username dengan nama admin, email, dan password

D.1 Memulai server dengan python
    1. Masuk ke folder project.
    2. Masuk ke CMD.
    3. ketik python manage.py migrate
    4. ketik python manage.py runserver

D.2 Memulai server dengan docker
    1. Masuk ke folder project
    2. Masuk ke CMD
    3. ketik docker-compose up

E. Masukkan admin ke group Admin
    1. masuk ke website 127.0.0.1:8000/admin
    2. login menggunakan akun superuser yang telah dibuat
    3. masuk ke halaman user
    4. pilih admin dan masukkan admin ke grup Admin

    Website dapat dijalankan