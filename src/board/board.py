from .tile import Tile
import random
from.board_util import *

class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(64)]

    def setup_board(self):
        # white is always A1
        # in order to place a piece, I need to mark it to occupied=true,
        # and set it equal to an instance of a piece
        # right now board is only a single list with 64 tiles, what info do I need for pawns
        
        types_to_create = {'white-pawn': list(range(8,15)),
                           'white-knight': [1,6],
                           'white-bishop': [2,5],
                           'white-rook': [0,7],
                           'white-queen': [3],
                           'white-king': [4],
                           'black-pawn': list(range(48,55)),
                           'black-knight': [57,62],
                           'black-bishop': [58,62],
                           'black-rook': [56,63],
                           'black-queen': [59],
                           'black-king': [60]}
        
        for piece_type in types_to_create.keys():
            color_type = piece_type.split('-') #this is the [color, type] 
            for index in types_to_create[piece_type]:
                self.board[index].create_piece_on_tile(color_type[1], color_type[0], index)
                # print("hello maryn")
                #i've created the piece and attached it to the tile at that location
    
            
    def __repr__(self):
        return_list = []
        for tile in self.board:
            # return_list.append(f'Tile:(occupied:{tile.is_occupied()} piece:{tile.piece})')
            if tile.is_occupied():
                color = tile.piece.color
                return_list.append(tile.piece.piece_symbol[color])
            else:
                return_list.append(' ')
        return f"Board:({return_list})"