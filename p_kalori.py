import csv
import os

_riwayat = []
_lokasi_file = ""


def load_file(lokasi_csv):
    # Muat csv file
    global _lokasi_file
    _lokasi_file = lokasi_csv
    # Mengecek Apakah Filenya Ada
    if os.path.exists(_lokasi_file):
        # Load Dari File
        with open(_lokasi_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            counter = 0
            for line in csv_reader:
                if counter != 0:
                    _riwayat.append(line)
                counter += 1
    else:
        # Buat File Sama Header
        with open(_lokasi_file, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([
                "Nama Aktivitas",
                "MET",
                "Berat Badan",
                "Durasi",
                "Kalori Terbakar"
            ])


def print_riwayat():
    counter = 1
    for i in _riwayat:
        print(f"{counter}. \tAktivitas : {i[0]}\n"
              f"\tMET : {i[1]}\n"
              f"\tBerat Badan : {i[2]}\n"
              f"\tDurasi : {i[3]}\n"
              f"\tKalori Terbakar : {i[4]}\n")
        counter += 1


# Hitung Kalori Sekalian Update Kegiatan
def hitung_kalori(kegiatan, met, berat_badan, durasi, index=None):
    global _riwayat
    kalori_terbakar = met * berat_badan * (durasi / 60)
    # Kalau index nggak dipakai bakalan append list
    if index is None:
        _riwayat.append([kegiatan, met, berat_badan, durasi, kalori_terbakar])
    # Kalau index dipakai bakalan ubah list di index
    else:
        _riwayat[index-1] = [kegiatan, met, berat_badan, durasi, kalori_terbakar]
    return kalori_terbakar


# Hapus Kegiatan
def delete_kegiatan(index):
    _riwayat.pop(index-1)


# Simpan File CSV
def save_file():
    with open(_lokasi_file, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow([
            "Nama Aktivitas",
            "MET",
            "Berat Badan",
            "Durasi",
            "Kalori Terbakar"
        ])
        for i in _riwayat:
            csv_writer.writerow(i)
