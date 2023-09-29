#!/usr/bin/env python3
import threading
import tkinter as tk
import customtkinter as ctk
import Screen

def UI():
    app = ctk.CTk()
    app.title("GUI")
    W, H = app.winfo_screenwidth(), app.winfo_screenheight()
    # W, H = 800, 400
    app.geometry("%dx%d+0+0" % (W, H))
    Screen.init(app, W, H)
    app.resizable(False, False)
    app.mainloop()


        
def main():
    UI()

if __name__ == "__main__":
    main()