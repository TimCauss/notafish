import re
from bs4 import BeautifulSoup

### Libs for cleaners and formaters used to format and/or
### remove unwanted from email

def clean_email(value):
    return re.sub(r'\S*@\S*\s?', '', value)

def clean_html(value):
    return BeautifulSoup(value, "html.parser").get_text()

def clean_url(value):
    return re.sub(r'http\S+', '', value)

def clean_char(value):
    pass #Define cleaner for spec characters