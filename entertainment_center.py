import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "Storyline about a boy and his toys who come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc");

toy_story2 = media.Movie("Toy Story",
                        "Storyline about a boy and his toys who come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc");


movies = [toy_story, toy_story2]
fresh_tomatoes.open_movies_page(movies)
