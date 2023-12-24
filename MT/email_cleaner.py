from Libs.cleaners import clean_html, clean_email, clean_url




def clean_email(email):
    cleaned_email = email
    cleaned_email = clean_html(email)
    cleaned_email = clean_email(email)
    cleaned_email = clean_url(email)