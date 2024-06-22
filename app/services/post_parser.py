import json
import os
import re
import unicodedata


def obtain_read_file():
    global read_file_name
    global downloads_path
    # Get the path to the Downloads directory
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Ask the user to input the filename
    read_file_name = input("Enter the name of the file in the Downloads folder: ")

    # Construct the full path to the file
    file_path = os.path.join(downloads_path, read_file_name)

    # Try to open the file and read its content
    try:
        with open(file_path, "r") as myfile:
            content = myfile.read()
        return content
    except FileNotFoundError:
        return f"File '{read_file_name}' not found in the Downloads folder."
    except Exception as e:
        return f"An error occurred: {e}"


def extract_contact_info(text):
    """
    Extract phone numbers and emails from text.

    Parameters
    ----------
    text: string

    Returns
    -------
    dictionary with 'mobile' and 'email'
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


def decode_unicode_text(text):
    return unicodedata.normalize("NFKD", text)


def seperate_posts_from_whatsapp_bulk_text(input_string):
    pattern = re.compile(
        r"\[(1[0-2]|0?[1-9]):([0-5][0-9])\s?(AM|PM|am|pm),\s?(\d{2}/\d{2}/\d{4})\]\s(\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}):\s?((?:.|\n)*?)(?=\[\d{1,2}:\d{2}\s?(?:AM|PM|am|pm),|\Z)",
        re.UNICODE,
    )

    matches = pattern.findall(input_string)
    results = []

    if not matches:
        return json.dumps(
            {"error": "Input string does not match the criteria"}, indent=4
        )

    for match in matches:
        time = f"{match[0]}:{match[1]} {match[2]}"
        date_time = f"{time}, {match[3]}"
        phone_number = match[4]
        free_text = decode_unicode_text(
            match[5].strip()
        )  # Ensure blank free text is handled correctly and decode
        result = {
            "Date-Time": date_time,
            "Phone Number": phone_number,
            "Free Text": free_text,
        }
        results.append(result)

    return results


# Calling the function
def extract_post_full_info_from_whatsapp_bulk_text():
    python_output = seperate_posts_from_whatsapp_bulk_text(obtain_read_file())
    result = []
    for entry in python_output:
        text_message = entry["Free Text"]
        contact_info = extract_contact_info(text_message)
        combined_entry = {**entry, **contact_info}  # Combine the two dictionaries
        result.append(combined_entry)

    # print(json.dumps(result, indent=2))
    end_result = json.dumps(result, ensure_ascii=False, indent=2)
    end_result = end_result.replace("\\n", "\n")
    return end_result


def write_parsed_messages_to_file():

    content = extract_post_full_info_from_whatsapp_bulk_text()
    # Define the filename
    filename = f"{read_file_name}_parsed_messages.txt"

    # Construct the full path to the file
    file_path = os.path.join(downloads_path, filename)

    # Call the extract_post_full_info_from_whatsapp_bulk_text function

    # Try to write the content to the file
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


write_parsed_messages_to_file()
