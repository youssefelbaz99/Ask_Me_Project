# AskMe App

A Python command-line application designed to simulate an anonymous asking platform (similar to Sarahah or Ask.fm). The project demonstrates file handling, OOP principles, and data management without an external database.

## Project Structure
- **src/askme**: Contains the source code (models, managers, utils, main).
- **src/data**: Stores persistent data (users.txt, questions.txt).

## Features
- **User System**: Sign up, Login (with password hiding), and Logout.
- **Questions**: Ask questions anonymously or publicly.
- **Threading**: Reply to questions (Threaded conversations).
- **Feed**: List all answered questions in the system.
- **File Database**: Custom flat-file database using `|` as a delimiter.

## How to Run
1. Navigate to the project root directory.
2. Run the following command:
   ```bash
   python -m src.askme.main
   
https://github.com/user-attachments/assets/99e0a214-334c-4b04-a32c-40fd590aa76b
