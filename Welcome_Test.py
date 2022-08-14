import unittest
import welcome


class TestFilter(unittest.TestCase):

    def setUp(self) -> None:
        apple = welcome.Product('apple', welcome.Color.GREEN,
                                welcome.Size.SMALL)
        tree = welcome.Product('tree', welcome.Color.GREEN, welcome.Size.LARGE)
        house = welcome.Product('house', welcome.Color.BLUE, welcome.Size.LARGE)

        self.products = [apple, tree, house]
        self.products_filter = welcome.ProductFilter()

    def test_is_name(self):
        blue = welcome.ColorSpecification(welcome.Color.BLUE)
        for product in self.products_filter.filter(self.products, blue):
            self.assertEqual(product.name, 'house')

    def test_wrong_color(self):
        with self.assertRaises(AttributeError):
            for product in self.products_filter.filter(self.products, 'Blue'):
                self.assertEqual(product.color, welcome.Color.GREEN)

    # def test_wrong_end(self):
    #     large_and_blue = welcome.SizeSpecification(welcome.Size.LARGE) & \
    #                      welcome.ColorSpecification(welcome.Color.BLUE)
    #     print(large_and_blue)
    #     for product in self.products_filter.filter((self.products,
    #                                                 large_and_blue)):
    #         print(f'{product.name} is LARGE and BLUE with __and__ overload')



unittest.main()
