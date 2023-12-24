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


## Refactor this module, it's for clean and prepare a mail to be read by an IA model.
## Maybe use dict for listing function by cleaned object


standardization_functions = {
    "email" : {
        "clean": [clean_html, clean_url, clean_email],
        "format": [],
        "standardize": []
    }
    
}
