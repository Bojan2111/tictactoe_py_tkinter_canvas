"""
    This is a tkinter version of my Tic Tac Toe game. This version uses canvas
    which is better looking and easier to work with. It represents my beginner
    to intermediate Python 3 skills. Thanks to wonderful community of Stack
    Overflow and great and detailed tkinter documentation, I have managed to
    learn more about the tkinter itself, as well as produce a well written code.
    Since I work alone, there is no one to review my code, so if that's your
    expertise, please review this code, I would be grateful to learn more about
    how to improve this and every next code.
    If your find problems with this program, please send me your feedback, it
    would be great to improve this code even more.
    I haven't messed around with try/catch statements because I've tested each
    step during the writing of this code, but I believe I will manage to insert
    these as soon as possible.

    IMPORTANT! If you plan to edit this code, please keep in mind that changing
    some variables can alter the gameplay and can raise errors. Change variables
    at your own risk. Only the variables for declaring colors are completely safe
    to edit, as long as you know what you're doing.
    Also keep in mind that if you change the canvas dimensions, other coordinates
    need to be changed accordingly. I will try to edit the code to make this
    process possible without manually altering large amount of code, but for now
    this is what you get.

    I appreciate your feedback on this code. Thanks!
    
    Code written by: Bojan Adzic
"""
# Importing the necessary packages
from tkinter import *
from time import sleep


