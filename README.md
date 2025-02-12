# Password Generator

## Description
The **Password Generator** is a Python-based GUI application that allows users to create secure passwords with customizable options. It is built using **Tkinter** and supports the following features:

- Generate passwords with or without special characters.
- Define the desired password length (8-20 characters).
- Save generated passwords along with usernames/emails to a text file on the Desktop.
- Simple and intuitive graphical user interface (GUI).

## Features
- **Graphical Interface (Tkinter)** for ease of use.
- **Customizable Passwords**: Users can choose to include special characters.
- **Automated File Saving**: Option to save credentials to a `.txt` file on the Desktop.
- **User-Friendly Layout**: Easy input fields for website/service name, username/email, and password length.

## Requirements
- Python 3.x
- Tkinter (included with Python)
- `password_configs.py` (required for password generation logic)

## Installation & Setup
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/Howflet/Password_Generator.git
   ```
2. Ensure Python is installed on your system.
3. Place `password_configs.py` in the same directory as `password_generator.py`.

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:
   ```bash
   python password_generator.py
   ```
4. Enter the required details in the GUI and click **Generate** to create a password.
5. If the **Save as text file** option is checked, the generated password will be saved on the Desktop.

## File Structure
```
Password_Generator/
│── password_generator.py  # Main script with GUI
│── password_configs.py    # Password generation logic (must be included)
│── icon/                  # Folder containing application icon (optional)
```

## Future Improvements
- Add the ability to copy passwords to the clipboard.
- Implement additional password strength settings.
- Improve UI design with modern styling.

## Author
**Howard Fletcher**


