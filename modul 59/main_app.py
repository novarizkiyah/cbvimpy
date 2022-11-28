# Graphical User Interface

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="magenta")
window.geometry("300x200")
window.resizable(False, False)
window.title("Notes Apps")

#frame input
input_frame=ttk.Frame(window)
#penempatan Grid, pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

#komponen2
# 1/ label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(fill="x", expand=True)
NAMA_DEPAN = tk.StringVar()
nama_depan_entry=ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(fill="x", expand=True)


window.mainloop()