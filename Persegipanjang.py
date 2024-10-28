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

# Contoh penggunaan
persegi_panjang = PersegiPanjang(3, 2)
print(persegi_panjang)  
print("Keliling:", persegi_panjang.hitung_keliling(), "cm")  
print("Luas:", persegi_panjang.hitung_luas(), "cm²")
