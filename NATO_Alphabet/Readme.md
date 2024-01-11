# :book: NATO Phonetic Alphabet Project

![Project Banner](https://i.imgur.com/gXTgEmW.jpg)

This project is a simple Python script that converts any input word into the NATO phonetic alphabet.

## :bookmark_tabs: Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## :wrench: Installation

To run this project, you need to have Python installed on your machine. You also need to install the `pandas` library. You can install it using pip:

```bash
pip install pandas
```

## :computer: Usage
The script reads from a CSV file named nato_phonetic_alphabet.csv which should be in the same directory as the script. This file should contain the NATO phonetic alphabet, with each row containing a letter and its corresponding code.

The script creates a dictionary from the CSV file, with the letters as keys and the codes as values.

When you run the script, it will prompt you to enter a word. It will then output the NATO phonetic code for each letter in the word.

Here's an example of how to run the script:

```bash
python your-script-name.py
```
And here's an example of the output:

```bash
Enter a word: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## :handshake: Contributing
Contributions are welcome! Please read the contributing guide to learn how to contribute.
```