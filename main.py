"""
Aplikasi deteksi gempa
"""


def ekstraksi_data():
    """
    Tanggal : 4 April 2022
    Waktu : 00:45:31 WIB
    Magnitudo : 2.9
    Kedalaman : 10 km
    Lokasi : 3.35 LS - 128.38 BT
    Pusat Gempa : Pusat gempa berada di darat 3 km timur Kairatu,Seram Bagian Barat
    Dirasakan : Dirasakan (Skala MMI): II Kairatu
    :return:
    """
    hasil = dict ()
    hasil ['tanggal'] = '4 April 2022'
    hasil ['waktu'] = '00:45:31 WIB'
    hasil ['magnitudo'] = 2.9
    hasil ['kedalaman'] = '10 KM'
    hasil ['lokasi'] = '3.35 LS - 128.38 BT'
    hasil ['pusat'] = 'Pusat gempa berada di darat 3 km timur Kairatu,Seram Bagian Barat'
    hasil ['dirasakan'] = 'Dirasakan (Skala MMI): II Kairatu'
    return hasil


def tampilkan_data(result):
    print('Informasi Gempa berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Pusat : {result['pusat']}")
    print(f"Dirasakan : {result['dirasakan']}")


if __name__ == '__main__'
    print('Aplikasi utama')
    result = ekstraksi_data ()
    tampilkan_data(result)