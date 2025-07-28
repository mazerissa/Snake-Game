# Snake Game with AI Player

Welcome to the Snake Game with AI! This project is a classic Snake game built using Python's Turtle graphics, enhanced with an AI that autonomously plays the game.

---

## Features

- Classic Snake gameplay using Python Turtle.
- AI-controlled snake that:
  - Seeks the food automatically.
  - Avoids collisions with walls and its own body.
  - Uses pathfinding algorithms to plan safe moves.
- Scoreboard tracks your high score.
- Modular design separating game logic and AI logic.

---

## Project Structure

├── main.py          # Main game loop, uses Turtle for rendering 
├── snake.py         # Snake class and movement logic 
├── food.py          # Food object with random spawning 
├── scoreboard.py    # Score tracking and display 
├── snake_ai.py      # AI logic to control the snake's movement 
└── README.md        # This file

---

## How to Run

1. Make sure you have Python 3 installed.

2. Clone this repository:

   `bash
   git clone https://github.com/mazerissa/snake-game.git
   cd snake-game

3. Run the game:

python main.py



The AI will automatically control the snake — no keyboard input is required.


---

How the AI Works

The AI uses a Breadth-First Search (BFS) algorithm to find the shortest safe path to the food.

If no safe path exists, it chooses moves that maximize survival by evaluating reachable open spaces.

It avoids collisions with walls and its own body.

The AI logic is encapsulated in snake_ai.py, making it easy to enhance or replace.



---

Customization

Adjust game speed by modifying the sleep time in main.py.

Modify grid size or snake speed by editing the respective variables.

Extend AI capabilities by improving pathfinding or adding machine learning.



---

Troubleshooting

If the game crashes on startup, ensure data.txt (used for storing high score) exists and contains a valid number (e.g., 0).

The AI occasionally might trap itself due to the complexity of the snake’s growing length. Future improvements are planned!



---

License

This project is open-source and free to use under the MIT License.


---

Contributing

Feel free to fork the repo and submit pull requests! Any improvements or bug fixes are welcome.


---

Contact

Created by Mazerissa.
Email: youcefelghoul@yahoo.com
GitHub: https://github.com/mazerissa


---

Enjoy watching your AI snake master the game! 🐍🤖
