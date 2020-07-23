import unittest
from vending_machine import *


class VendingMachineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.money = 20
        self.floors = 4
        self.slots_for_products = 6
        self.products = 5
        self.machine = VendingMachine(floors=self.floors,
                                      slots=self.slots_for_products,
                                      products=self.products)
        self.slots = []
        for product_slot in range(self.floors * self.slots_for_products):
            for product in range(self.products):
                self.product = Product(f'1234{product_slot}', 1 + product_slot)
                slot = self.machine.put(self.product)  # filling machine with products
                self.slots.append(slot)

    def test_putting_money(self):
        pass

    def test_chosing_the_product(self):
        pass

    def test_taking_product_and_giving_rest(self):
        self.machine.take("12345",
                          3)  # method will remove product from machine, also it will return the price of product
        for product_slot in range(self.floors * self.slots_for_products):
            for product in range(self.products):
                if self.slots[product_slot][product].name == "12345":
                    self.product_price = self.slots[product_slot][product].price
                    self.slots[product_slot][product].name = None
                    break
        self.machine.pay(self.money, self.product_price)  # method checking your money and returning rest
        rest = self.money - self.product_price
        self.assertEqual(rest, self.machine.pay(self.money, self.product_price))
        machine_without_product = self.machine.full_machine - 1
        self.assertEqual(machine_without_product, 119)

    def test_taking_all_products(self):
        for product_slot in range(self.floors * self.slots_for_products):
            for product in range(self.products):
                self.machine.take(f'1234{product_slot}', 1 + product_slot)
                self.slots[product_slot][product].name = None
        lenght = 0
        for product_slot in range(self.floors * self.slots_for_products):
            for product in range(self.products):
                if self.slots[product_slot][product].name != 'None':
                    lenght += 1
        self.assertEqual(self.machine.free_space, lenght)

    def test_checking_if_you_got_money(self):
        self.moneys = self.money
        for product_slot in range(0, 1):
            for product in range(3):
                if self.slots[product_slot][product].name == f'1234{product_slot}':
                    product_price = self.slots[product_slot][product].price
                    self.machine.take(f'1234{product_slot}', 1 + product_slot)
                    self.moneys = self.money - product_price
                    self.assertEqual(self.moneys, self.machine.pay(product_price))
                    if self.moneys <= self.slots[product_slot][product].price:
                        self.assertRaises(NomoneyException)

    def test_if_product_is_avaiable(self):
        for product_slot in range(self.floors * self.slots_for_products):
            for product in range(self.products):
                if self.slots[product_slot][product].name == '12341':
                    self.machine.isavaiable(self.slots[product_slot][product].name)
                    self.machine.take('12341', 2)
                    self.slots[product_slot][product].name = None
        self.assertFalse(self.machine.isavaiable('12341'))
        there_is_product = 0
        for product_slot in range(self.floors * self.slots_for_products):
            for product in range(self.products):
                if self.slots[product_slot][product].name == '12341':
                    there_is_product += 1
        if there_is_product == 0:
            self.assertRaises(NoproducException)


if __name__ == '__main__':
    unittest.main()
