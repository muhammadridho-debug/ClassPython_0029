# rectangle.py
# Program kelas persegi panjang
class Rectangle:
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        
        self.length = length
        self.width = width