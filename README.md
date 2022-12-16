# Fadhli-Tes-Teknis

<h3>A. Membuat Env python</h3>
    <ol>
        <li>Masuk CMD</li>
        <li>python venv Env</li>
    </ol>

<h3>B. Mengaktifkan Env</h3>
    <ol>
        <li>Masuk ke folder env/scripts</li>
        <li>ketik activate</li>
    </ol>

<h3>C. Membuat superuser</h3>
    <ol>
        <li>Masuk ke cmd dalam folder project</li>
        <li>ketik python manage.py createsuperuser</li>
        <li>masukkan username dengan nama admin, email, dan password</li>
    </ol>
<h3>D.1 Memulai server dengan python</h3>
    <ol>
        <li>Masuk ke folder project</li>
        <li>Masuk ke CMD</li>
        <li>ketik python manage.py migrate</li>
        <li>ketik python manage.py runserver</li>
    </ol>
<h3>D.2 Memulai server dengan docker</h3>
    <ol>
        <li>Pastikan anda telah menginstal docker desktop</li>
        <li>Masuk ke folder project</li>
        <li>Masuk ke CMD</li>
        <li>ketik docker-compose build</li>
        <li>ketik docker-compose up</li>
    </ol>
<h3>E. Masukkan admin ke group Admin</h3>
    <ol>
        <li>masuk ke website 127.0.0.1:8000/admin</li>
        <li>login menggunakan akun superuser yang telah dibuat</li>
        <li>masuk ke halaman user</li>
        <li>pilih admin dan masukkan admin ke grup Admin</li>
    </ol>

<h3>F. Membuat akun karyawan</h3>
    <ol>
        <li>Masuk ke website 127.0.0.1:8000</li>
        <li>Login sebagai admin</li>
        <li>Masuk ke halam create dan buat karyawan</li>
    </ol>