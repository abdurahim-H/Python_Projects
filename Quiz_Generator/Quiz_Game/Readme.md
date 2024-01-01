# Quiz Application 💻

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Quiz](https://img.shields.io/badge/-Quiz-FFA500?style=flat-square)

Welcome to our Quiz Application! This Python-based application offers a fun and interactive way to test your knowledge on various topics.

## 🎯 Overview

The application is built around three main components:

- **Question**: A class that encapsulates a single question. It holds two properties: text (the question text) and answer (the correct answer).
- **QuizBrain**: The engine of the quiz. It manages the list of questions, the current question number, and the user's score. It provides methods to check if there are more questions, to present the next question, and to verify the user's answer.
- **main.py**: The entry point of the application. It creates a list of Question objects from the predefined data, initializes a QuizBrain object with this list, and then kick-starts the quiz.

## 🚀 Getting Started

To dive into the quiz, simply execute the `main.py` script. You will be prompted with a series of true/false questions. Input your answer (either "true" or "false") for each question. Your final score will be displayed at the end.

## 📚 Data

The quiz data is stored in the `question_data` list. Each item in the list is a dictionary with the following keys:

| Key | Description |
| --- | --- |
| type | The type of the question (always "boolean" in this case). |
| difficulty | The difficulty level of the question ("easy" in this case). |
| category | The category of the question. |
| question | The question text. |
| correct_answer | The correct answer ("True" or "False"). |
| incorrect_answers | A list of incorrect answers. |

Feel free to modify this list to customize your quiz with different questions.

## 🎲 Example Run

Here's a sneak peek of how the quiz unfolds:

Q.1: The programming language "Python" is based off a modified version of "JavaScript". True or False: false That is correct Your current score is 1 / 1

Q.2: The Windows ME operating system was released in the year 2000. True or False: true That is correct Your current score is 2 / 2

...

The end of the quiz has been reached; your score is 8 out of 10


Enjoy the quiz and happy learning! 🎉