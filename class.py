class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

# Contoh penggunaan
persegi_panjang = PersegiPanjang(3, 2)
print(persegi_panjang)               # Output: Persegi Panjang, panjang 3 cm, dan lebar 2 cm
print("Keliling:", persegi_panjang.keliling(), "cm")  # Output: Keliling: 10 cm
print("Luas:", persegi_panjang.luas(), "cm²")         # Output: Luas: 6 cm²
