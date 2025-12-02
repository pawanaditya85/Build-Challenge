import unittest
import os
from src.assignment_2 import SalesAnalytics

class TestSalesAnalytics(unittest.TestCase):
    def setUp(self):
        """Create a temporary dummy CSV file before each test."""
        self.test_file = 'test_dummy_data.csv'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("order_id,category,region,sales,profit\n")
            f.write("1,Furniture,West,100.00,10.00\n")
            f.write("2,Furniture,East,200.00,20.00\n")
            f.write("3,Technology,West,500.00,50.00\n")
            f.write("4,Furniture,West,50.00,5.00\n")
        
        # Inject the custom test path!
        self.analyzer = SalesAnalytics(custom_path=self.test_file)

    def test_total_sales_by_category(self):
        # Logic: Furniture rows are 100.00 + 200.00 + 50.00 = 350.00
        total = self.analyzer.get_total_sales_by_category("Furniture")
        self.assertEqual(total, 350.00)

    def test_average_profit_by_region(self):
        # Logic: West Region rows are 10.00, 50.00, 5.00
        # Average: (10 + 50 + 5) / 3 = 21.67
        avg = self.analyzer.get_average_profit_by_region("West")
        self.assertEqual(avg, 21.67)

    def tearDown(self):
        """Delete the temporary file after tests finish."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()