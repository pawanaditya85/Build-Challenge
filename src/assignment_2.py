import csv
import os
from functools import reduce
from typing import Iterator, Dict

class SalesAnalytics:
    # UPDATE: Add 'custom_path' argument so tests can inject their own file
    def __init__(self, custom_path=None):
        if custom_path:
            self.filepath = custom_path
        else:
            # Default logic for Production (Pro) run
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.filepath = os.path.join(script_dir, '..', 'data', 'sales_data.csv')

    def _get_data_stream(self) -> Iterator[Dict]:
        if not os.path.exists(self.filepath):
            print(f"Error: File not found at {self.filepath}")
            return

        try:
            with open(self.filepath, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f, skipinitialspace=True)
                for row in reader:
                    yield {k.strip(): v.strip() for k, v in row.items() if k and v}
        except Exception as e:
            print(f"Error reading file: {e}")
            return

    def get_total_sales_by_category(self, target_category: str) -> float:
        stream = self._get_data_stream()
        category_filter = filter(lambda row: row.get('category') == target_category, stream)
        sales_map = map(lambda row: float(row['sales']), category_filter)
        total_sales = reduce(lambda acc, curr: acc + curr, sales_map, 0.0)
        return round(total_sales, 2)

    def get_average_profit_by_region(self, target_region: str) -> float:
        stream = self._get_data_stream()
        region_filter = filter(lambda row: row.get('region') == target_region, stream)
        profit_map = map(lambda row: float(row['profit']), region_filter)
        profit_list = list(profit_map)
        
        if not profit_list:
            return 0.0

        total_profit = reduce(lambda acc, curr: acc + curr, profit_list, 0.0)
        return round(total_profit / len(profit_list), 2)

if __name__ == "__main__":
    analyzer = SalesAnalytics()
    print("--- Analysis Results ---")
    print(f"Total Sales (Furniture): ${analyzer.get_total_sales_by_category('Furniture')}")
    print(f"Average Profit (West Region): ${analyzer.get_average_profit_by_region('West')}")