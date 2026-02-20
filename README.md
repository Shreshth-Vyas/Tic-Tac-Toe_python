# Tic-Tac-Toe_python
Tic Tac Toe game by using Python
# 🎮 Python Terminal Tic-Tac-Toe

> A classic, text-based Tic-Tac-Toe game built entirely in Python. Play against a randomized computer opponent right inside your terminal!

## 🌟 Overview
This project takes the classic game of Tic-Tac-Toe and brings it to the command line. It features a complete gameplay loop, an automated computer opponent, and robust error-handling to ensure the game never crashes, even if the user makes a typo.

### 🎯 Features
* **Human vs. AI:** Play as "X" while the computer automatically calculates and places "O" in available spots.
* **Bulletproof Input Validation:** Try to type `9` or steal a spot that's already taken? The game acts as a bouncer, catching the error and politely asking for a valid move without breaking the loop.
* **Instant Win/Tie Detection:** A custom-built scanning engine checks the board for all 8 possible winning combinations (or a full board) after every single turn.
* **Modular Architecture:** The codebase is refactored away from "spaghetti code" into clean, single-purpose functions.

---

## 🧠 Technical Takeaways
Building this project reinforced several core software engineering principles:
* **State Management:** Tracking and updating the game board using Python lists.
* **Control Flow:** Utilizing `while True` loops and complex `if/elif/else` conditional logic to maintain the game loop.
* **Modular Design:** Breaking down a monolithic script into readable, reusable functions (`user_turn()`, `computer_turn()`, `check_winner()`).
* **User Experience (UX):** Writing clean terminal outputs and handling user errors gracefully.

---

## 🚀 How to Play

**Prerequisites:** You must have Python installed on your local machine.

1. **Clone the repository** or download the python file to your machine.
2. **Open your terminal** or command prompt and navigate to the project folder.
3. **Run the game** by executing the following command:
   ```bash
   python Tic-Tac-Toe_python.py
4. **Make your move!** Enter a number between 0 and 8 to place your "X". The numbers correspond to the board positions below:
  0 | 1 | 2 
 ---+---+---
  3 | 4 | 5 
 ---+---+---
  6 | 7 | 8