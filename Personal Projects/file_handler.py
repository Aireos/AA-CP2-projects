#Alex Anderson Word Counter

def read_file(file_name):
    # Reads content from the specified file
    # Returns the content as a string or None if an error occurs
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        print(f"Error: Unable to read file '{file_name}'.")
        return None

def write_file(file_name, content):
    # Writes updated content back to the specified file
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
    except:
        print(f"Error: Unable to write to file '{file_name}'.")

def count_words(text):
    # Counts the number of words in the given text
    return len(text.split())
