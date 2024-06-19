import re


def extract_contact_info(text):
    """
    Add text passage.

    Parameters
    ----------
    text: string

    Returns
    -------
    dictionary with 'phone number(s)' and 'email(s)'
    """
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
    contact = {"mobile": matches_phone, "email": matches_email}
    return contact


def seperate_posts_from_whatsapp_bulk_text(bulk):
    """
    Add WhatApp text bulk.

    Parameters
    ----------
    bulk: string

    Returns
    -------
    list (of strings) containing each message as an element excluding
    repeated format

    Example
    -------
    ['message 1',
    'message 2',
    'message 3']
    """
    # These patterns extract the message right after the repeated format exclusively
    unsaved_ctc_sep_pat = (
        r"\[.*?\] \+\d+ \d{2} \d{7}:\s*(.*)"  # Unsaved Contact Seperator Pattern
    )

    saved_ctc_sep_pat = r"\[.*?\] .*?, .*?:\s*(.*)"  # Saved Contact Seperator Pattern
    ctc_sep_pat = [
        unsaved_ctc_sep_pat,
        saved_ctc_sep_pat,
    ]  # Merge between both patterns

    extracted_message = []  # Emtpy list to store the actual messages

    # For Loop done for each pattern saved and unsaved seperators
    for pattern in ctc_sep_pat:
        matches = re.findall(pattern, bulk)  # Put all matches in a list
        for match in matches:
            extracted_message.append(match)
            # Stores all list elements in 'extracted_message' list
    return extracted_message
