import re


def extract_contact_info(text):
    phone_patterns = [
        r"[\d٠-٩]{11}",  # Matches 11 digits (ASCII or Arabic)
        r"\W2[\d٠-٩]{11}",  # Matches a non-word character, then '2', then 11 digits
        r"[\d٠-٩]{3}\s[\d٠-٩]{4}\s[\d٠-٩]{4}",  # Matches 3 digits, space, 4 digits, space, 4 digits
        r"\+20\s[\d٠-٩]{3}\s[\d٠-٩]{4}\s[\d٠-٩]{3}",  # Matches '+20', space, 3 digits, space, 4 digits, space, 3 digits
    ]
    matches_phone = []
    for pattern in phone_patterns:
        matches_phone.extend(re.findall(pattern, text))

    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    matches_email = []
    matches_email.extend(re.findall(email_pattern, text))
    contact = [matches_phone, matches_email]
    return contact
