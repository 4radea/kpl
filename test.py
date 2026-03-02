username_benar = "admin"
password_benar = "123"

# Input dari user
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Proses pengecekan
if username == username_benar and password == password_benar:
    print("Login berhasil!")
else:
    print("Username atau password salah!")