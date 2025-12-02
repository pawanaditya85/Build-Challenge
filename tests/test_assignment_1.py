import unittest
import threading
from src.assignment_1 import DataTransferSystem

class TestProducerConsumer(unittest.TestCase):
    def test_transfer_integrity(self):
        """Test that all items from source move to destination."""
        source_data = ["Item1", "Item2", "Item3", "Item4", "Item5"]
        
        # Initialize system
        system = DataTransferSystem(list(source_data)) # Pass a copy
        
        # Run the transfer
        result = system.run_transfer()
        
        # Verify: Result count must match source count
        self.assertEqual(len(result), 5)
        
        # Verify: The actual content matches
        self.assertEqual(result, source_data)

if __name__ == '__main__':
    unittest.main()