# rectangle.py
# Program kelas persegi panjang
class Rectangle:
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        
        self.length = length
        self.width = width

    def calculate_circumference(self) -> float:
        """Menghitung keliling persegi panjang."""
        return 2 * (self.length + self.width)
    
    def calculate_area(self) -> float:
        """Menghitung luas persegi panjang."""
        return self.length * self.width

    def __str__(self) -> str:
        """Mengembalikan representasi string dari objek."""
        len_val = int(self.length) if isinstance(self.length, float) and self.length.is_integer() else self.length
        wid_val = int(self.width) if isinstance(self.width, float) and self.width.is_integer() else self.width
        return f"rectangle, {len_val} cm long, and {wid_val} cm wide"