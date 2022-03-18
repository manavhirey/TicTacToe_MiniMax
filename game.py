from ntpath import realpath
import time
from player import HumanPlayer, RandomComputerPlayer, UnbeatableComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' 'for _ in range(9)] #single list to represent 3x3 board
        self.current_winner = None #keeping track of winner

    def print_board(self):
        #for getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + ' |'.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+' |' .join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # for (i,spot) in enumerate(self.board):
        #     #['x' , 'x' , 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        #     return moves
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        #if move valid, then make move and return true
        #else return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter): 
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 anywhere
        #check row first
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #only if square is an even number (0,2,4,6,8)
        #these are the only possible moves to win for a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for  i in [0,4,8]] #left or right diagonals
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonals
            if all ([spot == letter for spot in diagonal2]):
                return True

        #if all of them fail
        return False

def play(game, x_player, o_player, print_game = True):
    #Returns winner of the game (return letter) or None for a tie 
    if print_game:
        game.print_board_nums()
    #itrate while empty squares are present
    letter = 'X' #starting Letter
    
    while game.empty_squares():
        if letter == 'O':
           square = o_player.get_move(game)
        else:
            square = x_player.get_move(game) 
    
    #function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('')

            #Check for winner 
            if game.current_winner:
                if print_game:
                    print (letter + ' wins!')
                return letter

            #Player Switch 
            letter = 'O' if letter =='X' else 'X'
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        if print_game:
            time.sleep(0.8)
        
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(0,1):
        x_player = RandomComputerPlayer('X') #player 1
        o_player = UnbeatableComputerPlayer('O') #player 2 
        t = TicTacToe()
        result = play(t,x_player,o_player,print_game=True) #if show game then change print_game = True
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        elif result == None:
            ties += 1
        
    # print(f'After 1000 iterations, X wins, {x_wins}, O wins {o_wins} and ties {ties} ')