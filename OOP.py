class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk : {self.nama}")
        print(f"Harga       : Rp{self.harga:,}")

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 0.05
        else:
            return 0

jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

total_seluruh = 0

print()

for i in range(jumlah_produk):
    print(f"--- Produk ke-{i + 1} ---")

    nama = input("Nama produk : ")
    harga = int(input("Harga produk : Rp. "))
    jumlah = int(input("Jumlah beli : "))

    produk = Produk(nama, harga)
    produk.tampilkan_info()
    total_produk = produk.hitung_total(jumlah)

    print(f"Total produk : Rp{total_produk:,}")
    print()
    total_seluruh += total_produk


produk_diskon = Produk("", 0)
diskon = produk_diskon.hitung_diskon(total_seluruh)
total_bayar = total_seluruh - diskon



print("=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : Rp{total_seluruh:,}")
print(f"Diskon 5%       : Rp{diskon:,}")
print(f"Total Bayar     : Rp{total_bayar:,}")