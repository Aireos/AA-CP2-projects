#Alex Anderson Movie Recommender

import csv



def movies_maker():
    movie_dictionary = {}

    with open("Personal Projects/Movie Recommender/Movies list.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            movie = {
                "director":row[1],
                "rating":row[3],
                "length":row[4]
            }
            movie_name = row[0]
            movie_dictionary[movie_name] = movie

    return movie_dictionary


def movies_printer(movie_dictionary):
    print("Here is a list of all the available movies:")
    print("-------------------------------------------------------")
    for movie_name, details in movie_dictionary.items():
        print(f"Name: {movie_name}")
        print(f"Director: {details["director"]}")
        print(f"Rating: {details["rating"]}")
        print(f"Length in minutes: {details["length"]}")
        print("-------------------------------------------------------")



def filter_one(movie_dictionary):
    filter_input_one = input("What is the range you want your movie length to be in? (write like this: 100-120): ")
    filter_one_movies = []
    sanitized_one = filter_input_one.split("-")
    sanitized_one_min = int(sanitized_one[0])
    sanitized_one_max = int(sanitized_one[1]) + 1
    for number in range(sanitized_one_min, sanitized_one_max):
        for movie_name, details in movie_dictionary.items():
            if number == int(details["length"]):
                filter_one_movies += {movie_name}
    return filter_one_movies



def filter_two(filter_one_movies, movie_dictionary):
    filter_two_movies = []
    filter_input_two = input("What is the rating of the movie you want to find? (R, PG-13, or PG): ")
    for item in filter_one_movies:
        if movie_dictionary[item]["rating"] == filter_input_two:
            filter_two_movies.append(item)
    return filter_two_movies



def print_filtered(filtered_movies, movie_dictionary):
    for item in filtered_movies:
        movie_details = movie_dictionary


movie_dictionary = movies_maker()
movies_printer(movie_dictionary)
filter_one_movies = filter_one(movie_dictionary)
filter_two_movies = filter_two(filter_one_movies, movie_dictionary)