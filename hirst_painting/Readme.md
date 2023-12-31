# Hirst Painting Generator 🎨

![Hirst Painting](https://media.cnn.com/api/v1/images/stellar/prod/200430102527-01-damien-hirst-severed-spots.jpg?q=x_2,y_580,h_898,w_1596,c_crop/w_800)

Generate your own Damien Hirst-inspired spot paintings with this Python script! 

## How it works 🛠️

The script creates a grid of points. For each point, it selects a random color from a predefined list and draws a dot at that point.

![Diagram](https://i.imgur.com/YfUcUqh.png)

The colors are selected using the `random.choices` function, which allows for the same color to be chosen more than once. This means that the painting can have a varied and interesting mix of colors.

## Usage 🚀

To run the script, simply execute it with Python:

```bash
python hirst_painting.py

The painting will be displayed in a new window. You can close the window by clicking on it.

Requirements 📋
Python 3 Turtle

This script requires Python 3 and the Turtle graphics library.

Example 🖼️
Here's an example of a painting generated by the script:
```
Example Painting
![Example Painting](https://i.imgur.com/ruWENKH.png)


