"""
Aplikasi deteksi gempa
"""
from beritapopuler import ekstraksi_data, tampilkan_data

if __name__ == '__main__' :
    #print('Aplikasi utama')
    result = ekstraksi_data ()
    tampilkan_data(result)