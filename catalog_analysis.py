import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 5:
        return "хорошо" if rating >= 7 else "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_titles(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    index = 0
    found = None
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            found = movies[index]
            print(found["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")
    return found


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = []
    for word in title.split():
        words.append(word[0].upper() + word[1:])
    return " ".join(words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in ordered]


def top_n_by_rating(movies, n=3):
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in ordered[:n]]


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, []) + [movie["title"]]
    return filmography


def ratings_above_average(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_high_rated_duration(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


def build_report(movies):
    movies_by_title = {movie["title"]: movie for movie in movies}
    average_age = catalog_age_stats(movies)[2]

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")

    print()
    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies):
        print(f"  {format_report_line(movies_by_title[title])}")

    print()
    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies).items()
    for genre, count in sorted(genre_counts, key=lambda item: (-item[1], item[0])):
        print(f"  {genre} — {count}")

    print()
    genres_line = ", ".join(sorted(all_genres(movies)))
    print(f"Все жанры каталога: {genres_line}")


def show_demos(movies):
    print("Фильмы не из жанра comedy:")
    print_non_comedy_titles(movies)

    print()
    print("Первый фильм с рейтингом выше 9.0:")
    find_first_masterpiece(movies)

    print()
    print("Поиск среди первых трех фильмов, где таких нет:")
    find_first_masterpiece(movies[:3])

    print()
    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")

    print()
    print("Фильмы с рейтингом от 8.0:")
    print_high_rated(movies)

    print()
    total_duration = total_high_rated_duration(movies)
    print(f"Суммарная длительность фильмов с рейтингом выше 7: {total_duration} мин")


if __name__ == "__main__":
    show_demos(movies)
    print()
    build_report(movies)
