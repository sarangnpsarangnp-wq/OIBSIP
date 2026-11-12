# Random Password Generator

## Project Overview
The Random Password Generator is a Python-based command-line application that generates strong and random passwords based on user-defined preferences. Users can specify the password length and select different character types, including uppercase letters, lowercase letters, numbers, and symbols.

## Objective
The objective of this project is to develop a simple and efficient password generator that helps users create random passwords according to their security requirements.

## Technologies Used
- **Programming Language:** Python
- **Modules:** random, string
- **IDE:** Visual Studio Code

## Features
- Allows users to specify the desired password length.
- Enforces a minimum password length of 8 characters.
- Supports uppercase letters (A–Z).
- Supports lowercase letters (a–z).
- Supports numbers (0–9).
- Supports special symbols.
- Requires at least two character types.
- Validates invalid length and character selections.
- Allows users to generate multiple passwords without restarting the application.

## Project Structure

```text
Python-Task3-RandomPasswordGenerator/
│
├── password_generator.py
├── README.md
│
└── Screenshots/
    ├── password_output.png
    ├── uppercase_lowercase.png
    ├── numbers_symbols.png
    ├── invalid_length.png
    ├── invalid_character_selection.png
    └── generate_another.png
```

## Installation Requirements

Python 3 must be installed on your system.

The project uses Python's built-in modules:
- random
- string

No external libraries are required.

## How to Run the Project

1. Download or clone the project.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

```bash
python password_generator.py
```

5. Enter the desired password length.
6. Choose the character types using yes/no.
7. View the generated password.

## Sample Output

```text
================================
     RANDOM PASSWORD GENERATOR
================================

Enter password length (minimum 8): 12

Choose character types (yes/no):
Include uppercase letters? yes
Include lowercase letters? yes
Include numbers? yes
Include symbols? yes

================================
Your Generated Password: aB7@kL9#mP2!
================================

Generate another password? (yes/no): no

Thank you for using Password Generator!
```

*Note: The displayed password is an example. Actual passwords are randomly generated.*

## Input Validation
The application handles different invalid inputs:

1. **Invalid Password Length:** Rejects passwords shorter than 8 characters.
2. **Invalid Number Input:** Displays an error when the user enters non-numeric values for password length.
3. **Insufficient Character Types:** Requires at least two character types to be selected.
4. **Multiple Password Generation:** Allows users to generate another password without restarting the program.

## Project Screenshots

### 1. Generated Password
![Password Output](Screenshots/password_output.png)

### 2. Uppercase and Lowercase Selection
![Uppercase and Lowercase](Screenshots/uppercase_lowercase.png)

### 3. Numbers and Symbols Selection
![Numbers and Symbols](Screenshots/numbers_symbols.png)

### 4. Invalid Password Length
![Invalid Length](Screenshots/invalid_length.png)

### 5. Invalid Character Selection
![Invalid Character Selection](Screenshots/invalid_character_selection.png)

### 6. Generate Another Password
![Generate Another](Screenshots/generate_another.png)

## Learning Outcomes
- Understanding Python's random and string modules.
- Working with user input and conditional statements.
- Using loops and functions in Python.
- Implementing input validation and exception handling.
- Generating random passwords based on user requirements.

## Conclusion
The Random Password Generator successfully generates random passwords based on user-selected criteria. This project helped improve my understanding of Python programming, string operations, randomization, loops, functions, and input validation.

## Internship Information
- **Organization:** Oasis Infobyte
- **Track:** Python Programming
- **Task:** Task 3 – Random Password Generator
- **Level:** Beginner