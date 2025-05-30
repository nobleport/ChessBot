from src.board.board import Board
from src.game.game_util import letter_to_idx
from src.game.game_util import *
from src.game.game import Game
import math
from copy import deepcopy

class GameController():
    def __init__(self, window, board):
        self.window = window
        self.board = board
        self.selected_square = None
        self.game = Game(window, 50, 50, 100, 100, board)
        self.game.draw_board()

    def handle_click_flow(self, square_coord):
        if self.selected_square is None:
            tile_idx = self.convert_coord_to_idx(square_coord)
            tile = self.board.board[tile_idx]
            
            if tile.is_occupied() and tile.piece.color == self.board.turn:
                self.selected_square = square_coord
            return
        
        from_idx = self.convert_coord_to_idx(self.selected_square)
        to_idx = self.convert_coord_to_idx(square_coord)

        if self.is_valid_move(from_idx, to_idx):
            self.make_move(from_idx, to_idx)
            self.window.move_piece(
                self.window.squares[self.selected_square],
                self.window.squares[square_coord]
            )
            self.board.turn = 'black' if self.board.turn == 'white' else 'white'
        
        prev_selected = self.selected_square
        self.selected_square = None
        
        if square_coord != prev_selected:
            self.handle_click_flow(square_coord)

    def handle_square_click(self, x, y):
        numeric_coordinate_tuple = self.convert_pixels_to_coordinates(x, y)
        chess_coordinates = self.numeric_to_chess_coordinates(numeric_coordinate_tuple)
        self.handle_click_flow(chess_coordinates)
    
    def convert_coord_to_idx(self, square_coord):
        letter, number = square_coord.split('-')
        number = int(number)
        letter_idx = letter_to_idx[letter]
        coord = (8 - number) * 8 + letter_idx
        return coord
       
    def convert_pixels_to_coordinates(self, x, y):
        subtract_border_x = x - self.game.x1
        subtract_border_y = y - self.game.y1
        
        idx_quotient_i = subtract_border_y / self.game.square_size_y
        idx_quotient_j = subtract_border_x / self.game.square_size_x
        
        idx_i = math.floor(idx_quotient_i)
        idx_j = math.floor(idx_quotient_j)
        
        return (idx_i, idx_j)

    def numeric_to_chess_coordinates(self, numeric_coordinate_tuple):
        i, j = numeric_coordinate_tuple
        letter = coordinates_j[j]
        number = coordinates_i[i]
        return f'{letter}-{number}'

    def make_move(self, from_idx, to_idx):
        from_tile = self.board.board[from_idx]
        to_tile = self.board.board[to_idx]
        moving_piece = from_tile.piece
        
        from_tile.occupied = False
        from_tile.piece = None
        
        to_tile.occupied = True
        to_tile.piece = moving_piece
        moving_piece.position = to_idx
        
        if moving_piece.piece_name == 'pawn':
            moving_piece.has_moved = True
        if moving_piece.piece_name == 'rook':
            moving_piece.has_moved = True
            moving_piece.can_castle = False
        if moving_piece.piece_name == 'king':
            moving_piece.can_castle = False
        if moving_piece.piece_name == 'king' and moving_piece.color == 'white':
            self.board.king_pos_white = to_idx
        if moving_piece.piece_name == 'king' and moving_piece.color == 'black':
            self.board.king_pos_black = to_idx

    def is_valid_move(self, from_idx, to_idx):
        from_tile = self.board.board[from_idx]
        piece = from_tile.piece
        
        if not from_tile.is_occupied():
            return False
        
        #need to make a check here to see if there is
            
        possible_moves = piece.get_possible_moves(self.board.board, from_idx)
        
        if to_idx not in possible_moves:
            return False

        board_copy = deepcopy(self.board)
        
        for idx, tile in enumerate(board_copy.board):
            if tile.is_occupied():
                tile.piece.position = idx
        
        moving_piece = board_copy.board[from_idx].piece
        if moving_piece.piece_name == 'king':
            setattr(board_copy, f'king_pos_{moving_piece.color}', to_idx)
        moving_piece.position = to_idx
        board_copy.board[to_idx].piece = moving_piece
        board_copy.board[to_idx].occupied = True
        board_copy.board[from_idx].piece = None
        board_copy.board[from_idx].occupied = False
        
        king_pos = to_idx if piece.piece_name == 'king' else getattr(board_copy, f'king_pos_{moving_piece.color}')
        our_king = board_copy.board[king_pos].piece
        
        if our_king is None:
            return False
            
        our_king.color = piece.color
        
        if our_king.king_in_check(board_copy.board):
            return False
            
        return True



