import fresh_tomatoes
import media


# Creating four instances of the movie class
toy_story = media.Movie("Toy Story",
                        "Storyline about a boy and his toys who come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc");

pulp_fiction = media.Movie("Pulp Fiction",
                           "Prizefighter Butch Coolidge has decided to stop payment on a deal he's made with the devil. Honey Bunny and Pumpkin are young lovers and small time thieves who decide they need a change of venue. Meanwhile, two career criminals, Vincent Vega and Jules, go about their daily business of shooting up other crooks that are late on payments to their boss. While one is asked to baby sit their boss' dangerously pretty young wife, the other suddenly realizes that he must give up his life of crime.",
                        "http://dgeiu3fz282x5.cloudfront.net/g/l/lgpp30791+movie-one-sheet-pulp-fiction-poster.jpg",
                        "https://www.youtube.com/watch?v=s7EdQ4FqbhY");

shawshank_redemption = media.Movie("The Shawshank Redemption",
                           "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco");

big_lebowski = media.Movie("The Big Lebowski",
                           "American crime comedy film written, produced, and directed by Joel and Ethan Coen. It stars Jeff Bridges as Jeffrey \"The Dude\" Lebowski, a Los Angeles slacker and avid bowler. He is assaulted as a result of mistaken identity, after which The Dude learns that a millionaire also named Jeffrey Lebowski was the intended victim. The millionaire Lebowski's trophy wife is kidnapped, and he commissions The Dude to deliver the ransom to secure her release; but the plan goes awry when the Dude's friend Walter Sobchak (John Goodman) schemes to keep the ransom money. Julianne Moore and Steve Buscemi also star, with David Huddleston, John Turturro, Philip Seymour Hoffman, Sam Elliott, Tara Reid, David Thewlis and Flea appearing in supporting roles.",
                        "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                        "https://www.youtube.com/watch?v=cd-go0oBF4Y");

# Create a list of the 4 movie objects
movies = [toy_story, pulp_fiction, shawshank_redemption, big_lebowski]

# Call the Udacity library which takes a list of movies as an input and dynamically create the html
fresh_tomatoes.open_movies_page(movies)
