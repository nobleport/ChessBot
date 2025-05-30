from .piece import Piece

class Pawn(Piece):
    piece_symbol = {
        'white' : '♟',
        'black' : '♙'
    }
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
        self.piece_name = 'pawn'
        self.has_moved = False

    def get_possible_moves(self, board_state, starting_position):
        print(f"Calculating moves for pawn at position {starting_position}")  # Debug
        possible_moves = []
        direction = -8 if self.color == 'white' else 8
        print(f"Moving in direction: {direction}")  # Debug

        new_pos = starting_position + direction
        print(f"Checking forward move to {new_pos}")  # Debug
        
        if 0 <= new_pos < 64 and not board_state[new_pos].is_occupied():
            print(f"Adding forward move to {new_pos}")  # Debug
            possible_moves.append(new_pos)
            
            if not self.has_moved:
                two_squares_pos = starting_position + (direction * 2)
                print(f"First move - checking two square move to {two_squares_pos}")  # Debug
                if 0 <= two_squares_pos < 64 and not board_state[two_squares_pos].is_occupied():
                    print(f"Adding two square move to {two_squares_pos}")  # Debug
                    possible_moves.append(two_squares_pos)
        
        # Check captures
        on_left_edge = starting_position % 8 == 0
        on_right_edge = starting_position % 8 == 7
        print(f"On edges: left={on_left_edge}, right={on_right_edge}")  # Debug

        if not on_left_edge:
            left_capture = starting_position + direction - 1
            print(f"Checking left capture at {left_capture}")  # Debug
            if 0 <= left_capture < 64:
                if (board_state[left_capture].is_occupied() and 
                    board_state[left_capture].piece.color != self.color):
                    print(f"Adding left capture at {left_capture}")  # Debug
                    possible_moves.append(left_capture)
        
        if not on_right_edge:
            right_capture = starting_position + direction + 1
            print(f"Checking right capture at {right_capture}")  # Debug
            if 0 <= right_capture < 64:
                if (board_state[right_capture].is_occupied() and 
                    board_state[right_capture].piece.color != self.color):
                    print(f"Adding right capture at {right_capture}")  # Debug
                    possible_moves.append(right_capture)
        
        print(f"Final possible moves: {possible_moves}")  # Debug
        return possible_moves

    def __repr__(self):
        return f"Pawn:({self.position})"