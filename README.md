# Match 3 Game
An amateur attempt at creating a Bejeweled clone in pygame.

Started as a capstone project, currently just a hobby.

## How to run
1. Clone this repository.
```
git clone https://github.com/CocoTheMii/match3game
```
2. Install pygame.
```
cd match3game
pip install pygame
```
3. Run game.py with Python 3.
```
python game.py
```

## Implemented so far
Right now, the game is very incomplete, but some rudimentary functions are implemented.

* Generates an 8x8 grid of tiles
  * Loads a texture to make the tiles circular
  * Checks the board to prevent generating with any matches
* Allows selecting and deselecting tiles by clicking on them
* Displays an outline around selected tiles

...and that's about it.

## To do
In its current state, this is barely a playable game. There are still many things that need to be done.

* Swapping tiles
* Only allow selecting one tile at a time
* Remove matches from the board
  * This is currently done at startup, but the check is only run once and could probably use improvement
* Scoring
* Levels
* Powerups
* Determine current number of possible moves
  * Lose condition if there are no more moves
* Make it look nicer

...and probably more I forgot to list here.

## Known issues
This is a list of known issues with the code in its current state. Obviously, this doesn't include missing features (see [To do](#to-do) for that).

* Tile texture sometimes fails to load
  * Appears as a square
  * Not sure what causes this