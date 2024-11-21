class Rectangle:
    def __init__(self, length, width):
        """To'g'ri to'rtburchakning uzunligi va kengligini belgilaydi."""
        self.length = length
        self.width = width

    def perimeter(self):
        """To'g'ri to'rtburchakning perimetrini hisoblaydi."""
        return 2 * (self.length + self.width)

    def area(self):
        """To'g'ri to'rtburchakning yuzini hisoblaydi."""
        return self.length * self.width


# 5 ta to'g'ri to'rtburchak yaratish va ularning perimetri va yuzini hisoblash
rectangles = []

for i in range(5):
    length = float(input(f'{i + 1}-to\'g\'ri to\'rtburchak uchun uzunlikni kiriting: '))
    width = float(input(f'{i + 1}-to\'g\'ri to\'rtburchak uchun kenglikni kiriting: '))
    
    rectangle = Rectangle(length, width)
    rectangles.append(rectangle)

# Har bir to'g'ri to'rtburchakning perimetri va yuzini chiqarish
print("\nTo'g'ri to'rtburchaklar:")
for i, rectangle in enumerate(rectangles):
    print(f"{i + 1}-to'g'ri to'rtburchak:")
    print(f"  Uzunlik: {rectangle.length}")
    print(f"  Kenglik: {rectangle.width}")
    print(f"  Perimetr: {rectangle.perimeter()}")
    print(f"  Yuz: {rectangle.area()}")
