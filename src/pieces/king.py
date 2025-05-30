from .piece import Piece

class King(Piece):
    piece_symbol = {
        'white' : '♚',
        'black' : '♔'
    }
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self.piece_name = 'king'
        self.can_castle = True

    def king_in_check(self, board_state):
        for idx, tile in enumerate(board_state):
            if tile.is_occupied() and tile.piece.color != self.color:
                current_piece = tile.piece
                current_piece.position = idx
                current_possible_moves = current_piece.get_possible_moves(board_state, idx)
                if self.position in current_possible_moves:
                    return True
        return False

    def get_possible_moves(self, board_state, starting_position):
        final_moves = []
        directions = [-1, +1, +8, -8, +7, -7, +9, -9]
        
        for direction in directions:
            next_pos = starting_position + direction
            
            if not 0 <= next_pos < 64:
                continue
            
            if direction in [-1, +1] and (starting_position // 8) != (next_pos // 8):
                continue
            
            if direction in [+7, -9] and (starting_position % 8) == 0:  # Left edge
                continue
            if direction in [+9, -7] and (starting_position % 8) == 7:  # Right edge
                continue
            
            current_tile = board_state[next_pos]
            if not current_tile.is_occupied() or current_tile.piece.color != self.color:
                final_moves.append(next_pos)
            
        return final_moves

    def __repr__(self):
        return f"King:({self.position})"