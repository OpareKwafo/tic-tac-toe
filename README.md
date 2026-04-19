# 🎮 Tic-Tac-Toe (Python | OOP Project)

A command-line Tic-Tac-Toe game built in Python using Object-Oriented Programming principles. This project demonstrates clean modular design, game state management, and basic AI logic using a random computer opponent.

---

## 👨‍💻 About the Project

This project was built as a hands-on exercise to strengthen core Python skills, particularly:

* Object-Oriented Programming (OOP)
* Multi-file project structure (modules)
* Game loop design and state management
* Input validation and error handling
* Basic AI behavior (randomized computer moves)

The game runs entirely in the terminal and follows classic Tic-Tac-Toe rules.

---

## 📂 Project Structure

```id="k8q2lp"
Tic-Tac-Toe-Project/
│
├── game.py              # Main game loop (controls flow)
├── board.py             # Board class (stores & displays state)
├── player.py            # Player class (human & computer logic)
├── check_winner.py      # Win condition logic
└── README.md
```

---

## ▶️ How to Run the Game

### 1. Clone the repository

```bash id="r9v3sd"
git clone https://github.com/<your-username>/tic-tac-toe.git
cd tic-tac-toe
```

### 2. Run the game

```bash id="v2m8ta"
python game.py
```

---

## 🎯 How to Play

* You are **X**
* The computer is **O**
* Enter a number from **1 to 9** to place your move:

```id="t5n1qp"
1 | 2 | 3
-+-+-+-
4 | 5 | 6
-+-+-+-
7 | 8 | 9
```

### 🏆 Win Condition:

Get **three of your symbols in a row**:

* Horizontally
* Vertically
* Diagonally

If all 9 spaces are filled without a winner → the game ends in a draw.

---

## ⚙️ Features

* 🎮 Turn-based gameplay (Player vs Computer)
* 🧠 Modular OOP design
* 🧾 Separate board, player, and game logic
* 🔍 Win detection across all combinations
* 🤖 Randomized computer moves
* 🛡️ Input validation to prevent overwriting moves

---

## 🚧 Future Improvements

This project can be extended with:

* 🔥 Smarter AI (Minimax algorithm)
* 🔁 Replay / restart functionality
* 🧑‍🤝‍🧑 Two-player mode (PvP)
* 🎨 GUI version using Pygame or Tkinter
* 📊 Score tracking system

---

## 🧠 What I Learned

* Designing multi-module Python applications
* Separating concerns using classes
* Managing game state across modules
* Debugging real-world logic and flow issues
* Structuring a scalable Python project

---

## 👤 Author

**Opare Kwafo**
GitHub: https://github.com/<OpareKwafo>

---

## 📜 License

This project is open-source and available under the MIT License.
