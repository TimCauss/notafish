from Libs.cleaners import clean_html, clean_email, clean_url

## Refactor this module, it's for clean and prepare a mail to be read by an IA model.
## Maybe use dict for listing function by cleaned object


def clean_email(email):
    cleaned_email = email
    cleaned_email = clean_html(email)
    cleaned_email = clean_email(email)
    cleaned_email = clean_url(email)