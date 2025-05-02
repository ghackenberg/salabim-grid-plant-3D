from tkinter import Tk, Canvas, mainloop

from ..Configuration import Layout, Order

canvas_width = 800
canvas_height = 600

padding = 100

unit = 10

def visualizeRoute(layout: Layout, order: Order) -> None:

    # Count corridors and machines

    num_corridors = len(layout.corridors)
    num_machines = 0

    for c in layout.corridors:
        num_machines = max(num_machines, len(c.machines_left))
        num_machines = max(num_machines, len(c.machines_right))

    print(num_corridors)
    print(num_machines)

    step_y = (canvas_height - padding * 2) / (num_corridors + 1)
    step_x = (canvas_width - padding * 2) / (num_machines * 2 + 3)

    # Initialize window

    root = Tk()

    # Initialize canvas

    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
    
    # Draw corridors

    canvas.create_rectangle(canvas_width / 2 - unit / 2, padding, canvas_width / 2 + unit / 2, canvas_height - padding, fill='red')

    for i in range(num_corridors):
        c = layout.corridors[i]

        y = padding + step_y * (i + 1)
        y0 = y - unit / 2
        y1 = y + unit / 2

        # Draw left arm
        if len(c.machines_left) > 0:
            x1 = canvas_width / 2 - step_x
            x0 = x1 - step_x * len(c.machines_left)
            canvas.create_rectangle(x0, y0, x1, y1, fill='green')
        
        # Draw right arm
        if len(c.machines_right) > 0:
            x0 = canvas_width / 2 + step_x
            x1 = x0 + step_x * len(c.machines_right)
            canvas.create_rectangle(x0, y0, x1, y1, fill='green')
    
    # Draw machines

    for i in range(num_corridors):
        c = layout.corridors[i]

        y = padding + step_y * (i + 1)
        y0 = y - unit
        y1 = y + unit

        for j in range(len(c.machines_left)):
            m = c.machines_left[j]

            x = canvas_width / 2 - step_x * (j + 2)
            x0 = x - unit
            x1 = x + unit

            canvas.create_rectangle(x0, y0, x1, y1, fill='blue')
        
        for j in range(len(c.machines_right)):
            m = c.machines_right[j]

            x = canvas_width / 2 + step_x * (j + 2)
            x0 = x - unit
            x1 = x + unit

            canvas.create_rectangle(x0, y0, x1, y1, fill='blue')

    mainloop()
