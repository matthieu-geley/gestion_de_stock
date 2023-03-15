import mysql.connector
import sys
sys.path.append('./classe')
from classe.Categorie import *
from classe.Produit import *
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title('Gestionnaire de Stock')
win.configure(bg="grey")
window_width = 1024
window_height = 600
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

win.mainloop()