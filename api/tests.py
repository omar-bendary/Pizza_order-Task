from django.test import TestCase
from .models import Order


class OrderTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_order = Order.objects.create(desired_pizza='Test pizza', number_of_pizza='5', size='S',
                                          customer_name="Test name", customer_number='0', customer_address='Test address', status='ORDER PLACED')
        test_order.save()

    def test_order_content(self):
        order = Order.objects.get(id=1)
        desired_pizza = f'{order.desired_pizza}'
        number_of_pizza = f'{order.number_of_pizza}'
        size = f'{order.size}'
        customer_name = f'{order.customer_name}'
        customer_number = f'{order.customer_number}'
        customer_address = f'{order.customer_address}'
        status = f'{order.status}'

        self.assertEqual(desired_pizza, 'Test pizza')
        self.assertEqual(number_of_pizza, '5')
        self.assertEqual(size, 'S')
        self.assertEqual(customer_name, 'Test name')
        self.assertEqual(customer_number, '0')
        self.assertEqual(customer_address, 'Test address')
        self.assertEqual(status, 'ORDER PLACED')
