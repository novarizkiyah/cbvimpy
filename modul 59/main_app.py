# Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Init
window = tk.Tk()
window.configure(bg="magenta")
window.geometry("300x200")
window.resizable(False, False)
window.title("Notes Apps")

#Variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
def tombol_click():
    print(NAMA_BELAKANG.get())
    '''fungsi ini akan dipanggil tombol'''
    pesan = f"Halo, {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Selamat Datang!"
    showinfo(title="Hai", message=pesan)

#frame input
input_frame=ttk.Frame(window)
#penempatan Grid, pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

#komponen2
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(fill="x", expand=True)
# 2. entry nama depan

nama_depan_entry=ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(fill="x", expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang")
nama_belakang_label.pack(fill="x", expand=True)
#4. entry nama belakang

nama_belakang_entry=ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(fill="x", expand=True)

# 5. Tombol


tombol_sapa = ttk.Button(input_frame,text="Sapa", command=tombol_click)
tombol_sapa.pack(fill='x', expand=True, padx=10, pady=10)




window.mainloop()