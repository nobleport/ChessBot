from .piece import Piece

class Bishop(Piece):
    piece_symbol = {
        'white' : '♝',
        'black' : '♗'
    }

    def __init__(self, color, position):
        super().__init__(color=color, position=position)
    
    def __repr__(self):
        return f"Bishop:({self.position})"