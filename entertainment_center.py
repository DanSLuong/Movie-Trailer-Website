import media
import fresh_tomatoes

# Create Object of each movie
''' Kizumonogatari movie: movie title, storyline, poster image, movie trailer,
    movie duration, and release date'''
kizumonogatariP1 = media.Movie(
    "Kizumonogatari Part 1",
    "The first part in a three part movie about Araragi's encounter with "
    "the vampire Kiss-shot Acerola-orion Heart-under-blade and his journey "
    "back into humanity from being a vampire.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZmJkN2Q4ZmQtOWY0Z"
    "C00MjNmLWFiN2ItY2NiNjYxMGQxZWRhXkEyXkFqcGdeQXVyMjE5MjQ4Nzk@._V1_SY1000"
    "_CR0,0,708,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=LYPJoA9udJo",
    "1hr 4mins",
    "Janurary 8, 2016")

''' Your Name movie: movie title, storyline, poster image, movie trailer,
    movie duration, and release date'''
yourName = media.Movie(
    "Your Name",
    "Two strangers find themselves linked in a bizarre way. When a connection "
    "forms, will distance be the only thing to keep them apart?",
    "http://www.kulturbunkeren.dk/wp-content/uploads/2017/05/YourName.jpg",
    "https://www.youtube.com/watch?v=hRfHcp2GjVI",
    "1hr 46mins",
    "April 7, 2017")

''' Wonder Woman movie: movie title, storyline, poster image, movie trailer,
    movie duration, and release date'''
wonderWoman = media.Movie(
    "Wonder Woman",
    "Before she was Wonder Woman, she was Diana, princess of the Amazons, "
    "trained warrior. When a pilot crashes and tells of conflict in the "
    "outside world, she leaves home to fight a war, discovering her full "
    "powers and true destiny.",
    "https://i0.wp.com/www.pissedoffgeek.com/wordpress/wp-content/uploads/"
    "2017/03/wonder-woman.jpg?fit=1000%2C1482",
    "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
    "2hrs 22mins",
    "June 2, 2017")

''' Interstellar movie: movie title, storyline, poster image, movie trailer,
    movie duration, and release date'''
interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to "
    "ensure humanity's survival.",
    "http://vignette2.wikia.nocookie.net/interstellarfilm/images/3/30/Imax-pos"
    "ter-for-interstellar.jpeg/revision/latest?cb=20141003183300",
    "https://www.youtube.com/watch?v=Rt2LHkSwdPQ",
    "2hrs 49mins",
    "November 7, 2014")

''' The Shaw Shank Redemption movie: movie title, storyline, poster image,
    movie trailer, movie duration, and release date'''
shaw = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and eventu"
    "al redemption through acts of common decency.",
    "http://cdn3.gbtimes.com/cdn/farfuture/Mi_FbKUe9PiQ9YB26WYTS-RSe9vUEfGBxUe"
    "h0rRYXKk/mtime:1417532777/sites/default/files/styles/1280_wide/public/201"
    "4/12/02/the-shawshank-redemption.jpg?itok=1RpNyipr",
    "https://www.youtube.com/watch?v=6hB3S9bIaco",
    "2hrs 22mins",
    "October 14, 1994")

''' Toy Story 3 movie: movie title, storyline, poster image, movie trailer,
    movie duration, and release date'''
tS3 = media.Movie(
    "Toy Story 3",
    "Part three of a story of a boy and his toys that come to life",
    "http://www.nakedmovieviews.com/wp-content/uploads/2015/12/14317452030_e88"
    "31034eb_o.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg",
    "1hr 43mins",
    "June 18, 2010")

# Create a list with the movies that will be used by the media.py file
movies = [kizumonogatariP1, yourName, wonderWoman, interstellar, shaw, tS3]

# Opens the HTML file in a webbrowser using the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
