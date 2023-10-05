import json
from django.shortcuts import render


def movies(request):
    with open("movies/index.json") as file:
        json_data = json.load(file)

    all_movies = []
    for date_data in json_data:
        all_movies.extend(date_data.get("movies", []))

    all_genres = set()
    for movie in all_movies:
        all_genres.update(movie.get("genre", []))

    context = {
        "movies": all_movies,
        "all_genres": all_genres,
    }
    print(context)
    return render(request, "movie_template.html", context)
