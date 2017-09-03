# Movie-Trailer-Website

This is a sample website that allows the user to view information about movies listed and watch *YouTube* trailers about them when clicked.

## Languages and Tools Used

Languages:
- `Python` (Information about the Python language can be found in this [link](https://docs.python.org/))
- `HTML` (Information about HTML, CSS can be found in this [link](http://html.com/))
- `CSS`
- `JavaScript` (Information about the JavaScript language can be found [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript))


Tools:
- Any web browser (*Google Chrome*, *Mozilla Firefox*, *Internet Explorer*, *Safari*, etc)
- A `Python` IDE (IDLE, etc)

## Directions for Viewing

1. Download the three files (`entertainment_center.py`, `fresh_tomatoes.py`, and `media.py`) into the same folder location of your computer.
2. Use a `Python` IDE to compile the `entertainment_center.py` file and allow it to open a tab in your web browser of choice.

## Directions for Editing

If you wanted to add movies to the website you would need to:
1. Open the file `entertainment_center.py` in a `Python` IDE or text editor.
2. Create a new instance of the object like this example *code* of a movie named `movieName`:

```
movieName = media.Movie(
    "Movie Title",
    "Movie description",
    "Movie poster link",
    "Movie trailer youtube link",
    "Movie duration in hours and minutes",
    "Moive release date")
```

3. You must then add the movie to the movie list movies like this example *code*:

```
movies = [kizumonogatariP1, yourName, wonderWoman, interstellar, shaw, tS3, movieName]
```

## Issues
* The files need to be in the folder inorder for the project to run without errors.

## License
`Movie-Trailer-Website` is open-source so edit it as you please.
