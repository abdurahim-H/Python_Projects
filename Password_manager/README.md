
# 🔐 MyPass - Password Manager

![MyPass](https://i.imgur.com/BuDKxEw.png)

**MyPass** is a simple and secure password manager built using Python's Tkinter library. It helps users generate and store strong passwords for various websites while ensuring the credentials are kept in a file for later retrieval.

---

## 🚀 Features

- 🔑 **Password Generator**: Create random, secure passwords with a mix of letters, numbers, and symbols.
- 💾 **Save Credentials**: Store website, email, and password information securely in a local text file.
- 📋 **Clipboard Support**: Automatically copies the generated password to the clipboard for easy pasting.
- 🎨 **Simple UI**: A clean, intuitive interface built with Tkinter.

---

## 📷 Screenshots

![MyPass UI](images/screenshot.png)

---

## 🛠️ Project Structure

```bash
.
├── main.py                # The main application file with Tkinter UI and logic
├── logo.png               # Application logo
├── data.txt               # File where the saved credentials are stored
└── README.md              # Project readme (this file!)
```

---

## 🎮 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abdurahim-H/MyPass.git
   cd MyPass
   ```

2. **Install necessary dependencies**:
   Install the required libraries using the `requirements.txt` or the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Xvfb and pyperclip** (for systems without a display):
   ```bash
   sudo apt-get install xvfb
   sudo apt-get install xclip
   ```

4. **Run the application with Xvfb**:
   ```bash
   xvfb-run python main.py
   ```

5. **Using the Application**:
   - Enter the website and email.
   - Click **Generate Password** to generate a secure password.
   - Click **Add** to save the credentials.

---

## 🧩 How It Works

- **Password Generation**: The app generates passwords using a combination of random letters, numbers, and symbols.
- **Data Storage**: Credentials are saved in a `data.txt` file in a `Website | Email | Password` format.
- **Clipboard Copy**: The generated password is automatically copied to the clipboard for quick use.

---

## 🎯 Future Enhancements

- 🔒 **Encryption**: Add encryption for securely storing passwords.
- 🔍 **Search Functionality**: Allow users to search for saved credentials by website.
- 🛡️ **Password Strength Indicator**: Show password strength when generating a password.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Credits

- **Logo**: Custom-designed logo for the project.
- **UI**: Built with Tkinter

