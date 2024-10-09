class Piece:
    def __init__(self, color, position):
        self.position = position
        self.color = color
        
    def __repr__(self):
        return f"Piece:({self.position})"