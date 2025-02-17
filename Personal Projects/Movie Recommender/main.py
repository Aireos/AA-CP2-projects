import csv

# Function to read the movie data and store it in a dictionary
def movies_maker():
    movie_dictionary = {}

    try:
        with open("Personal Projects/Movie Recommender/Movies list.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                try:
                    # Attempt to parse movie data
                    movie = {
                        "director": row[1],
                        "genre": row[2],
                        "rating": row[3],
                        "length": row[4],
                        "actors": row[5]
                    }
                    movie_name = row[0]
                    movie_dictionary[movie_name] = movie
                except IndexError:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

    return movie_dictionary

# Function to create a list of all available movie names
def filtered_movies_maker(movie_dictionary):
    return list(movie_dictionary.keys())

# Function to print out all movies with details
def movies_printer(movie_dictionary):
    print("Here is a list of all the available movies:")
    print("-------------------------------------------------------")
    for movie_name, details in movie_dictionary.items():
        print(f"Name: {movie_name}")
        print(f"Director: {details['director']}")
        print(f"Genre: {details['genre']}")
        print(f"Rating: {details['rating']}")
        print(f"Length in minutes: {details['length']}")
        print(f"Actors: {details['actors']}")
        print("-------------------------------------------------------")

# Filter movies based on length
def filter_one(filtered_movies, movie_dictionary):
    while True:
        try:
            filter_input_one = input("What is the range you want your movie length to be in? (write like this: 100-120): ")
            filter_one_movies = []
            sanitized_one = filter_input_one.split("-")
            
            # Ensure valid integers
            sanitized_one_min = int(sanitized_one[0])
            sanitized_one_max = int(sanitized_one[1]) + 1
            
            for number in range(sanitized_one_min, sanitized_one_max):
                for movie_name, details in movie_dictionary.items():
                    if number == int(details["length"]) and movie_name in filtered_movies:
                        filter_one_movies.append(movie_name)
            return filter_one_movies
        except ValueError:
            print("Error: Please ensure the length range is in the correct format (e.g., 100-120). Try again.")
        except Exception as e:
            print(f"An unexpected error occurred while processing the input: {e}")
            return filtered_movies  # Return unfiltered list in case of error

# Filter movies based on rating
def filter_two(filtered_movies, movie_dictionary):
    while True:
        filter_two_movies = []
        filter_input_two = input("What is the rating of the movie you want to find? (R, PG-13, or PG): ").strip()
        if filter_input_two not in ['R', 'PG-13', 'PG']:
            print("Error: Invalid rating. Please enter 'R', 'PG-13', or 'PG'.")
        else:
            for item in filtered_movies:
                if movie_dictionary[item]["rating"] == filter_input_two:
                    filter_two_movies.append(item)
            return filter_two_movies

# Filter movies based on director
def filter_three(filtered_movies, movie_dictionary):
    while True:
        filter_three_movies = []
        filter_input_three = input("What is the name of the director you want to find?: ").strip()
        if not filter_input_three:
            print("Error: Please enter a valid director name.")
        else:
            for movie_name, details in movie_dictionary.items():
                if filter_input_three.lower() in details["director"].lower() and movie_name in filtered_movies:
                    filter_three_movies.append(movie_name)
            return filter_three_movies

# Filter movies based on actor
def filter_four(filtered_movies, movie_dictionary):
    while True:
        filter_four_movies = []
        filter_input_four = input("What actor's movies do you want to find?: ").strip()
        if not filter_input_four:
            print("Error: Please enter a valid actor name.")
        else:
            for movie_name, details in movie_dictionary.items():
                actors = details["actors"].split(", ")
                if filter_input_four.lower() in [actor.lower() for actor in actors] and movie_name in filtered_movies:
                    filter_four_movies.append(movie_name)
            return filter_four_movies

# Print out the filtered movies with details
def print_filtered(filtered_movies, movie_dictionary):
    print("Here is a list of all the movies that fit your needs:")
    print("-------------------------------------------------------")
    for movie_name, details in movie_dictionary.items():
        if movie_name in filtered_movies:
            print(f"Name: {movie_name}")
            print(f"Director: {details['director']}")
            print(f"Genre: {details['genre']}")
            print(f"Rating: {details['rating']}")
            print(f"Length in minutes: {details['length']}")
            print(f"Actors: {details['actors']}")
            print("-------------------------------------------------------")

# Function to display the filter choices
def filter_choice(filtered_movies, movie_dictionary):
    while True:
        try:
            print("Choose the filters you would like to apply:")
            print("1. Filter by Length")
            print("2. Filter by Rating")
            print("3. Filter by Director")
            print("4. Filter by Actor")
            print("5. Print All Movies")

            filter_choices = input("Enter the numbers of the filters you want to use (separate with commas, e.g., 1,3) or '5' to print all movies: ").strip()

            # Check for valid input (either two filters or '5')
            if filter_choices == '5':
                print_filtered(filtered_movies, movie_dictionary)
                return
            filters = filter_choices.split(",")
            
            # Ensure exactly two filters or 5 are selected
            if len(filters) != 2 or not all(f in ['1', '2', '3', '4'] for f in filters):
                print("Error: Please enter either two filters (e.g., 1,2) or '5' to print all movies.")
                continue

            # Apply filters progressively to the filtered list
            for filter_choice in filters:
                if filter_choice == '1':
                    filtered_movies = filter_one(filtered_movies, movie_dictionary)
                elif filter_choice == '2':
                    filtered_movies = filter_two(filtered_movies, movie_dictionary)
                elif filter_choice == '3':
                    filtered_movies = filter_three(filtered_movies, movie_dictionary)
                elif filter_choice == '4':
                    filtered_movies = filter_four(filtered_movies, movie_dictionary)
            
            print_filtered(filtered_movies, movie_dictionary)
            return  # Exit after displaying results

        except ValueError:
            print("Error: Invalid input. Please enter the filter numbers correctly.")
        except Exception as e:
            print(f"An unexpected error occurred while applying filters: {e}")

# Main function to tie everything together
def main():
    try:
        movie_dictionary = movies_maker()
        filtered_movies = filtered_movies_maker(movie_dictionary)
        filter_choice(filtered_movies, movie_dictionary)
    except Exception as e:
        print(f"An error occurred in the main program: {e}")

# Run the program
main()
