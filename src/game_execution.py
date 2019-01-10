import itertools
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import BOTH, CENTER, RIGHT, LEFT, RAISED, Text
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


class GameExecution(tk.Frame):

    def __init__(self, mode):
        super().__init__()

        self.mode = mode
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

        self.piece_to_move = ''
        self.place_to_move = ''

    def init_ui(self):
        """
        This method initializes the GUI.
        """
        self.master.title("Python Chess")
        self.pack(fill=BOTH, expand=1)
        self.center_window()
        self.message_board()
        self.close_button()

    def center_window(self):
        """
        This method prepares the board interface.
        """
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

    def message_board(self):
        """
        This method prepares the message interface.
        """
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        self.my_text = Text(self, width=80, height=1)
        self.my_text.insert('1.0', turns[self.turn] + ' - ' + phases[self.phase])
        self.my_text.pack(side=LEFT, padx=5)

    def close_button(self):
        """
        This method prepares the close button.
        :return:
        """
        button_style = Style()
        button_style.configure("TButton", background='white')
        close_button = Button(self, text="Quit", command=self.quit)
        close_button.pack(side=RIGHT, padx=5, pady=5)

    def pressed(self, position, board):
        """
        This method is called every time a board button is pressed. It
        checks the current turn and phase, to check if the pressed button
        belongs to a possible situation, and acts consequently.
        :param position: (tuple) the position of the pressed button.
        :param board: (Board) the current game board.
        """
        pos_value = board.get_pos_val(position)
        if self.phase == 'P' and pos_value[1] == self.turn:
            self.piece_to_move = position
            self.phase = next(phase_iter)
            if self.mode == 'normal':
                board.check_movements(position)
                print(board.squares)
        elif self.phase == 'T':
            self.place_to_move = position
            if board.check_correct_move(self.piece_to_move, self.place_to_move, True):
                board.move_piece(self.piece_to_move, self.place_to_move)
                self.turn = next(turn_iter)
            self.phase = next(phase_iter)
        self.my_text.insert('1.0', turns[self.turn] + ' - ' + phases[self.phase] + '    White:' + white_timer.format_time() + ' Black:' + black_timer.format_time() + '\n')
        self.my_text.pack(side=LEFT)
        board.print_board_in_terminal()
        self.show_board(board)

    def show_board(self, board):
        """
        This method creates all the buttons needed to represent a board in
        the current game instance.
        :param board: (GameExecution) The current board.
        """
        button_style = Style()
        button_style.configure("B.TLabel", background='black')
        button_style.configure("W.TLabel", background='white')
        button_style.configure("Y.TLabel", background='yellow')
        button_style.configure("R.TLabel", background='red')
        button_style.configure("G.TLabel", background='green')
        param = ''
        for ind1, x in enumerate(board.squares):
            for ind2, y in enumerate(x):
                if (ind1 + ind2) % 2 == 1:
                    color = 'B'
                    try:
                        param = eval('self.values["' + y.lower()[0:2] + 'b"]')
                    except KeyError:
                        pass
                else:
                    color = 'W'
                    try:
                        param = eval('self.values["' + y.lower()[0:2] + 'w"]')
                    except KeyError:
                        pass
                if y[2] == 'k' or y[3] == 'c' or y[4] == 'l':
                    if y[2] == 'k':
                        color = 'R'
                    elif y[3] == 'c':
                        color = 'Y'
                    elif y[4] == 'l':
                        color = 'G'
                    board.put_pos_val((ind1, ind2), board.get_pos_val((ind1, ind2))[0:2] + '   ')
                if y.lower()[0:4] != '    ':
                    piece_button = Button(self,
                                          style=color+".TLabel",
                                          command=lambda v=(ind1, ind2): self.pressed(v, board),
                                          image=param,
                                          compound=CENTER)
                else:
                    piece_button = Button(self,
                                          style=color+".TLabel",
                                          command=lambda v=(ind1, ind2): self.pressed(v, board))

                piece_button.place(x=(80*ind2) + 25, y=(80*ind1)+25, width=74, height=74)
        self.pack()
