# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser_coords):
    # Eraser ke andar jo bhi rectangles aayenge unko delete karenge
    x1, y1, x2, y2 = eraser_coords
    overlap = canvas.find_overlapping(x1, y1, x2, y2)
    for obj in overlap:
        # Eraser khud delete na ho jaaye, so eraser ko skip karo
        if obj != eraser_id:
            canvas.itemconfig(obj, fill='white')  # Erase by changing color

def on_mouse_move(event):
    # Eraser ko mouse ke saath move karna
    x, y = event.x, event.y
    canvas.coords(eraser_id, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    erase_objects(canvas, (x, y, x + ERASER_SIZE, y + ERASER_SIZE))

root = tk.Tk()
root.title("Eraser Canvas")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Grid create karna
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Eraser create karo (initially canvas ke top-left mein rakha hai)
eraser_id = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="")

# Mouse movement bind karna
canvas.bind("<Motion>", on_mouse_move)

root.mainloop()
