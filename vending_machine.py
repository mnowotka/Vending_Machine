class VendingMachine:
    def __init__(self, floors, slots, products):
        pass
        # self.floors = floors
        # self.slots = slots
        # self.products = products
        # self.machine = [[[Slot(floors) for _ in self.floors] for _ in self.slots] for _ in self.products]

    def free_space(self):
        free_spots = 0
        for floors in self.machine:
            for slots in floors:
                for products in slots:
                    free_spots +=1
        return free_spots


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Slot:
    def __init__(self, floor):
        self.floor = floor
        self.taken = False


class NomoneyException(Exception):
    pass

