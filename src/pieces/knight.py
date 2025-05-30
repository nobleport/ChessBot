from .piece import Piece

class Knight(Piece):
    #I am going to check if a king gets put in check by a move later when I am actually moving
    piece_symbol = {
        'white' : '♞',
        'black' : '♘'
    }
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self.piece_name = 'knight'
    
    def get_possible_moves(self, board_state, starting_position):
        moves = [
            (2, 1),   # Two right, one down
            (2, -1),  # Two right, one up
            (-2, 1),  # Two left, one down
            (-2, -1), # Two left, one up
            (1, 2),   # One right, two down
            (1, -2),  # One right, two up
            (-1, 2),  # One left, two down
            (-1, -2)  # One left, two up
        ]
        
        final_moves = []
        current_row = starting_position // 8
        current_col = starting_position % 8
        
        for x, y in moves:
            new_col = current_col + x
            new_row = current_row + y
            
            # Check if new position is on board
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                new_pos = new_row * 8 + new_col
                current_tile = board_state[new_pos]
                
                if not current_tile.is_occupied() or current_tile.piece.color != self.color:
                    final_moves.append(new_pos)
                
        return final_moves
    
    def __repr__(self):
        return f"Knight:({self.position})"