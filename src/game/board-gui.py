import tkinter as tk
from tkinter import *

class ChessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.geometry("600x600")

        self.board_gui =[
            ["♖","♘","♗","♕","♔","♗","♘","♖"],
            ["♙","♙","♙","♙","♙","♙","♙","♙"],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ["♟","♟","♟","♟","♟","♟","♟","♟"],
            ["♜","♞","♝","♛","♚","♝","♞","♜"]
        ]

        self.canvas = tk.Canvas(self, width=600, height=600, bg='blue')
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                x0, y0 = i * 75, j * 75
                x1, y1 = x0 * 75, y0 + 75
                color = 'white' if (i + j) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        for i in range(8):
            for j in range(8):
                if self.board_gui[i][j] != ' ':
                    piece = self.board_gui[i][j]
                    x, y = j * 75 + 37.5, i * 75 + 37.5
                    self.canvas.create_text(x, y, text = piece, font=('Ariel', 36))
    def play(self):
        self.mainloop()
    
if __name__ == "__main__":
    game = ChessGame()
    game.play()