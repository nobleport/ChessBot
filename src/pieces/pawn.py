from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color=color, position=position)
    
    def __repr__(self):
        return f"Pawn:({self.position})"