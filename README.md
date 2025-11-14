# Polly – Your Python Calculator

**Polly** is an interactive console calculator that supports essential arithmetic operations.  
This project was created as part of my Python training and focuses on input validation, error handling, and user interaction in the console.

---

## Features

Polly can perform the following operations:

- **Addition** (`+`)
- **Subtraction** (`-`)
- **Multiplication** (`*`)
- **Division** (`/`)
- **Integer division** (`//`)
- **Modulo** (`%`)
- **Exponentiation** (`**`)

Additional functionality:

- Validates whether both inputs are numeric  
- Prevents division by **0**  
- Checks whether the chosen operator is valid  
- Allows repeating calculations in a loop  

---

## Program Logic

The program uses:

- A custom function `ist_float()` to validate and convert inputs to `float`
- A `while True` loop to allow continuous calculations
- `if/elif` statements to handle different operators
- Clear error messages and guided user prompts
