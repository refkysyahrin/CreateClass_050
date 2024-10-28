class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
    try:
        # Meminta input panjang dan lebar dari pengguna
        panjang = 3
        lebar = 2

        # Membuat objek PersegiPanjang dengan input pengguna
        PP = PersegiPanjang(panjang, lebar)

        # Menampilkan informasi objek
        print(PP)
        print("Keliling:", PP.hitung_keliling(), "cm")
        print("Luas:", PP.hitung_luas(), "cm²")
    
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")

# Memanggil fungsi main
if __name__ == "__main__":
    main()
    
    

