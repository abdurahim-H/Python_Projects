<p align="center">
  <img src="https://i.imgur.com/Og6ZdJv.png" alt="Project Banner" width="100%">
</p>

# Flashy Flashcard App 📇

Flashy is an interactive flashcard application designed to help you learn French vocabulary effortlessly. With its user-friendly interface and spaced repetition technique, Flashy makes language learning fun and effective.

## Features ✨

- Loads French vocabulary from a CSV file
- Displays flashcards with French words and their English translations
- Flips the flashcard automatically after a set interval
- Allows marking words as known, which removes them from the learning set
- Saves progress by storing unknown words in a separate CSV file

## Installation 💾

1. Clone the repository:
   ```
   git clone https://github.com/your-username/flashy-flashcard-app.git
   ```

2. Install the required dependencies:
   ```
   pip install tkinter pandas
   ```

3. Make sure you have the necessary data files:
   - `data/french_words.csv`: Contains the initial set of French words and their English translations.
   - `images/card_front.png` and `images/card_back.png`: Images for the front and back of the flashcard.
   - `images/wrong.png` and `images/right.png`: Images for the "unknown" and "known" buttons.

## Usage 🚀

1. Run the `flashcard_app.py` script:
   ```
   python flashcard_app.py
   ```

2. The Flashy application window will open, displaying a flashcard with a French word.

3. After a few seconds, the flashcard will automatically flip to reveal the English translation.

4. Click the ❌ button if you don't know the word, and it will be added to the list of words to learn.

5. Click the ✅ button if you know the word, and it will be removed from the list of words to learn.

6. The application will automatically load the next flashcard.

7. Your progress will be saved in the `data/words_to_learn.csv` file, so you can continue learning from where you left off.

## Contributing 🤝

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License 📄

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements 🙏

- The flashcard images used in this project are for demonstration purposes only.
- Special thanks to the creators of the Tkinter and Pandas libraries for their amazing work.

Happy learning with Flashy! 🌟