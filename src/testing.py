import numpy as np
import random
import pygame
import sys
import math



ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4

screen = pygame.display.set_mode((1366, 780))
board_img  = pygame.image.load(r"./assets/board2.png")
bg = pygame.image.load(r"./assets/bg1.jpg")


def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_board_cord(x: int, y: int) -> (int, int):
    imgx, imgy = 780, 490
    return ((x // 2) - (imgx // 2), (y // 2) - (imgy // 2))

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score posiive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else: # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def pick_best_move(board, piece):

    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col

def draw_board(row_no, col_no, turn):
    pos_x = 71 + 106 * (col_no)
    pos_y = 51 + 77 * (row_no)

    if turn == PLAYER:
        pygame.draw.circle(board_img, (125, 24, 28), (pos_x, pos_y), 37)
    if turn == AI:
        pygame.draw.circle(board_img, (40, 95, 71), (pos_x, pos_y), 37)
    pygame.display.update()

def main():
    board = create_board()
    print_board(board)
    
    game_over = False

    pygame.init()

    
    board_pos = get_board_cord(screen.get_width(), screen.get_height())
    pygame.display.update()
    columns =[]
    for i in range(6):
        columns.append((106 * i + 53))

    turn = random.randint(PLAYER, AI)

    coin_tray = pygame.Surface([1366, 74], pygame.SRCALPHA, 32)
    coin_tray.convert_alpha()

    while not game_over:

        screen.blit(bg, (0,0))
        screen.blit(coin_tray, (0, 13))
        screen.blit(board_img, board_pos)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                coin_tray.fill((0, 0, 0, 0))
                posx = event.pos[0]
                if posx < 295:
                        posx = 295
                if posx > 1072:
                        posx = 1072
                if turn == PLAYER:
                    pygame.draw.circle(coin_tray, (125, 24, 28) , (posx, 37), 37)         

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Ask for Player 1 Input
                if turn == PLAYER:
                    mouse_pos = event.pos
                    posx = mouse_pos[0]
                    if posx < 295:
                        posx = 295
                    if posx > 1072:
                        posx = 1072
                    if posx < 295 + 71 + 53:
                        print(posx - 295 - 71)
                        col = 0
                    elif posx > 1072 - (71 + 53):
                        col = 6
                    else:
                        posx = posx - 295 - 71
                        col = 0
                        prev = 0
                        for j, i in enumerate(columns):
                            if prev < posx < i:
                                col = j
                                break
                            else:
                                prev = i
                    print(f'col {col+1} was pressed')
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)
                        draw_board(5-row, col, turn)
                        print_board(board)
                        if winning_move(board, PLAYER_PIECE):
                            game_over = True
                            return PLAYER_PIECE
                        
                        turn += 1
                        turn = turn % 2

                        
                        


        # # Ask for Player 2 Input
        if turn == AI and not game_over:				
            col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                draw_board(5-row, col, turn)
                print_board(board)
                if winning_move(board, AI_PIECE):
                    game_over = True
                    return AI_PIECE
    
                turn += 1
                turn = turn % 2
                
        pygame.display.update()

        if game_over:
            pygame.time.wait(3000)

