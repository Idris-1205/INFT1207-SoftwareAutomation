# Aidress's Files

import unittest
from src.temperature_sensor import process_temperatures

class TestTemperatureSensor(unittest.TestCase):

    def test_min_boundary(self):
        self.assertEqual(process_temperatures([-50]), "Min: -50.0°C, Max: -50.0°C, Avg: -50.0°C")

    def test_max_boundary(self):
        self.assertEqual(process_temperatures([150]), "Min: 150.0°C, Max: 150.0°C, Avg: 150.0°C")

    def test_near_boundaries(self):
        self.assertEqual(process_temperatures([-49, 149]), "Min: -49.0°C, Max: 149.0°C, Avg: 50.0°C")

    def test_mixed_valid_invalid(self):
        self.assertEqual(process_temperatures([-60, 20, 160]), "Out-of-bound value detected!!")

    def test_alphabetic_characters(self):
        self.assertEqual(process_temperatures([20, "abc", 30]), "Invalid input detected!!")

    def test_special_characters(self):
        self.assertEqual(process_temperatures([10, "@", -40]), "Invalid input detected!!")

    def test_large_values(self):
        self.assertEqual(process_temperatures([2**31 - 1, -2**31]), "Out-of-bound value detected!!")

    def test_all_same_values(self):
        self.assertEqual(process_temperatures([50, 50, 50]), "Min: 50.0°C, Max: 50.0°C, Avg: 50.0°C")

    def test_empty_list(self):
        self.assertEqual(process_temperatures([]), "No valid input provided.")

if __name__ == "__main__":
    unittest.main()
