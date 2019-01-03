import argparse
import itertools
import logging
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, BOTH, RIGHT, RAISED, Text, SUNKEN
from tkinter.ttk import Frame, Button, Style, Label
from src.checks.checks import check_correct_move
from src.conf.settings import size_x, size_y
from src.conf.board_init import board_init
from src.conf.logger import setup_logger
from src.input_output.inputs import choose_move, choose_piece
from src.input_output.outputs import print_table, clean_screen, start_print
from src.moves.moves import move_piece


turn_iter = itertools.cycle('WB')

formatter = logging.Formatter('%(message)s')
current_logger = setup_logger('log1', "logs/current.log", with_formatter=formatter)
super_logger = setup_logger('log2', "logs/all.log")


def main_function(coord_x_or, coord_y_or, turn, cont_file=''):
    if cont_file != '':
        file = open(cont_file, 'r')
    else:
        file = ''
    board = board_init(coord_x_or, coord_y_or)
    print_table(board)
    while True:
        if cont_file != '':
            try:
                line = next(file)
                turn_move = line.replace('\n', '')
            except StopIteration:
                turn_move = False
                cont_file = ''
        else:
            turn_move = False
        position = 0
        correct_move = 0
        target = 0
        while not correct_move:
            while not position:
                if turn_move:
                    position = choose_piece(turn, board, turn_move.split()[0])
                else:
                    position = choose_piece(turn, board)

            if turn_move:
                target = choose_move(board, turn_move.split()[1])
            else:
                target = choose_move(board)
            if target:
                correct_move = check_correct_move(position, target, board)
            else:
                position = 0
        board = move_piece(position, target, board)
        print_table(board)
        turn = next(turn_iter)


