nilai_algoritma = float(input("Masukkan nilai algoritma: "))
nilai_perancangan_objek= float(input("Masukkan nilai perancangan objek: "))
nilai_kalkulus = float(input("Masukkan nilai kalkulus: "))
nilai_etika_profesi = float(input("Masukkan nilai etika profesi: "))
nilai_database = float(input("Masukkan nilai databases: "))
nilai_english = float(input("Masukkan nilai english 1: "))

def skorToBobot(skor):
    if skor >= 90:
        return 4
    elif skor >= 84:
        return 3.75
    elif skor >= 80:
        return 3.5
    elif skor >= 75:
        return 3.25
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.5
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    else:
        return 0
    
total_SKS = 18
ipk = (nilai_algoritma + nilai_perancangan_objek + nilai_kalkulus + nilai_etika_profesi + nilai_database + nilai_english) / total_SKS

print(f"IPK Anda untuk Semester Ini adalah: {ipk}")