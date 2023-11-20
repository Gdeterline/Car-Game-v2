import tkinter as tk
from tkinter import messagebox

# display popup
def show_popup():
    messagebox.showinfo("Crash", "You crashed !")

# new tkinter window
root = tk.Tk()

# popup displaying button
popup_button = tk.Button(root, text="What happened ?", command=show_popup)
popup_button.pack(pady=20)

# main loop
root.mainloop()