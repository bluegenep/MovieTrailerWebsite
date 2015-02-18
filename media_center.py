import media
import fresh_tomatoes

inception = media.Movie("Inception","A Movie of dream within dream", \
                        "http://sourcefed.com/wp-content/uploads/2013/10/inception.jpg",\
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
batman = media.Movie("Batman","A SuperHero Movie", \
                        "http://www.arewenotentertained.com/wp-content/uploads/2014/09/The-Dark-Knight-2008.jpg",\
                        "https://www.youtube.com/watch?v=1T__uN5xmC0")
avatar = media.Movie("Avatar", "An Extratresstrail movie", \
                      "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",\
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

shawshank_redemption = media.Movie("Shawshank Redemption", "Movie about the prisioner"\
                                   ,"http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",\
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")


movies = [batman, inception, avatar, shawshank_redemption]
fresh_tomatoes.open_movies_page(movies)

