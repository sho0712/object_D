"""
課題D-2: 長方形オブジェクト
次のコードが正しく動作するような Rectangle クラスを実装してください
diagonal は 対角線(の長さ) という意味です。
rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return f"{((self.height ** 2) + (self.width ** 2)) ** 0.5:.2f}"


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
