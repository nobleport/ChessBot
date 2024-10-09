from .piece import Piece

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(position=position, color=color)
    
    def __repr__(self):
        return f"Rook:({self.position})"