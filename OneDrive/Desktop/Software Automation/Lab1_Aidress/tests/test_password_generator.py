import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.password_generator import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_correct_length(self):
        """Test if the generated password has the correct length."""
        password = generate_password(12, 6, 3, 3)
        self.assertEqual(len(password), 12)

    def test_contains_letters_digits_specials(self):
        """Test if the password contains the correct number of letters, digits, and special characters."""
        password = generate_password(10, 4, 3, 3)
        letters = sum(c.isalpha() for c in password)
        digits = sum(c.isdigit() for c in password)
        specials = sum(not c.isalnum() for c in password)
        
        self.assertEqual(letters, 4)
        self.assertEqual(digits, 3)
        self.assertEqual(specials, 3)

    def test_invalid_length(self):
        """Test if an error is raised for passwords shorter than 8 characters."""
        with self.assertRaises(ValueError):
            generate_password(7, 3, 2, 2)  # Invalid length

    def test_exceeding_total_length(self):
        """Test if an error is raised when the sum of characters exceeds the total length."""
        with self.assertRaises(ValueError):
            generate_password(8, 5, 5, 5)  # 15 total chars for length 8

    def test_negative_values(self):
        """Test if an error is raised for negative values in input."""
        with self.assertRaises(ValueError):
            generate_password(10, -1, 5, 5)  # Negative number of letters

if __name__ == "__main__":
    unittest.main()
