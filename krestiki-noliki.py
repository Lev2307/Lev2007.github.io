from tkinter import *
#TODO: change import method, to fropm tkinter import module

# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = CANVAS_SIZE / 3
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'white'
EMPTY = NONE

# players setup
x = 'player 1'
o = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        # self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    def build_grid(self):
        x = CANVAS_SIZE // RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        for _ in range(2):
            self.canvas.create_line(x, y1, x, y2)
            self.canvas.create_line(y1, x, y2, x)
            x += CANVAS_SIZE // RATIO

    def render_cross(self, posX, posY):
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill='red', width=5)
        self.canvas.create_line(posX + f_size, posX, posY, posY + f_size, fill='red', width=5)


    def render_circle(self, posX, posY):
        """Magic number: 5, its a gap between edges and figure 
        Render 0 on field"""
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline='blue', width=5)

    def winner(self, player=None):
        """Display end game text, depends on player attribute
        and shutdown the game"""
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text=text, fill='lightseagreen', font='Arial 50')
        self.canvas.unbind('<Button-1>')

    def click_event(self):
        pass


game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid()


# Testing
game_v1.winner('Test')


game_v1.mainloop()                               