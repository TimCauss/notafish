from Libs.cleaners import clean_url
import pytest

test_cases = [
    ("Check out this link: http://example.com", "Check out this link: "),
    ("Secure site at https://secure.example.com", "Secure site at "),
    ("URL with path http://example.com/path/to/page.html", "URL with path "),
    ("Query URLs https://example.com/search?q=query", "Query URLs "),
    ("Port number https://example.com:8080/page", "Port number "),
    ("User info user:pass@example.com", "User info "),
    ("Fragment https://example.com/page#section", "Fragment "),
    ("Multiple URLs http://first.com and https://second.com", "Multiple URLs  and "),
    ("Parentheses (https://example.com)", "Parentheses ()"),
    ("In sentence http://example.com is a URL.", "In sentence  is a URL."),
    ("Comma separation http://example.com, text", "Comma separation , text"),
    ("FTP site ftp://example.com/files", "FTP site "),
    ("With credentials https://user:password@example.com", "With credentials "),
    ("Subdomain http://subdomain.example.com", "Subdomain "),
    ("IP address http://192.168.1.1", "IP address "),
    ("IPv6 address http://[::1]", "IPv6 address "),
    ("With port and path http://example.com:8080/path", "With port and path "),
    ("Trailing slash https://example.com/", "Trailing slash "),
    ("No HTTP www.example.com", "No HTTP "),
    ("HTTPS uppercase HTTPS://EXAMPLE.COM", "HTTPS uppercase "),
    ("URL in quotes 'http://example.com'", "URL in quotes ''"),
    ("URL ending with punctuation http://example.com.",
     "URL ending with punctuation ."),
    ("Bracketed URL [http://example.com]", "Bracketed URL []"),
    ("URL with special characters http://example.com/path/?q=te%20st",
     "URL with special characters "),
    ("Just a period .", "Just a period ."),
]


@pytest.mark.parametrize(
    "input_text, expected_output",
    test_cases,
    ids=[f"Test Case {i+1}" for i in range(len(test_cases))]
)
def test_clean_url(input_text: str, expected_output: str):
    assert clean_url(
        input_text) == expected_output, f"Failed for input: {input_text}"
