import unittest
from app import Products, Product
from db import ProductModel
from peewee import *


class MyTest(unittest.TestCase):
    def test_get_products(self):

        products_instance = Products()

        expected = [row.to_dict() for row in ProductModel().select()]

        result = products_instance.get()

        self.assertEqual(result, expected)

    def test_post(self):

        products_instance = Products()

        expected = [row.to_dict() for row in ProductModel().select()]

        result = products_instance.post()

        self.assertEqual(result, expected)


    def test_get_by_id(self):

        product_id = "1"

        product_instance = Product()


        try:
            product = ProductModel.get(ProductModel.id == product_id)
            expected = product.to_dict()
        except DoesNotExist:
            expected = None


        result = product_instance.get("1")

        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()