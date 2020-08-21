class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Room():
    def __init__(self, location, area):
        self.location = location
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'您的家地理位置为{self.location},您的家的面积为{self.area},您的家的剩余面积为{self.free_area},您的家家具有{self.furniture}'

    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
            pass
        else:

            print('剩余空间不足')


Home1 = Room('西安', 120)
bed = Furniture('双人床', 61)
sofa = Furniture('沙发', 60)
Home1.add_furniture(bed)
Home1.add_furniture(sofa)
print(Home1)


