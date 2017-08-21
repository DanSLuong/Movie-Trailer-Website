import media
import fresh_tomatoes


kizumonogatariP1 = media.Movie(
    "Kizumonogatari Part 1",
    "Follows Araragi's encounter with the vampire Kiss-shot Acerola-orion "
    "Heart-under-blade and his journey back into humanity from being a "
    "vampire.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZmJkN2Q4ZmQtOWY0Z"
    "C00MjNmLWFiN2ItY2NiNjYxMGQxZWRhXkEyXkFqcGdeQXVyMjE5MjQ4Nzk@._V1_SY1000"
    "_CR0,0,708,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=LYPJoA9udJo")

yourName = media.Movie(
    "Your Name",
    "Two strangers find themselves linked in a bizarre way. When a connection "
    "forms, will distance be the only thing to keep them apart?",
    "http://www.kulturbunkeren.dk/wp-content/uploads/2017/05/YourName.jpg",
    "https://www.youtube.com/watch?v=hRfHcp2GjVI")

wonderWoman = media.Movie(
    "Wonder Woman",
    "Before she was Wonder Woman, she was Diana, princess of the Amazons, "
    "trained warrior. When a pilot crashes and tells of conflict in the "
    "outside world, she leaves home to fight a war, discovering her full "
    "powers and true destiny.",
    "https://i0.wp.com/www.pissedoffgeek.com/wordpress/wp-content/uploads/"
    "2017/03/wonder-woman.jpg?fit=1000%2C1482",
    "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to "
    "ensure humanity's survival.",
    "http://vignette2.wikia.nocookie.net/interstellarfilm/images/3/30/Imax-pos"
    "ter-for-interstellar.jpeg/revision/latest?cb=20141003183300",
    "https://www.youtube.com/watch?v=Rt2LHkSwdPQ")

shaw = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and eventu"
    "al redemption through acts of common decency.",
    "http://cdn3.gbtimes.com/cdn/farfuture/Mi_FbKUe9PiQ9YB26WYTS-RSe9vUEfGBxUe"
    "h0rRYXKk/mtime:1417532777/sites/default/files/styles/1280_wide/public/201"
    "4/12/02/the-shawshank-redemption.jpg?itok=1RpNyipr",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

tS3 = media.Movie(
    "Toy Story 3",
    "A Story of a boy and his toys that come to life",
    "http://www.nakedmovieviews.com/wp-content/uploads/2015/12/14317452030_e88"
    "31034eb_o.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg")

movies = [kizumonogatariP1, yourName, wonderWoman, interstellar, shaw, tS3]

fresh_tomatoes.open_movies_page(movies)