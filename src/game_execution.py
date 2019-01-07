import itertools
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import BOTH, RIGHT, LEFT, RAISED, Text
from tkinter.ttk import Frame, Button, Style
from src.timer import black_timer, white_timer

phase_iter = itertools.cycle('PT')
phases = {
    'P': 'Choose Piece',
    'T': 'Choose Target'
}
turn_iter = itertools.cycle('WB')
turns = {
    'W': 'White plays',
    'B': 'Black plays'
}
global piece_to_move
global place_to_move


class GameExecution(tk.Frame):

    def __init__(self):
        super().__init__()

        self.turn = next(turn_iter)
        self.phase = next(phase_iter)
        self.config(background='black')

        self.style = Style()

        self.init_ui()
        values = {}
        self.values = {}
        for v1 in 'phbqkt':
            for v2 in 'bw':
                for v3 in 'bw':
                    values[v1 + v2 + v3] = eval("Image.open('src/images/" + v1 + v2 + v3 + ".jpg')")
                    self.values[v1 + v2 + v3] = ImageTk.PhotoImage(values[v1 + v2 + v3])
                    self.label = tk.Label(image=self.values[v1 + v2 + v3])
                    self.label.values = dict()
                    self.label.values[v1 + v2 + v3] = self.values[v1 + v2 + v3]

    def init_ui(self):
        self.master.title("Chess")
        self.pack(fill=BOTH, expand=1)
        self.center_window()
        self.other()

    def center_window(self):

        w = 665
        h = 705

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.style.theme_use("default")

        my_text = Text(self, width=100, height=44)
        my_text.config(background='LightSteelBlue')
        my_text.insert('2.2', ' '*7 + (' '*11).join('123') + ' '*10 + (' '*11).join('45') + ' '*10 + (' '*11).join('67') + ' '*10 + (' '*11).join('8'))
        my_text.insert('2.2', '\n\n\n A' + '\n'*6 + ' B' + '\n'*5 + ' C' + '\n'*5 + ' D' + '\n'*6 + ' E' + '\n'*5 + ' F' + '\n'*5 + ' G' + '\n'*5 + ' H')
        my_text.pack()

    def other(self):
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        self.my_text = Text(self, width=80, height=1)
        self.my_text.insert('1.0', turns[self.turn] + ' - ' + phases[self.phase])
        self.my_text.pack(side=LEFT)

        button_style = Style()
        button_style.configure("TButton", background='white')
        close_button = Button(self, text="Quit", command=self.quit)
        close_button.pack(side=RIGHT, padx=5, pady=5)

    def button_pressed(self, position, board):
        global place_to_move
        global piece_to_move
        pos_value = board.obtain_pos_value(position)
        if self.phase == 'P' and pos_value[1] == self.turn:
            piece_to_move = position
            self.phase = next(phase_iter)
        elif self.phase == 'T':
            place_to_move = position
            if board.check_correct_move(piece_to_move, place_to_move, True):
                board.move_piece(piece_to_move, place_to_move)
                self.turn = next(turn_iter)
            self.phase = next(phase_iter)
        self.my_text.insert('1.0', turns[self.turn] + ' - ' + phases[self.phase] + '    White:' + white_timer.format_time() + ' Black:' + black_timer.format_time() + '\n')
        self.my_text.pack(side=LEFT)
        board.print_board()
        board.show_board(self)
