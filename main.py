from src.board.board import Board
from src.game.window import Window
from src.game.game import Game
import time
from src.controller.game_controller import GameController

def main():
    
    board = Board()
    board.setup_board()
    win = Window(800, 800)
    controller = GameController(win, board)
    win.set_controller(controller)
    win.wait_for_close()
    
    
main()