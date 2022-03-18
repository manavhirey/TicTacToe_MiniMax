import math
import random
from zoneinfo import available_timezones 

class Player:
    def __init__(self, letter):
        #letter is X or O 
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8):')
            #checks for valid input
            #if not an integer, invalid 
            #if not an available spot, invalid
            try: 
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are successful
            except ValueError:
                print('Invalid square. Try again.')
        
        return val

class UnbeatableComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #random choice of square
        else:
            #Get Square from MiniMax Algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter 
        other_player = 'O' if player =='X' else 'X'

        #check if previous move was a winner
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1* (state.num_empty_square()+1) if other_player == max_player else -1 * (state.num_empty_square()+1)}

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} #each score should be maximised 
        else: 
            best = {'position': None, 'score': math.inf} #each score should be minimized
        
        for possible_move in state.available_moves():
            # Step 1: make a move, try that square
            state.make_move(possible_move, player)

            # Step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # Step 3: undo the move 
            state.board[possible_move] = ' '
            state.current_winner = None 
            sim_score['position'] = possible_move 

            # Step 4: update the dictionaries if necessary
            if player == max_player: #trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else:  #but minimizing the other player
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
        
        return best

