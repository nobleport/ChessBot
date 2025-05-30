from .tile import Tile
import random
from.board_util import *

class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(64)]
        self.king_pos_white = 60
        self.king_pos_black = 4
        self.turn = 'white'

    def setup_board(self):
        # white is always A1
        # in order to place a piece, I need to mark it to occupied=true,
        # and set it equal to an instance of a piece
        # right now board is only a single list with 64 tiles, what info do I need for pawns
        
        types_to_create = {'black-pawn': list(range(8,16)),
                           'black-knight': [1,6],
                           'black-bishop': [2,5],
                           'black-rook': [0,7],
                           'black-queen': [3],
                           'black-king': [4],
                           'white-pawn': list(range(48,56)),
                           'white-knight': [57,62],
                           'white-bishop': [58,61],
                           'white-rook': [56,63],
                           'white-queen': [59],
                           'white-king': [60]}
        
        for piece_type in types_to_create.keys():
            color_type = piece_type.split('-') #this is the [color, type] 
            for index in types_to_create[piece_type]:
                self.board[index].create_piece_on_tile(color_type[1], color_type[0], index)
    
    def board_to_2d(self):
        #transforms our game state (1-D array) to 2d array for GUI
        two_d_list = []
        for i in range(0,8):
            new_row = []
            for j in range(0,8):
                index_on_board = i * 8 + j
                current_tile = self.board[index_on_board]
                # print(current_tile)
                new_row.append(current_tile)
            two_d_list.append(new_row)
            # print(new_row, 'This is the new row')
        return two_d_list
    
    # def get_castle_move
    

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