class TicTacToe():
    def __init__(self, master):
        # Master top level window settings
        master.title('Tic Tac Toe')
        self.master = master

        # Global variables, lists and dictionaries important for game logic. Change at your own risk.
        # Change only color values i.e. first six variables.
        self.border_color = 'purple'
        self.cross_color = 'black'
        self.field_color = 'gray'
        self.x_color = 'red'
        self.o_color = 'blue'
        self.win_line_color = 'silver'
        self.count = 0
        self.items_count = 0
        self.game_won = False
        self.game_count = 1

        # List of coordinates for drawing the X and O symbols for every squere -> [x_start, y_start, x_end, y_end]
        self.xo_coords = [[25, 25, 90, 90],
                          [132.5, 25, 197.5, 90],
                          [245, 25, 310, 90],
                          [25, 132.5, 90, 197.5],
                          [132.5, 132.5, 197.5, 197.5],
                          [245, 132.5, 310, 197.5],
                          [25, 245, 90, 310],
                          [132.5, 245, 197.5, 310],
                          [245, 245, 310, 310]]

        # Explanation: field_tagOrId=self.canvas.find_withtag("current")[0]:
        #    [is_clickable=bool, symbol='X' or 'O', [symbol_coords=x_start, y_start, x_end, y_end]]
        self.field_dict = {6: [True, '', self.xo_coords[0]],
                           7: [True, '', self.xo_coords[1]],
                           8: [True, '', self.xo_coords[2]],
                           9: [True, '', self.xo_coords[3]],
                           10: [True, '', self.xo_coords[4]],
                           11: [True, '', self.xo_coords[5]],
                           12: [True, '', self.xo_coords[6]],
                           13: [True, '', self.xo_coords[7]],
                           14: [True, '', self.xo_coords[8]]}

        # Create Canvas
        self.canvas = Canvas(master, width=327.5, height=327.5)
        self.canvas.pack()

        # Canvas Frame
        self.canvas.create_rectangle(4, 4, 328, 328, fill='white',
                                     outline=self.border_color, width=5)

        # Create Tic Tac Toe field separator lines
        self.canvas.create_line(
            110, 7, 110, 326, fill=self.cross_color, width=10)
        self.canvas.create_line(
            220, 7, 220, 326, fill=self.cross_color, width=10)
        self.canvas.create_line(
            7, 110, 326, 110, fill=self.cross_color, width=10)
        self.canvas.create_line(
            7, 220, 326, 220, fill=self.cross_color, width=10)

        # Create fields or squares only for clickability reasons
        # First row of fields
        self.a1 = self.canvas.create_rectangle(
            7, 7, 105, 105, fill=self.field_color)
        self.a2 = self.canvas.create_rectangle(
            115, 7, 215, 105, fill=self.field_color)
        self.a3 = self.canvas.create_rectangle(
            225, 7, 325, 105, fill=self.field_color)

        # Second row of fields
        self.b1 = self.canvas.create_rectangle(
            7, 115, 105, 215, fill=self.field_color)
        self.b2 = self.canvas.create_rectangle(
            115, 115, 215, 215, fill=self.field_color)
        self.b3 = self.canvas.create_rectangle(
            225, 115, 325, 215, fill=self.field_color)

        # Third row of fields
        self.c1 = self.canvas.create_rectangle(
            7, 225, 105, 325, fill=self.field_color)
        self.c2 = self.canvas.create_rectangle(
            115, 225, 215, 325, fill=self.field_color)
        self.c3 = self.canvas.create_rectangle(
            225, 225, 325, 325, fill=self.field_color)

        # Calling the method to add mouse button 1 (left button) click events to all clickable fields
        self.add_clicks()

    # Drawing X or O symbols on clicked square
    def field_click(self, event):

        # Symbol is either X or O, depending on the click count variable
        symb = 'X' if self.count % 2 == 0 else 'O'

        # Finding the tag ID (int) for putting things in field dictionary
        b = self.canvas.find_withtag("current")[0]
        i = self.field_dict[b][2]

        # Managing the drawing of symbols and keeping track of item's total number (for resetting purposes)
        if symb == 'X':
            self.field_dict[b][1] = 'X'
            self.canvas.create_line(
                i[0], i[1], i[2], i[3], fill=self.x_color, width=10)
            self.canvas.create_line(
                i[0], i[3], i[2], i[1], fill=self.x_color, width=10)
            self.items_count += 2   # Two items were drawn on canvas
        elif symb == 'O':
            self.field_dict[b][1] = 'O'
            o = self.canvas.create_oval(i[0], i[1], i[2], i[3],
                                        outline=self.o_color, width=10)
            self.items_count += 1   # One item was drawn on canvas

        self.count += 1
        self.field_dict[b][0] = False
        self.canvas.tag_unbind(b, '<Button-1>')
        if self.count > 4:
            self.win_check()

    # Resetting the fields, deleting symbols and other non-constant objects, or clearing score table if specified
    def game_reset(self):
        # Finding out the first and last ID for keeping the deletion process as effective as possible
        last_id = self.canvas.find_all()[-1] + 1
        new_item_start = self.canvas.find_all()[-self.items_count]
        # Deleting symbols and extra lines
        for i in range(new_item_start, last_id):
            self.canvas.delete(i)
        # Resetting the field dictionary
        for j in range(6, 15):
            self.field_dict[j][0] = True
            self.field_dict[j][1] = ''
        # Adding the click events back to the fields
        self.add_clicks()
        # Resetting counters and keeping track of the game number (for turn-changing purposes)
        self.count = 0
        self.items_count = 0
        self.game_count += 1

    # Checking if the player has won the game and displaying information on screen
    def win_check(self):
        # A nested list of winning combination of fields with coordinates for drawing the winning line (last 4 numbers)
        win_comb = [[6, 7, 8, 57.5, 57.5, 277.5, 57.5],
                    [7, 10, 13, 165, 57.5, 165, 277.5],
                    [12, 13, 14, 57.5, 277.5, 277.5, 277.5],
                    [6, 9, 12, 57.5, 57.5, 57.5, 277.5],
                    [9, 10, 11, 57.5, 165, 277.5, 165],
                    [8, 11, 14, 277.5, 57.5, 277.5, 277.5],
                    [12, 10, 8, 57.5, 277.5, 277.5, 57.5],
                    [6, 10, 14, 57.5, 57.5, 277.5, 277.5]]
        # Actual checking of winner
        for i in win_comb:
            # variables created for better code readability
            a = self.field_dict[i[0]][1]
            b = self.field_dict[i[1]][1]
            c = self.field_dict[i[2]][1]
            field_not_empty = a != '' and b != '' and c != ''
            if field_not_empty and a == b and b == c:
                self.canvas.create_line(i[3], i[4], i[5], i[6],
                                        fill=self.win_line_color, width=20)
                self.canvas.create_text(165, 165, font=('Arial', 30, 'bold'), fill='gold',
                                        text=f'{a} has won\nthis game!')
                self.items_count += 2   # Two items were drawn on canvas
                self.game_won = True

        # Disable other empty fields from clicking
        if self.game_won == True:
            for i in range(6, 15):
                if self.field_dict[i][0] == True:
                    self.canvas.tag_unbind(i, '<Button-1>')
            self.game_won = False
            self.master.update()
            sleep(2.4)
            self.game_reset()

    # Adding mouse button 1 (left) click events to all fields, binding them to field_click method
    def add_clicks(self):
        self.canvas.tag_bind(self.a1, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.a2, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.a3, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.b1, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.b2, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.b3, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.c1, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.c2, '<Button-1>', self.field_click)
        self.canvas.tag_bind(self.c3, '<Button-1>', self.field_click)

# main function


def main():
    root = Tk()
    tictactoe = TicTacToe(root)
    root.mainloop()


if __name__ == '__main__':
    main()
    
