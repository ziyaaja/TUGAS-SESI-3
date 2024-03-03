def konversi_nilai(nilai):
    if nilai < 50:
        return 'E'
    elif 50 <= nilai < 60:
        return 'D'
    elif 60 <= nilai < 70:
        return 'C'
    elif 70 <= nilai < 80:
        return 'B'
    else:
        return 'A'

nilai_mahasiswa = float(input("Masukkan nilai mahasiswa: "))
hasil_konversi = konversi_nilai(nilai_mahasiswa)
print("Hasil konversi nilai:", hasil_konversi)
