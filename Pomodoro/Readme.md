# 🍅 Pomodoro Timer

![Pomodoro Timer](https://i.imgur.com/2rzYbJk.png)

This is a simple and efficient Pomodoro Timer built with Python and the Tkinter library. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## ⭐ Features

- Customizable work and break durations
- Visual and audio notifications to start work or take a break
- Reset functionality to stop and reset the timer
- Counts the number of work sessions completed

## 🚀 How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Run `python main.py` to start the application.

## 🎨 Application Interface

The application interface is simple and intuitive. It consists of a timer display, a label indicating the current mode (work or break), and three buttons to start work, start a break, or reset the timer.

![Application Interface](https://i.imgur.com/RQxrkdG.png)

## 📚 Code Overview

The code is organized into several functions, each responsible for a specific part of the application's functionality.

- `start_work_time`: Starts the work timer.
- `start_break_time`: Starts the break timer.
- `count_down`: Handles the countdown functionality.
- `reset`: Resets the timer and the application state.

## 🔧 Customization

You can customize the duration of the work and break periods by modifying the `WORK_MIN` and `SHORT_BREAK_MIN` constants at the top of the `main.py` file.

## 🔔 Audio Notifications

The application uses custom audio notifications to signal the end of a work period or a break. You can replace these with your own audio files by modifying the `os.system` calls in the `count_down` function.

## 📦 Dependencies

- Python 3
- Tkinter
- math
- os

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
