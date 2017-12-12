# MOSTLY CREATED BY FOLLOWING ALONG IN THE UDACITY LESSONS

import fresh_tomatoes
import media

# define some of my favorite movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio&t=10s")


avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")



interstellar = media.Movie("Interstellar",
                        "With our time on Earth coming to an end, a team of explorers undertakes the most important mission in human history: finding mankind's future among the stars",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://youtu.be/zSWdZVtXT7E")


dunkirk = media.Movie("Dunkirk",
                "Citizens attempt to rescue stranded soldiers",
                "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                "https://youtu.be/F-eMt3SrfFU")

amelie = media.Movie("Amelie",
                "Amelie meets her destiny.",
                "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                "https://youtu.be/HUECWi5pX7o")

about_time = media.Movie("About Time",
                    "Males in a family can travel back in time",
                    "https://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg",
                    "https://youtu.be/T7A810duHvw")

# put the movies in a list
movies = [toy_story, avatar, interstellar, dunkirk,
        amelie, about_time]

# open the webpage using fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
