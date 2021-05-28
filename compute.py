listt = [
    {"type": "Square", "area": 150.5},
    {"type": "Rectangle", "area": 80},
    {"type": "Rectangle", "area": 660},
    {"type": "Circle", "area": 68.2},
    {"type": "Triangle", "area": 20}
]
class Geometry:
    x = 5
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def get_type(self):
        return self.type 

    def get_area(self):
        return self.area

g1 = Geometry("Square", 150.5)
g2 = Geometry("Rectangle", 80)
g3 = Geometry("Rectangle", 660)
g4 = Geometry("Circle", 68.2)
g4 = Geometry("Triangle", 20)


for i in range(len(listt)):
    print(f'{i+1}- {listt[i]["type"]} with area size {listt[i]["area"]}')