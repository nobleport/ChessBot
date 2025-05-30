import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk




class Window():
    #I wanna keep the logic here simple, focused mainly on initializing the window.
    # Let's keep a lot of the game logic in the game class. 

    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Chess Game")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg = 'white', height = height, width = width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.bind('<Button-1>', self.on_click)
        self.running = False
        self.images={}
        self.squares={}
        self._load_piece_images()
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
    
    def on_click(self, event):
        if self.controller:
            self.controller.handle_square_click(event.x, event.y)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def close(self):
        self.running = False

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def draw_square(self, square):
        if square.color == "dark":
            square.draw(self.canvas)
        elif square.color == 'light':
            square.draw(self.canvas)
        self.squares[square.coordinate] = square

    def _load_piece_images(self):
        piece_types = ['white-pawn', 'white-rook', 'white-knight', 'white-bishop', 
                      'white-queen', 'white-king', 'black-pawn', 'black-rook', 
                      'black-knight', 'black-bishop', 'black-queen', 'black-king']
        for piece in piece_types:
            try:
                image = Image.open(f'piece_pngs/{piece}.png')
                self.images[piece] = ImageTk.PhotoImage(image)
            except FileNotFoundError:
                pass

    def place_piece(self, color_name_string, square):
        square.place_piece(self.canvas, self.images, color_name_string)
    
    def move_piece(self, from_square, to_square):
        try:
            color_name_string_on_from_sqr = from_square.color_name_string
            from_square.remove_piece(self.canvas)
            to_square.place_piece(self.canvas, self.images, color_name_string_on_from_sqr)
            self.redraw()
        except Exception:
            pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Square():
    def __init__(self, p1, p2, coordinate, color="dark", color_name_string=None):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.color_name_string = color_name_string
        self.coordinate = coordinate
        self.piece_id = None  # Store the canvas item ID
    
    def draw(self, canvas):
        if self.color == "dark":
            canvas.create_rectangle(
                self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill='#D3D3D3'
            )
        else:
            canvas.create_rectangle(
                self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill='#228B22'
            )

    def place_piece(self, canvas, images, color_name_string):
        # First remove any existing piece
        self.remove_piece(canvas)
        
        # Calculate center of square
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        
        if color_name_string in images:
            self.color_name_string = color_name_string
            self.piece_id = canvas.create_image(mid_x, mid_y, anchor=tk.CENTER, image=images[color_name_string])

    def remove_piece(self, canvas):
        if self.piece_id is not None:
            canvas.delete(self.piece_id)
            self.piece_id = None
            self.color_name_string = None

if __name__ == "__main__":
    win = ()
    win.play()