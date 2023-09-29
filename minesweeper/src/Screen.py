#!/usr/bin/env python3
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import csv

Frame = None

def change_cell_color(x, y, color):
    canvas.itemconfig(cells[y][x], fill=color)
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def draw_cells(data):
    clear, buried, surface = 0, 0, 0
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            if value == '0':
                clear += 1
                change_cell_color(col_idx, row_idx, "white")
            elif value == '1':
                buried += 1
                change_cell_color(col_idx, row_idx, "#013220")
            elif value == '2':
                surface += 1
                change_cell_color(col_idx, row_idx, "#30D5C8")
    canvas.itemconfig(Texts[0], text=f"Clear Cells: {clear}")
    canvas.itemconfig(Texts[1], text=f"Buried Mines: {buried}")
    canvas.itemconfig(Texts[2], text=f"Surface Mines: {surface}")

def load_data_and_draw_cells():
    filename = "cell_data.csv"  # Replace with the path to your CSV file
    data = read_csv(filename)
    draw_cells(data)


photos = []
cells = [[]]
Texts = []
def init(app, W, H):

    # Create a new tkinter window
    global Frame, canvas

    # Create the homeFrame
    Frame = ctk.CTkFrame(master=app, width=W, height=H, bg_color="transparent" ,fg_color="transparent")
    Frame.place(x=0, y=0)

    # make canvas
    canvas = ctk.CTkCanvas(Frame, width=W, height=H,bg = "blue")
    canvas.place(x=0, y=0, anchor=tk.NW)

    
    # Load the image
    img = Image.open("Background3.jpg")
    img = img.resize((W, H))  # Resize the image to match the frame's dimensions
    # img.show()
    # Create the background image label
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(0, 0, image=photos[-1], anchor="nw")
    

    rows = 2
    columns = 1

    cell_width = 0.045 * canvas.winfo_reqwidth()   # 0.045 is the x_percent of the grid's starting position
    cell_height = 0.045 * canvas.winfo_reqwidth()  # 0.045 is the y_percent of the grid's starting position
    # Define the starting position of the grid
    grid_start_x = 0.5 * canvas.winfo_reqwidth()   # 0.5 is the x_percent of the grid's starting position
    grid_start_y = 0.09 * canvas.winfo_reqheight() # 0.09 is the y_percent of the grid's starting position

    # Function to draw a transparent cell
    def draw_transparent_cell(x, y, width, height, outline_width=1):
        # append the canvas ID into the cells grid
        return canvas.create_rectangle(x, y, x + width, y + height, fill="white", outline="#11A797", width=outline_width)

    canvas.create_rectangle(grid_start_x - 0.01 * canvas.winfo_reqwidth(), grid_start_y - 0.07 * canvas.winfo_reqheight(), grid_start_x + 10 * cell_width + 0.01 * canvas.winfo_reqwidth(), grid_start_y + 10 * cell_height + 0.02 * canvas.winfo_reqheight(), outline="#11A797", width=4, fill="white")
    # Create the 10x10 grid of transparent cells with a thicker outline
    for row in range(10):
        cells.append([])
        for col in range(10):
            x = grid_start_x + col * cell_width
            y = grid_start_y + row * cell_height
            cells[row].append(draw_transparent_cell(x, y, cell_width, cell_height, outline_width=4))  # Append the canvas ID into the cells grid
    canvas.create_text(grid_start_x + 5 * cell_width, grid_start_y - 0.04 * canvas.winfo_reqheight(), text="Minesweeper Team MOTQN", font=("Arial", 30, "bold"), fill="#36454F", anchor=tk.CENTER)
    # load button under the grid with image Assets/Reload.png
    # Photo box
    img = Image.open("Assets/Reload.png")
    img = img.resize((50, 50))  
    img = ctk.CTkImage(light_image=img, dark_image=img, size=(50, 50))
    photos.append(img)
    
    # canvas.create_image(30, 135, image=photos[-1], anchor="nw")
    load_button = ctk.CTkButton(canvas, image=photos[-1],text="", width=10, height=2, bg_color="white", fg_color="white", hover_color="white",font=("Arial", 20, "bold"), command=load_data_and_draw_cells)
    load_button.place(x=grid_start_x + 10 * cell_width - 0.01 * canvas.winfo_reqwidth(), y=grid_start_y - 0.035 * canvas.winfo_reqheight(), anchor=tk.CENTER)
    # Create three status texts that tells how many cells are white and how many with status 1 and how many with status 2
    Texts.append(canvas.create_text(0.2 * canvas.winfo_reqwidth(), 0.4 * canvas.winfo_reqheight(), text="Clear Cells: 100", font=("Arial", 40, "bold"), fill="white", anchor=tk.CENTER))
    Texts.append(canvas.create_text(0.2 * canvas.winfo_reqwidth(), 0.4 * canvas.winfo_reqheight() + 100, text="Buried Mines: 0", font=("Arial", 40, "bold"), fill="white", anchor=tk.CENTER))
    Texts.append(canvas.create_text(0.2 * canvas.winfo_reqwidth(), 0.4 * canvas.winfo_reqheight() + 200, text="Surface Mines: 0", font=("Arial", 40, "bold"), fill="white", anchor=tk.CENTER))

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Screen")
    app.geometry("800x480")
    W, H = 800, 480
    init(app, 800, 480)
    Frame.place(x=0, y=0)
    app.mainloop()