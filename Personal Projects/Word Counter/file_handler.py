#Alex Anderson Word Counter

def read_file(file_name):
    # Reads content from the file
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except:
        print("Unable to read file.")
        return None

def write_file(file_name, content):
    # Brings updated content back to the file
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except:
        print("Unable to write to file")

def count_words(text):
    # Counts the number of words in text
    return len(text.split())
