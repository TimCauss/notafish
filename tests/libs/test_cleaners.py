from Libs.cleaners import clean_email
import unittest


class TestCleanemail(unittest.TestCase):

    test_cases = {
        "My email is example@example.com thank you.": "My email is thank you.",
        "example@example.com is my email.": "is my email.",
        "test.com is not an email.": "test.com is not an email.",
    }

    def test_clean_email(self):
        for input_text, expected_output in self.test_cases.items():
            with self.subTest(input_text=input_text):
                self.assertEqual(clean_email(input_text), expected_output)


if __name__ == '__main__':
    unittest.main()
