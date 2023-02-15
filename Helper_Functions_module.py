# imports
from screeninfo import get_monitors
from tkinter import Label, Button, Entry

class Helper_functions():

    '''
    DECS:- This module contains helper functions like Label, Button creator and grid them together
    '''
    def __init__(self, frame, bgcol='powder blue'):
        self.frame = frame
        self.bgcol = bgcol
        
    
    def create_label(self, text="Label Text", font_family='times new roman', font_size=12, font_style='bold', px=2, py=6):
        return Label(self.frame, bg=self.bgcol, text=text, font=(font_family, font_size, font_style), padx=px, pady=py)
    
    
    def grid_it(self,obj, row, col, sticky=None):
        obj.grid(row=row, column=col, sticky=sticky)
        
    
    def create_entry(self,textvariable, font_family='times new roman', font_size=12, font_style='italic', width=24):
        return Entry(self.frame,textvariable=textvariable , font=(font_family, font_size, font_style), width=width)
    
    def create_button(self,cmd=None, txt='Button Text', font_family='times new roman', font_size=12, font_style='italic', px=2, py=6, width=10, bg='white', fg='black'):
        return Button(self.frame, text=txt, command=cmd, font=(font_family, font_size, font_style), padx=px, pady=py, width=width, bg=bg, fg=fg)
    


def get_screen_res():
        w = get_monitors()[0].width
        h = get_monitors()[0].height
        x = get_monitors()[0].x
        y = get_monitors()[0].y
        return (w, h, x, y)
    