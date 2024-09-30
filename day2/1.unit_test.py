import unittest, os

def process_orders(orders):
    """
    Processes a list of orders and calculates the total price.
    Each order contains multiple items. Each item is a dictionary with 'name', 'quantity', 'price', and 'discount'.
    Handles edge cases such as missing fields, negative values, and invalid discounts.
    """
    total_price = 0
    total_items = 0
    
    for order in orders:
        for item in order.get('items', []):
            name = item.get('name', '')
            quantity = item.get('quantity', 0)
            price = item.get('price', 0)
            discount = item.get('discount', 0)
            
            # Edge case handling: Skip items with invalid or negative values
            if quantity <= 0 or price <= 0 or discount < 0 or discount > 100:
                continue

            # Calculate price after discount
            item_price = quantity * price * (1 - discount / 100)
            total_price += item_price
            total_items += quantity

    # Apply bulk discount if total items exceed 100
    if total_items > 100:
        total_price *= 0.95  # Apply a 5% discount

    return total_price

import unittest

class TestProcessOrders(unittest.TestCase):
    def test_normal_orders(self):
        # TODO: Write a test case for normal orders with valid data
        pass  # Remove this pass statement after completing the code

    def test_invalid_data(self):
        # TODO: Write a test case to handle orders with invalid data (e.g., negative values)
        pass  # Remove this pass statement after completing the code

    def test_bulk_discount(self):
        # TODO: Write a test case to verify the bulk discount is applied correctly when total items > 100
        pass  # Remove this pass statement after completing the code

    def test_empty_orders(self):
        # TODO: Write a test case for when the list of orders is empty
        pass  # Remove this pass statement after completing the code

    def test_missing_fields(self):
        # TODO: Write a test case for handling orders with missing fields (e.g., missing quantity or price)
        pass  # Remove this pass statement after completing the code

    def test_large_numbers(self):
        # TODO: Write a test case for handling very large numbers in quantity, price, or discount
        pass  # Remove this pass statement after completing the code

if __name__ == "__main__":
    unittest.main()
