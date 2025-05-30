from src.board.board import Board
from src.game.window import Point, Square
import time, math
from src.game.game_util import coordinates_i, coordinates_j

class Game():
    def __init__(self, win, x1, y1, square_size_x, square_size_y, board):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.square_size_x = square_size_x
        self.square_size_y = square_size_y
        self.board = board.board_to_2d()
    
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()

    def update_board(self, current_board = None):
        if not current_board:
            board = Board()
            board.setup_board()
            return board.board_to_2d()
        else:
            board = current_board
            return board.board_to_2d()
        # this returns a 2d list of strings wit

    def draw_board(self):
        #places pieces and draws the board
        if not self.board:
            return
        
        for i in range(0,8):
            for j in range(0,8):
                top_left_coordinate = ((self.x1 + self.square_size_x * j),(self.y1 + self.square_size_y * i))
                bottom_right_coordinate = ((self.x1 + self.square_size_x * (j + 1)),(self.y1 + self.square_size_y * (i + 1)))
                point1 = Point(top_left_coordinate[0], top_left_coordinate[1])
                point2 = Point(bottom_right_coordinate[0], bottom_right_coordinate[1])
                coordinate = f'{coordinates_j[j]}-{coordinates_i[i]}'
                if (i + j) % 2 == 0:
                    square = Square(point1, point2, coordinate, "dark")
                else:
                    square = Square(point1, point2, coordinate, "light")
                self.win.draw_square(square)
                self.win.squares[coordinate] = square
                current_tile = self.board[i][j]
                if current_tile.is_occupied():
                    piece_name = current_tile.piece.piece_name
                    piece_color = current_tile.piece.color
                    path_to_piece = f"{piece_color}-{piece_name}"
                    square.piece = path_to_piece
                    self.win.place_piece(path_to_piece, square)
                self.animate()

        
