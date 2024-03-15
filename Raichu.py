#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
# This code is contributed by:  Vishal Dung (vidung) , Kavya Sri Kasarla (kkasarla), Prathyusha Reddy Thumma (pthumma)
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import random

Level = 8
Weights = {'w': 1, 'b': 1,'W':3, 'B': 3, '@': 5, '$': 5, '.': 0}
Pieces = ''


def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))


def score(board):
    infavour = 0
    against = 0
    for ch in board.replace('.',''):
        if ch in Pieces:
            infavour += Weights[ch]
        else:
            against += Weights[ch]
    return infavour - against

def final_state(board):
    if sum([c in "wW@" for c in board]) == 0 or sum([c in "bB$" for c in board]) == 0:
        return True
    return False

def successors(N, player, board, score):
    res = []
    pieces_poss = 'wW@' if player==1 else 'bB$'
    if 'b' in pieces_poss:
        board = board[::-1]
    for (index, ch) in enumerate(board):
        if ch not in pieces_poss:
            continue
        row = index//N
        column = index%N
        
        # moves of Pichu
        if ch in 'wb' and row < N-1:
            piece = ch
            head_piece = 'b' if piece=='w' else 'w'
            raichu = '@' if piece == 'w' else '$'
            newrow = row + 1
            
            if column + 1 < N and board[newrow*N + column + 1] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[newrow*N + column + 1] = raichu if newrow == N-1 else piece
                new_board[row*N+column] = '.'
                if newrow == N-1:
                    newscore += ((Weights[raichu] - Weights[piece]) if piece in Pieces else -1*((Weights[raichu] - Weights[piece])))
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if column - 1 >=0 and board[newrow*N + column - 1] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[newrow*N + column - 1] = raichu if newrow == N-1 else piece
                new_board[row*N+column] = '.'
                if newrow == N-1:
                    newscore += ((Weights[raichu] - Weights[piece]) if piece in Pieces else -1*((Weights[raichu] - Weights[piece])))
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if column + 2 < N and board[newrow*N + column + 1] in head_piece and newrow + 1 < N and board[(newrow+1)*N + column + 2] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                newscore += Weights[new_board[newrow*N + column + 1]] if piece in Pieces else -1*(Weights[new_board[newrow*N + column + 1]])
                new_board[newrow*N + column + 1] = '.'
                new_board[(newrow+1)*N + column + 2] = raichu if newrow+1 == N-1 else piece
                if newrow+1 == N-1:
                    newscore += ((Weights[raichu] - Weights[piece]) if piece in Pieces else -1*((Weights[raichu] - Weights[piece])))
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if column - 2 >=0 and board[newrow*N + column - 1] in head_piece and newrow + 1 < N and board[(newrow+1)*N + column - 2] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                newscore += Weights[new_board[newrow*N + column + 1]] if piece in Pieces else -1*(Weights[new_board[newrow*N + column + 1]])
                new_board[newrow*N + column - 1] = '.'
                new_board[(newrow+1)*N + column - 2] = raichu if newrow+1 == N-1 else piece
                if newrow+1 == N-1:
                    newscore += ((Weights[raichu] - Weights[piece]) if piece in Pieces else -1*((Weights[raichu] - Weights[piece])))
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
        
        # moves of pikachu
        elif ch in 'WB':
            piece = ch
            head_pieces = 'bB' if piece == 'W' else 'wW'
            raichu = '@' if piece == 'W' else '$'
            
            if row+1 < N and board[(row+1)*N + column] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                new_board[(row+1)*N+column] = raichu if row+1 == N-1 else piece
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if row+2 < N and board[(row+2)*N + column] == '.' and (board[(row+1)*N+column] in head_pieces or board[(row+1)*N+column] == '.'):
                new_board = list(board[:])
                newscore = score
                new_board[row*N + column] = '.'
                newscore += Weights[new_board[(row+1)*N+column]] if piece in Pieces else -1*(Weights[new_board[(row+1)*N+column]])
                new_board[(row+1)*N+column] = '.'
                new_board[(row+2)*N+column] = raichu if row+2 == N-1 else piece
                if row+2 == N-1:
                    newscore += ((Weights[raichu] - Weights[piece]) if piece in Pieces else -1*((Weights[raichu] - Weights[piece])))
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if row+3 < N and board[(row+3)*N+column] == '.':
                temp = board[(row+1)*N+column] + board[(row+2)*N+column]
                temp = temp.replace('.','')
                if len(temp) == 1 and temp in head_pieces:
                    new_board = list(board[:])
                    newscore = score
                    new_board[row*N+column] = '.'
                    newscore += Weights[new_board[(row+1)*N+column]] if piece in Pieces else -1*(Weights[new_board[(row+1)*N+column]])
                    new_board[(row+1)*N+column] = '.'
                    newscore += Weights[new_board[(row+2)*N+column]] if piece in Pieces else -1*(Weights[new_board[(row+2)*N+column]])
                    new_board[(row+2)*N+column] = '.'
                    new_board[(row+3)*N+column] = raichu if row+3 == N-1 else piece
                    if row+3 == N-1:
                        newscore += ((Weights[raichu] - Weights[piece]) if piece in Pieces else -1*((Weights[raichu] - Weights[piece])))
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))

            if column-1 >= 0 and board[row*N+column-1] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                new_board[row*N+column-1] = piece
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if column+1 < N and board[row*N+column+1] == '.':
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                new_board[row*N+column+1] = piece
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))

            if column+2 < N and board[row*N+column+2] == '.' and (board[row*N+column+1] in head_pieces or board[row*N+column+1] == '.'):
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                newscore += Weights[new_board[row*N+column+1]] if piece in Pieces else -1*(Weights[new_board[row*N+column+1]])
                new_board[row*N+column+1] = '.'
                new_board[row*N+column+2] = piece
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if column-2 >= 0 and board[row*N+column-2] == '.' and (board[row*N+column-1] in head_pieces or board[row*N+column-1] == '.'):
                new_board = list(board[:])
                newscore = score
                new_board[row*N+column] = '.'
                newscore += Weights[new_board[row*N+column-1]] if piece in Pieces else -1*(Weights[new_board[row*N+column-1]])
                new_board[row*N+column-1] = '.'
                new_board[row*N+column-2] = piece
                res_board = ''.join(new_board)
                if 'b' in pieces_poss:
                    res_board = res_board[::-1]
                res.append((newscore, res_board))
            
            if column+3 < N and board[row*N+column+3] == '.':
                temp = board[row*N+column+1] + board[row*N+column+2]
                temp = temp.replace('.','')
                if len(temp) == 1 and temp in head_pieces:
                    new_board = list(board[:])
                    newscore = score
                    new_board[row*N+column] = '.'
                    newscore += Weights[new_board[row*N+column+1]] if piece in Pieces else -1*(Weights[new_board[row*N+column+1]])
                    new_board[row*N+column+1] = '.'
                    newscore += Weights[new_board[row*N+column+2]] if piece in Pieces else -1*(Weights[new_board[row*N+column+2]])
                    new_board[row*N+column+2] = '.'
                    new_board[row*N+column+3] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
            
            if column-3 >= 0 and board[row*N+column-3] == '.':
                temp = board[row*N+column-1] + board[row*N+column-2]
                temp = temp.replace('.','')
                if len(temp) == 1 and temp in head_pieces:
                    new_board = list(board[:])
                    newscore = score
                    new_board[row*N+column] = '.'
                    newscore += Weights[new_board[row*N+column+1]] if piece in Pieces else -1*(Weights[new_board[row*N+column+1]])
                    new_board[row*N+column-1] = '.'
                    newscore += Weights[new_board[row*N+column+2]] if piece in Pieces else -1*(Weights[new_board[row*N+column+2]])
                    new_board[row*N+column-2] = '.'
                    new_board[row*N+column-3] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                    
        #moves of Raichu 
        elif ch in '@$':
            piece = ch
            head_pieces = 'bB$' if piece == '@' else 'wW@'
            
            # Right 
            trigger = 0
            trigger_pos = 0
            release = 0
            for c in range(column+1, N):
                if release > 0 or trigger > 1:
                    break
                if board[row*N+c] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[row*N+c] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[row*N+c] in head_pieces:
                    trigger+=1
                    trigger_pos = row*N+c
                else:
                    release += 1
            
            # Left 
            trigger = 0
            trigger_pos = 0
            release = 0
            for c in range(column-1, -1, -1):
                if release > 0 or trigger > 1:
                    break
                if board[row*N+c] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[row*N+c] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[row*N+c] in head_pieces:
                    trigger+=1
                    trigger_pos = row*N+c
                else:
                    release += 1

            #Down
            trigger = 0
            trigger_pos = 0
            release = 0
            for r in range(row+1, N):
                if release > 0 or trigger > 1:
                    break
                if board[r*N+column] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[r*N+column] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[r*N+column] in head_pieces:
                    trigger+=1
                    trigger_pos = r*N+column
                else:
                    release += 1
            
            #Up
            trigger = 0
            trigger_pos = 0
            release = 0
            for r in range(row-1, -1, -1):
                if release > 0 or trigger > 1:
                    break
                if board[r*N+column] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[r*N+column] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[r*N+column] in head_pieces:
                    trigger+=1
                    trigger_pos = r*N+column
                else:
                    release += 1            
            
            #Diagonal_upleft
            trigger = 0
            trigger_pos = 0
            release = 0
            for r,c in zip(range(row-1, -1, -1), range(column-1, -1, -1)):
                if release > 0 or trigger > 1:
                    break
                if board[r*N+c] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[r*N+c] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[r*N+c] in head_pieces:
                    trigger+=1
                    trigger_pos = r*N+c
                else:
                    release += 1
                    
            #Diagonal_upright
            trigger = 0
            trigger_pos = 0
            release = 0
            for r,c in zip(range(row-1, -1, -1), range(column+1, N)):
                if release > 0 or trigger > 1:
                    break
                if board[r*N+c] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[r*N+c] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[r*N+c] in head_pieces:
                    trigger+=1
                    trigger_pos = r*N+c
                else:
                    release += 1
            
            #Diagonal_downleft
            trigger = 0
            trigger_pos = 0
            release = 0
            for r,c in zip(range(row+1, N), range(column-1, -1, -1)):
                if release > 0 or trigger > 1:
                    break
                if board[r*N+c] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[r*N+c] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[r*N+c] in head_pieces:
                    trigger+=1
                    trigger_pos = r*N+c
                else:
                    release += 1
            
            #Diagonal_downright
            trigger = 0
            trigger_pos = 0
            release = 0
            for r,c in zip(range(row+1, N), range(column+1, N)):
                if release > 0 or trigger > 1:
                    break
                if board[r*N+c] == '.':
                    new_board = list(board[:])
                    newscore = score
                    if trigger == 1:
                        newscore += Weights[board[trigger_pos]] if piece in Pieces else -1*(Weights[board[trigger_pos]])
                        new_board[trigger_pos] = '.'
                    new_board[row*N+column] = '.'
                    new_board[r*N+c] = piece
                    res_board = ''.join(new_board)
                    if 'b' in pieces_poss:
                        res_board = res_board[::-1]
                    res.append((newscore, res_board))
                elif board[r*N+c] in head_pieces:
                    trigger+=1
                    trigger_pos = r*N+c
                else:
                    release += 1
    return random.sample(res, len(res))

