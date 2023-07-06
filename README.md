# Snake-Game
Snake Game

This is a classic Snake game implemented using Python and the Turtle module. The objective of the game is to control the snake on the screen and help it eat food to grow longer. As the snake eats the food, the player earns points. However, the game ends if the snake collides with the wall or its own tail.

The game consists of the following files:

1. `main.py`: This is the main script file that sets up the game window, creates the snake, food, and scoreboard objects, and handles the game logic. It uses the Turtle module for graphics and screen management.

2. `snake.py`: This file defines the `Snake` class, which represents the snake in the game. The snake is made up of segments, and the class provides methods to move the snake, detect collisions, and handle the snake's behavior.

3. `food.py`: This file defines the `Food` class, which represents the food that the snake needs to eat. The food appears at random positions on the screen, and when the snake collides with it, the snake grows longer, and the player earns points.

4. `scoreboard.py`: This file defines the `Scoreboard` class, which keeps track of the player's score and high score. The scoreboard is displayed at the top of the game window, and it updates whenever the player earns points or resets the game.

5. `data.txt`: This file stores the high score of the game. It is read and updated by the `Scoreboard` class.

To play the game, run the `main.py` script. The snake can be controlled using the arrow keys (Up, Down, Left, Right).

Enjoy playing the Snake Game and try to beat your high score!
