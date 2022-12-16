# Fadhli-Tes-Teknis

<h1>A. Membuat Env python</h1>
    <ol>
        <li>Masuk CMD</li>
        <li>python venv Env</li>
    </ol>

B. Mengaktifkan Env
    <ol>
        <li>Masuk ke folder env/scripts</li>
        <li>ketik activate</li>
    </ol>

C. Membuat superuser
    <ol>
        <li>Masuk ke cmd dalam folder project</li>
        <li>ketik python manage.py createsuperuser</li>
        <li>masukkan username dengan nama admin, email, dan password</li>
    </ol>
D.1 Memulai server dengan python
    <ol>
        <li>Masuk ke folder project</li>
        <li>Masuk ke CMD</li>
        <li>ketik python manage.py migrate</li>
        <li>ketik python manage.py runserver</li>
    </ol>
D.2 Memulai server dengan docker
    <ol>
        <li>Masuk ke folder project</li>
        <li>Masuk ke CMD</li>
        <li>ketik docker-compose up</li>
    </ol>
E. Masukkan admin ke group Admin
    <ol>
        <li>masuk ke website 127.0.0.1:8000/admin</li>
        <li>login menggunakan akun superuser yang telah dibuat</li>
        <li>masuk ke halaman user</li>
        <li>pilih admin dan masukkan admin ke grup Admin</li>
    </ol>
# Website dapat dijalankan