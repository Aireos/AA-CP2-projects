# Alex Anderson Word Counter

import file_handler
import time_handler

def main():
    # Ask user for the filename
    file_name = "Personal Projects/Word Counter/" + input("Enter the file name (with extension, example: document.txt): ").strip()

    # Reads the file content  
    content = file_handler.read_file(file_name)

    # If the file couldn't be read, exits the program
    if content is None:
        return

    # Splits the content into lines
    lines = content.strip().split("\n")

    # Makes sure the time stamp is not included in the number of words.
    if len(lines) >= 2 and lines[-2].startswith("Word Count:") and lines[-1].startswith("Last Updated:"):
        content = "\n".join(lines[:-2])

    # Counts the number of words in the file
    word_count = file_handler.count_words(content)
    
    # Get the current time and date
    timestamp = time_handler.get_current_timestamp()

    #Updated content with word count and timestamp
    updated_content = f"{content.strip()}\n\nWord Count: {word_count}\nLast Updated: {timestamp}"
    
    # Brings the updated content back to the file
    file_handler.write_file(file_name, updated_content)

    print(f"Word count: {word_count} and the timestamp for this is: {timestamp}")

main()