class GameExecution(tk.Frame):

    def __init__(self):
        super().__init__()
        self.config(background='black')

        self.style = Style()

        self.init_ui()
        pbw = Image.open('src/images/pbw.jpg')
        pww = Image.open('src/images/pww.jpg')
        hww = Image.open('src/images/hww.jpg')
        hbw = Image.open('src/images/hbw.jpg')
        bww = Image.open('src/images/bww.jpg')
        bbw = Image.open('src/images/bbw.jpg')
        qww = Image.open('src/images/qww.jpg')
        qbw = Image.open('src/images/qbw.jpg')
        kww = Image.open('src/images/kww.jpg')
        kbw = Image.open('src/images/kbw.jpg')
        tww = Image.open('src/images/tww.jpg')
        tbw = Image.open('src/images/tbw.jpg')
        pbb = Image.open('src/images/pbb.jpg')
        pwb = Image.open('src/images/pwb.jpg')
        hwb = Image.open('src/images/hwb.jpg')
        hbb = Image.open('src/images/hbb.jpg')
        bwb = Image.open('src/images/bwb.jpg')
        bbb = Image.open('src/images/bbb.jpg')
        qwb = Image.open('src/images/qwb.jpg')
        qbb = Image.open('src/images/qbb.jpg')
        kwb = Image.open('src/images/kwb.jpg')
        kbb = Image.open('src/images/kbb.jpg')
        twb = Image.open('src/images/twb.jpg')
        tbb = Image.open('src/images/tbb.jpg')
        b = Image.open('src/images/black.jpg')
        w = Image.open('src/images/white.jpg')
        self.hww = ImageTk.PhotoImage(hww)
        self.pww = ImageTk.PhotoImage(pww)
        self.pbw = ImageTk.PhotoImage(pbw)
        self.hbw = ImageTk.PhotoImage(hbw)
        self.bww = ImageTk.PhotoImage(bww)
        self.bbw = ImageTk.PhotoImage(bbw)
        self.qww = ImageTk.PhotoImage(qww)
        self.qbw = ImageTk.PhotoImage(qbw)
        self.kww = ImageTk.PhotoImage(kww)
        self.kbw = ImageTk.PhotoImage(kbw)
        self.tww = ImageTk.PhotoImage(tww)
        self.tbw = ImageTk.PhotoImage(tbw)
        self.hwb = ImageTk.PhotoImage(hwb)
        self.pwb = ImageTk.PhotoImage(pwb)
        self.pbb = ImageTk.PhotoImage(pbb)
        self.hbb = ImageTk.PhotoImage(hbb)
        self.bwb = ImageTk.PhotoImage(bwb)
        self.bbb = ImageTk.PhotoImage(bbb)
        self.qwb = ImageTk.PhotoImage(qwb)
        self.qbb = ImageTk.PhotoImage(qbb)
        self.kwb = ImageTk.PhotoImage(kwb)
        self.kbb = ImageTk.PhotoImage(kbb)
        self.twb = ImageTk.PhotoImage(twb)
        self.tbb = ImageTk.PhotoImage(tbb)
        self.b = ImageTk.PhotoImage(b)
        self.w = ImageTk.PhotoImage(w)
        self.label = tk.Label(image=self.pbb)
        self.label.pbw = self.pbw
        self.label.pww = self.pww
        self.label.hww = self.hww
        self.label.hbw = self.hbw
        self.label.bww = self.bww
        self.label.bbw = self.bbw
        self.label.qww = self.qww
        self.label.qbw = self.qbw
        self.label.kww = self.kww
        self.label.kbw = self.kbw
        self.label.tww = self.tww
        self.label.tbw = self.tbw
        self.label.pbb = self.pbb
        self.label.pwb = self.pwb
        self.label.hwb = self.hwb
        self.label.hbb = self.hbb
        self.label.bwb = self.bwb
        self.label.bbb = self.bbb
        self.label.qwb = self.qwb
        self.label.qbb = self.qbb
        self.label.kwb = self.kwb
        self.label.kbb = self.kbb
        self.label.twb = self.twb
        self.label.tbb = self.tbb
        self.label.b = self.b
        self.label.w = self.w
        self.pack()

    def init_ui(self):
        self.master.title("Chess")
        self.pack(fill=BOTH, expand=1)
        self.center_window()

    def center_window(self):

        w = 665
        h = 720

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.style.theme_use("default")

        my_text = Text(self, width=100, height=45)
        my_text.config(background='LightSteelBlue')
        my_text.insert('2.2', ' '*7 + (' '*11).join('123') + ' '*10 + (' '*11).join('45') + ' '*10 + (' '*11).join('67') + ' '*10 + (' '*11).join('8'))
        my_text.insert('2.2', '\n\n\n A' + '\n'*6 + ' B' + '\n'*5 + ' C' + '\n'*5 + ' D' + '\n'*6 + ' E' + '\n'*5 + ' F' + '\n'*5 + ' G' + '\n'*5 + ' H')
        my_text.pack()

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        close_button = Button(self, text="Quit", command=self.quit)
        close_button.pack(side=RIGHT, padx=5, pady=5)

    def show_board(self, curr_board):
        button_style = Style()

        for ind1, x in enumerate(curr_board):
            for ind2, y in enumerate(x):
                if y.lower() == 'pw':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=self.button_pressed(y.lower()), image=self.pwb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=self.button_pressed(y.lower()), image=self.pww)
                elif y.lower() == 'pb':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=print('pressed'), image=self.pbb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=print('pressed'), image=self.pbw)
                elif y.lower() == 'qw':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.qwb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.qww)
                elif y.lower() == 'qb':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.qbb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.qbw)
                elif y.lower() == 'kw':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.kwb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.kww)
                elif y.lower() == 'kb':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.kbb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.kbw)
                elif y.lower() == 'bw':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.bwb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.bww)
                elif y.lower() == 'bb':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.bbb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.bbw)
                elif y.lower() == 'tw':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.twb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.tww)
                elif y.lower() == 'tb':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.tbb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.tbw)
                elif y.lower() == 'hw':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.hwb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.hww)
                elif y.lower() == 'hb':
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.hbb)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.hbw)
                else:
                    if (ind1 + ind2) % 2 == 1:
                        button_style.configure("TButton", background='black', foreground='black')
                        piece_button = Button(self, command=None, image=self.b)
                        self.pack(fill=BOTH, expand=True)
                    else:
                        button_style.configure("TButton", background='white', foreground='white')
                        piece_button = Button(self, command=None, image=self.w)
                        self.pack(fill=BOTH, expand=True)
                piece_button.place(x=(80*ind2) + 25, y=(80*ind1)+25, width=74, height=74)

        self.pack(fill=BOTH, expand=True)

    def button_pressed(self, button_name):
        print(button_name)


if __name__ == "__main__":

    # Arguments are taken from command line

    parser = argparse.ArgumentParser(description='Python Chess',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--sizex', action="store", dest="size_x",
                        help="Horizontal size of the chess board",
                        default=size_x, type=int)
    parser.add_argument('--sizey', action="store", dest="size_y",
                        help="Vertical size of the chess board",
                        default=size_y, type=int)
    parser.add_argument('-c', action="store_true",
                        help="If you want to continue a game stored in src/logs/movements.log")
    args = parser.parse_args()
    size_x = args.size_x
    size_y = args.size_y

    initial_turn = next(turn_iter)

    root = Tk()
    app = GameExecution()
    board = board_init(size_x, size_y)
    app.show_board(board)
    root.mainloop()
    '''
    clean_screen()
    
    start_print()

    if args.c:
        main_function(size_x, size_y, turn=initial_turn, cont_file='logs/movements.log')
    else:
        main_function(size_x, size_y, turn=initial_turn)
    '''
