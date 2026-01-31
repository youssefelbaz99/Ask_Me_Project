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


## Project Structure

AskMeApp/
│
├── src/
│   ├── askme/              # Source Code
│   │   ├── main.py         # Entry point (Application Logic)
│   │   ├── managers.py     # Data Managers (Logic Layer)
│   │   ├── models.py       # Data Classes (User, Question)
│   │   └── utils.py        # Helper functions (File I/O, Inputs)
│   │
│   └── data/               # Database Files
│       ├── users.txt       # Stores user data
│       └── questions.txt   # Stores questions and threads
│
└── README.md

## How to Run
1. Navigate to the project root directory.
2. Run the following command:
   ```bash
   python -m src.askme.main