def minmax(N, player, board, score, alpha, beta, level):
    if level == 0 or final_state(board):
        return (board, score)
    if player=='w':
        (maximum_state, maximum_score) = (None, float('-inf'))
   
        res = sorted(successors(N, player, board, score), key= lambda x: -x[0])
        if len(res) > 0:
            filter_childs = []
            maximum = res[0][0]
            for (score,_) in res:
                if score >= maximum//2 or (maximum < 0 and score <= maximum//2):
                    filter_childs.append((score,_))
            res = filter_childs
    
        for (temp_score, child) in res:
            (_, score) = minmax(N, 'b', child, temp_score, alpha, beta, level-1)
            if score > maximum_score:
                (maximum_state, maximum_score) = (child, score)
            if maximum_score >= beta:
                 break
            if maximum_score > alpha:
                 alpha = maximum_score
        return (maximum_state, maximum_score)
    
    else:
        (minimum_state, minimum_score) = (None, float('inf'))

        res = sorted(successors(N, player, board, score), key= lambda x: x[0])
        if len(res) > 0:
            filter_childs = []
            minimum = res[0][0]
            for (score,_) in res:
                if score <= minimum//2 or (minimum > 0 and score >= minimum//2):
                       filter_childs.append((score,_))
            res = filter_childs

        for (temp_score, child) in res:
            (_, score) = minmax(N, 'w', child, temp_score, alpha, beta, level-1)
            if score < minimum_score:
                (minimum_state, minimum_score) = (child, score)
            if minimum_score <= alpha:
                 break
            if minimum_score < beta:
                 beta = minimum_score
        return (minimum_state, minimum_score)

    
def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
   # while True:
    #    time.sleep(1)
     #   yield board
    level = 2
    initial_score = score(board)
    prev_time = 0
    while timelimit > 0:
        if timelimit < prev_time:
            break
        start = time.time()
        board_temp = board[:]
        (minimum_state, _) = minmax(N, 'w', board_temp, initial_score, float('-inf'), float('inf'),level)
        level += 2
        yield minimum_state
        prev_time = time.time()-start
        timelimit -= (prev_time)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, opposite_player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    
    if opposite_player not in "wb":
        raise Exception("Invalid player.")
        
    player = 1 if opposite_player == 'w' else 0
    Pieces = 'wW@' if opposite_player == 'w' else 'bB$'

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + opposite_player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)


