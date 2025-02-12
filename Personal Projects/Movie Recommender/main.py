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


movie_dictionary = movies_maker()
movies_printer(movie_dictionary)
