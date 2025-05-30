from .piece import Piece

class Rook(Piece):
    piece_symbol = {
        'white' : '♜',
        'black' : '♖'
    }
    def __init__(self, color, position):
        super().__init__(position=position, color=color)
        self.piece_name = 'rook'
        self.can_castle = True
    
    def get_possible_moves(self, board_state, starting_position):
        final_moves = []
        directions = [-1, +1, +8, -8]
        
        for direction in directions:
            current_pos = starting_position
            
            while True:
                next_pos = current_pos + direction
                
                # Check horizontal wrapping
                if direction in [-1, +1] and (current_pos // 8) != (next_pos // 8):
                    break
                    
                # Check board boundaries
                if not 0 <= next_pos < 64:
                    break
                    
                current_pos = next_pos
                current_tile = board_state[current_pos]
                
                if current_tile.is_occupied():
                    if current_tile.piece.color != self.color:
                        final_moves.append(current_pos)
                    break
                
                final_moves.append(current_pos)
                
        return final_moves

    
    def __repr__(self):
        return f"Rook:({self.position})"