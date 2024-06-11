# Walking Trackmap

This project summarizes the story of two guys who one day realized that the walks they were doing every time they hung out were tediously repetitive. Normal people would have searched for some other form of entertainment, but two freaks saw a challenge: go through every single street in their city exhaustively. This map is the result of the challenge, we keep updating it every time we make new walks.

## Working

Clone the repo

    git clone https://github.com/abeldonate/walking-trackmap.git

Install the dependencies

    make setup

Store on `/tracks/` the `.gpx` files you want to visualize.

When running `make` a file `resultingmap.html` is generated.

## Config

You can change the colors in the file `config.colors.hex`. Other parameters as the thickness of the lines, initial zoom or initial coordinates can be changed in the `config/config.yaml` file.
