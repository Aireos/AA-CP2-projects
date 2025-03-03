#Alex Anderson Word Counter

from datetime import datetime

def get_current_timestamp():
    # Returns the current time formatted as 'YYYY-MM-DD HH:MM:SS'
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
