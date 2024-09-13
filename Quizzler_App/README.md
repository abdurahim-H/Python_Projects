
# 🧠 Quizzler - The Ultimate Trivia Quiz App

![Quizzler](https://i.imgur.com/vOhiWG0.png)

**Quizzler** is a trivia quiz app built with Python and Tkinter. It uses the Open Trivia Database (OpenTDB) to dynamically fetch trivia questions and allows users to test their knowledge with a fun, interactive quiz interface. Are you ready to challenge your brain?

## 🚀 Features

- **Random Trivia Questions**: Pulls random trivia questions from OpenTDB using an API.
- **True/False Quiz**: Answer questions using simple True or False buttons.
- **Score Tracking**: Keeps track of your score as you progress through the quiz.
- **Dynamic Question Loading**: Loads a new question automatically after each answer.
- **Simple UI**: Clean and intuitive design using the Tkinter library.

## 🎮 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abdurahim-H/Python_Projects.git
   cd Python_Projects
   ```

2. **Install necessary dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Play the Quiz**:
   - Answer each question by clicking on the True or False buttons.
   - Your score will be updated automatically after each question.

## 🧩 How It Works

- **Fetching Questions**: The app pulls 10 random trivia questions from OpenTDB in boolean format (True/False).
- **Interactive Quiz**: Displays questions on a canvas, and users respond by clicking buttons.
- **Real-time Feedback**: The interface changes color based on whether your answer is correct or incorrect.

## 🎯 Future Enhancements

- **Category Selection**: Let users choose different trivia categories like Science, Sports, etc.
- **Multiple Question Types**: Add support for multiple-choice questions.
- **Leaderboard**: Store and display high scores for added competition.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Credits

- **API**: [Open Trivia Database (OpenTDB)](https://opentdb.com/)
- **UI**: Built with Tkinter
