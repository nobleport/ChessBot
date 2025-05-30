from .piece import Piece

class Queen(Piece):
    piece_symbol = {
        'white' : '♛',
        'black' : '♕'
    }
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self.piece_name = 'queen'

    def get_possible_moves(self, board_state, starting_position):
        final_moves = []
        directions = [-1, +1, +8, -8, +7, +9, -7, -9]
        for direction in directions:
            current_pos = starting_position

            while True:
                next_pos = current_pos + direction
                
                # Check boundaries and wrapping
                if direction in [-1, +1] and (current_pos // 8) != (next_pos // 8):
                    break
                if direction in [+7, -9] and (current_pos % 8) == 0:
                    break
                if direction in [-7, +9] and (current_pos % 8) == 7:
                    break
                if not 0 <= next_pos < 64:
                    break
                    
                current_pos = next_pos
                current_tile = board_state[current_pos]

                if current_tile.is_occupied():
                    if current_tile.piece.color != self.color:
                        final_moves.append(current_pos)
                    break
                
                final_moves.append(current_pos)  # Add empty squares as we go
                
        return final_moves
    
    def __repr__(self):
        return f"Queen:({self.position})"