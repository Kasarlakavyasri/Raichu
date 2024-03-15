**Aim**
* Raichu.py aims to enhance Raichu's gameplay performance.

**Review**
* The objective involves modifying the game to improve the performance of the given character, Raichu. To achieve this, we opt for the optimized approach: **MIN-MAX with Alpha-Beta Pruning.**

***Decision Design and Approach***

**Algorithm Used**
Min-Max with Alpha-Beta Pruning
**
**Min-Max Alpha-Beta Pruning
* Enhances search speed by exploring deeper levels (rows and columns) in a game tree.
* Alpha: The best value that the maximizer guarantees at or above the current level.
* Beta: The best value that the minimizer guarantees at or above the current level.
  
**State Space**
Boards utilized in the game.

**Initial Space**
Inputs.

**Goal State**
* The optimized move, within the board moves, should lead back to the initial input space.

**Working**
* Assign weights to the moves and convert the board into a string, representing a two-dimensional matrix.
* Create a successor function to generate possible moves and perform pruning on these successor states to determine the maximum.
* Define execution by creating find_best_move to optimize move selection for players: Pichu, Pikachu, and Raichu.

**REFERENCES:**
* https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
* https://www.javatpoint.com/ai-alpha-beta-pruning
  
