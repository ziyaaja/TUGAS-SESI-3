def hitung_rata_rata(nilai_mtk, nilai_inggris, nilai_indonesia):
    return (nilai_mtk + nilai_inggris + nilai_indonesia) / 3

def pendaftaran_universitas():
    nama = input("Masukkan Nama: ")
    tempat_lahir = input("Masukkan Tempat Lahir: ")
    tanggal_lahir = int(input("Masukkan Tanggal Lahir: "))
    bulan_lahir = int(input("Masukkan Bulan Lahir: "))
    tahun_lahir = int(input("Masukkan Tahun Lahir: "))
    jenis_kelamin = input("Masukkan Jenis Kelamin (Laki-laki/Perempuan): ")
    nilai_mtk = float(input("Masukkan Nilai Matematika: "))
    nilai_inggris = float(input("Masukkan Nilai Bahasa Inggris: "))
    nilai_indonesia = float(input("Masukkan Nilai Bahasa Indonesia: "))
    
    rata_rata_nilai = hitung_rata_rata(nilai_mtk, nilai_inggris, nilai_indonesia)
    umur = 2024 - tahun_lahir
    
    if rata_rata_nilai >= 80:
        if jenis_kelamin.lower() == "laki-laki":
            jurusan = "Teknik Informatika"
        elif jenis_kelamin.lower() == "perempuan":
            jurusan = "Sistem Informasi"
        else:
            jurusan = "DKV"
    else:
        jurusan = "DKV"
    
    if umur <= 25:
        print("Selamat! Anda diterima di jurusan", jurusan)
    else:
        print("Maaf, Anda tidak memenuhi syarat umur.")

pendaftaran_universitas()