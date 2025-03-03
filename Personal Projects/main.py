#Alex Anderson Word Counter

import file_handler
import time_handler

def main():
    # Ask user for the filename
    file_name = input("Enter the file name (with extension, example: document.txt): ").strip()

    # Read the file content
    content = file_handler.read_file(file_name)

    # If the file couldn't be read, exit the program
    if content is None:
        print("Exiting program due to file error.")
        return

    # Count the number of words in the file
    word_count = file_handler.count_words(content)
    
    # Get the current timestamp
    timestamp = time_handler.get_current_timestamp()

    # Prepare updated content with word count and timestamp
    updated_content = f"{content.strip()}\n\n---\nWord Count: {word_count}\nLast Updated: {timestamp}\n"
    
    # Write the updated content back to the file
    file_handler.write_file(file_name, updated_content)

    # Notify the user that the file has been updated
    print(f"Word count ({word_count}) and timestamp updated in '{file_name}'.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
