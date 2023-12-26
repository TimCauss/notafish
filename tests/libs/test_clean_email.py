import pytest
from Libs.cleaners import clean_email

test_cases = [
    ("My email is example@example.com thank you.", "My email is thank you."),
    ("example@example.com is my email.", "is my email."),
    ("test.com is not an email.", "test.com is not an email."),
]


@pytest.mark.parametrize(
    "input_text, expected_output",
    test_cases,
    ids=[f"Test Case {i+1}" for i in range(len(test_cases))]
)
def test_clean_email(input_text: str, expected_output: str):
    assert clean_email(
        input_text) == expected_output, f"Failed for input: {input_text}"
