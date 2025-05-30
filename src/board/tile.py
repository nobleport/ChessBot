from src.pieces.bishop import Bishop
from src.pieces.pawn import Pawn
from src.pieces.knight import Knight
from src.pieces.rook import Rook
from src.pieces.queen import Queen
from src.pieces.king import King

class Tile:
    def __init__(self, occupied=False, piece=None):
        self.occupied = occupied
        self.piece = piece
    
    def is_occupied(self):
        return self.occupied

    def create_piece_on_tile(self, piece_type, color, position):
        piece_classes = {'pawn': Pawn,
                      'bishop': Bishop,
                      'knight': Knight,
                      'rook': Rook,
                      'queen': Queen,
                      'king': King}
        if piece_type.lower() in piece_classes:
            new_piece = piece_classes[piece_type.lower()](color, position)
        else:
            raise Exception('invalid piece type')
        self.piece = new_piece
        self.occupied = True
    
    def tile_to_piece_symbol(self):
        if self.is_occupied():
            color = self.piece.color
            return self.piece.piece_symbol[color]
        else:
            return ' '

    def __repr__(self):
        return f'Tile(occupied:{self.occupied} piece:{self.piece})'
    
