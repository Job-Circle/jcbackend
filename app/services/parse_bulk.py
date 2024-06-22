from post_parser import *


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


def write_parsed_messages_to_file():

    content = extract_post_full_info_from_whatsapp_bulk_text(obtain_read_file())
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
