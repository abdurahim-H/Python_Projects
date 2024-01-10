<p align="center">
    <h3 align="center">U.S. States Game</h3>
    <p align="center">
        An interactive and fun way to learn all 50 U.S. states!
    </p>
</p>

![Screenshot](https://i.imgur.com/aXOAwSu.png)

## Table of Contents

* [About the Game](#about-the-game)
	* [Built With](#built-with)
* [Getting Started](#getting-started)
	* [Prerequisites](#prerequisites)
	* [Installation](#installation)
* [Usage](#usage)
* [Contact](#contact)

## About The Game

This project is a fun and interactive game to help you learn and remember the names of all 50 states in the United States.

### Built With

* [Python](https://www.python.org/)
* [Turtle](https://docs.python.org/3/library/turtle.html)
* [Pandas](https://pandas.pydata.org/)


### Prerequisites

This is a list of things you need to use the software and how to install them.

* Python
* Turtle
* Pandas

```bash
pip install turtle pandas
```

## :video_game: How to Play

When you run the game, you'll see a blank map of the United States. Your task is to enter the name of a state. If the state is correct, the state's name will appear at its correct location on the map. The game continues until you've correctly identified all 50 states.

## :star2: Features

- **Interactive Gameplay**: This game isn't just about memorization. It's about learning and having fun at the same time. You'll interact with the game using your keyboard to enter your answers.

- **Progress Tracking**: The game keeps track of how many states you've correctly identified. You'll see your progress in the title bar of the game window.

- **Learning Aid**: If you decide to exit the game before guessing all 50 states, the game will generate a CSV file named "states_to_learn.csv". This file will contain the names of the states you have yet to guess. You can use this as a study aid.

## :mag: Code Overview

The game uses the `turtle` library to create the game window and display the states on the map. The `pandas` library is used to read the CSV file that contains the names and coordinates of all the states.

When you guess a state correctly, a new turtle is created and moved to the correct coordinates on the map. The turtle then writes the name of the state at that location.

## :rocket: How to Run

To run the game, you need Python installed on your machine. You also need the `turtle` and `pandas` libraries, which you can install using pip:

```bash
pip install turtle pandas

```

Once you have Python and the necessary libraries installed, you can run the game using Python:

```bash
python main.py

```

Enjoy the game and happy learning! :tada:

```