import unittest
from Libs.cleaners import clean_email
# Correct the imports


class TestCleanemail(unittest.TestCase):

    def test_clean_email(self):
        self.assertEqual(clean_email(
            "My email is example@example.com thank you."), "My email is thank you.")
        self.assertEqual(clean_email(
            "example.com is my email."), " is my email.")


if __name__ == '__main__':
    unittest.main()
