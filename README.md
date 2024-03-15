The aim of part 1: (Raichu.py) is to make raichu play well

REVIEW :
Involves in modifying the game such that the given tag(Raichu) plays well To get this we expect the optimized approach is: MIN-MAX APLHA BETA PRUNING

DECISION DESIGN AND APPROACH:
The algorithm used: Min-Max alpha-beta pruning

MIN-MAX ALPHA BETA PRUNING:
				>search faster with given into deeper levels(rows and columns)in a game tree.
				> Alpha- best value that the maximizer guarantees level above
				> Beta- best value that the minimizerguaranteelevel above

STATE SPACE:
		> Boards used in the game
INITIAL SPACE: 	
		> Inputs 
GOAL STATE:
		> In the board moves the optimized move should reach the initial input space.
WORKING:
	> Here, first we assign weights to the moves and convert the board to the string which is a two-dimensional matrix.
	> Create a successor function and run pruning on the given successor states to find the max
	> We define the execution by creating find_best_move in which we optimize to find the move for players  ie., pichu, pikachu, and raichu
REFERENCES:
>>> https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
>>> https://www.javatpoint.com/ai-alpha-beta-pruning
>>> https://github.com/afontana1/Computer-Sciences/blob/2e2bded1189462a9857ca1807d790f346cd82f61/Algorithms%20%26%20Data%20Structures/search_sort/mini_max.py
