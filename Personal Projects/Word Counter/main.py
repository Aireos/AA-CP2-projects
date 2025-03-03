#Alex Anderson Word Counter

import file_handler
import time_handler

def main():
    # Ask user for the filename
    file_name = input("Enter the file name (with extension, example: document.txt): ").strip()

    # Reads the file content
    content = file_handler.read_file(file_name)

    # If the file couldn't be read, exit the program
    if content is None:
        print("Exiting program due to file error.")
        return

    # Counts the number of words in the file
    word_count = file_handler.count_words(content)
    
    # Get the current time and date
    timestamp = time_handler.get_current_timestamp()

    #Imports updated content with word count and timestamp
    updated_content = f"{content.strip()}\n\n---\nWord Count: {word_count}\nLast Updated: {timestamp}\n"
    
    #Brings the updated content back to the file
    file_handler.write_file(file_name, updated_content)

    print(f"Word count ({word_count}) and timestamp updated in '{file_name}'.")


if __name__ == "__main__":
    main()