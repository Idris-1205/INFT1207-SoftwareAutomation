# Aidress's Files

import unittest
import builtins
from src.temperature_sensor import process_temperatures, main
from io import StringIO
import sys
import runpy

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

    def main_interactive(self):
        inputs = iter(["10 20 30", "no"])
        original_input = builtins.input
        builtins.input = lambda _: next(inputs)

        captured_outputs = StringIO()
        sys.stdout = captured_outputs

        try:
            main()
        finally:
            builtins.input = original_input
            sys.stdout = sys.__stdout__

        output_str = captured_outputs.getvalue()
        self.assertIn("Min: 10.0°C, Max: 30.0°C, Avg: 20.0°C", output_str)
        self.assertIn("Thank you for using the Temperature Sensor Analysis Tool.", output_str)  
    def test_main_script_block(self):
        # Test the __main__ block by running the module as a script.
        inputs = iter(["10 20 30", "no"])
        original_input = builtins.input
        builtins.input = lambda _: next(inputs)
        
        captured_output = StringIO()
        sys.stdout = captured_output

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            runpy.run_path("src/temperature_sensor.py", run_name="__main__")
        finally:
            builtins.input = original_input
            sys.stdout = sys.__stdout__

        output_str = captured_output.getvalue()
        self.assertIn("Min: 10.0°C, Max: 30.0°C, Avg: 20.0°C", output_str)
        self.assertIn("Thank you for using the Temperature Sensor Analysis Tool.", output_str)

if __name__ == "__main__":
    unittest.main()
