import atexit
import p_kalori


def exit_handler():
    print("Menyimpan Riwayat Kegiatan...")
    p_kalori.save_file()
    print("Penyimpanan File Berhasil")


def input_kegiatan(index=None):
    kegiatan = input("Masukkan Kegiatan : ")
    met = float(input("Masukkan MET : "))
    berat_badan = int(input("Masukkan Berat Badan : "))
    durasi = int(input("Masukkan Durasi (dalam Menit): "))
    kalori_terbakar = p_kalori.hitung_kalori(kegiatan, met, berat_badan, durasi,index)
    print(f"Kalori Terbakar = {kalori_terbakar}")

p_kalori.load_file("riwayat/riwayat.csv")
atexit.register(exit_handler)

print("Program Penghitung Kalori Terbakar")

while True:
    print("-------------------------------------")
    print("1. Masukkan Kegiatan")
    print("2. Lihat Kegiatan")
    print("3. Edit Kegiatan")
    print("4. Hapus Kegiatan")
    print("5. Exit")
    menu_input = input("Pilih Menu : ")
    print("-------------------------------------")
    if menu_input == "1":
        input_kegiatan()
    elif menu_input == "2":
        p_kalori.print_riwayat()
    elif menu_input == "3":
        p_kalori.print_riwayat()
        index_input = int(input("Masukkan Index Kegiatan : "))
        input_kegiatan(index=index_input)
    elif menu_input == "4":
        p_kalori.print_riwayat()
        index_input = int(input("Masukkan Index Kegiatan : "))
        p_kalori.delete_kegiatan(index_input)
    elif menu_input == "5":
        break
    else:
        print("Menu Invalid")