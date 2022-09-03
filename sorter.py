import random
from tkinter import *
from tkinter import ttk
from tkinter.font import ITALIC
from bubblesort import bubble_sort

root = Tk()
root.title('Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#ffffff')
root.resizable(False, False)


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i + 1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("new roman", 15, "bold"),
                           fill="orange")

    root.update_idletasks()


def StartAlgorithm():
    global data
    bubble_sort(data, drawData, speedscale.get())


def Generate():
    global data
    print('Selected Algorithm: ' + selected_algorithm.get())

    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())

    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue + 1))
    drawData(data, ['red' for x in range(len(data))])


selected_algorithm = StringVar()

mainlabel = Label(root, text="Sort With : ", font=("new roman", 16, "bold"),
                  bg="#5D8AA8", width=10, fg="black", relief=FLAT, bd=5)

mainlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(root, width=15, font=("new roman", 19, "bold"),
                         textvariable=selected_algorithm, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])

algo_menu.place(x=145, y=0)
algo_menu.current(0)

random_generate = Button(root, text="Generate", bg="#66ff00", font=("arial", 12, "bold"),
                         relief=SUNKEN, activebackground="#05945B", activeforeground="white",
                         bd=5, width=10, command=Generate)

random_generate.place(x=750, y=60)

sizevaluelabel = Label(root, text="Size : ", font=("new roman", 12, "bold"),
                       bg="#5D8AA8", width=10, fg="black", height=2, relief=FLAT, bd=5)
sizevaluelabel.place(x=0, y=60)

sizevalue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL,
                  font=("new roman", 14, "bold"), relief=GROOVE, bd=2, width=10)
sizevalue.place(x=120, y=60)


minvaluelabel = Label(root, text="Minimum : ", font=("new roman", 12, "bold"),
                      bg="#5D8AA8", width=10, fg="black", height=2, relief=FLAT, bd=5)
minvaluelabel.place(x=250, y=60)

minvalue = Scale(root, from_=0, to=10, resolution=1, orient=HORIZONTAL,
                 font=("new roman", 14, "bold"), relief=GROOVE, bd=2, width=10)
minvalue.place(x=370, y=60)

maxvaluelabel = Label(root, text="Maximum : ", font=("new roman", 12, "bold"),
                      bg="#5D8AA8", width=10, fg="black", height=2, relief=FLAT, bd=5)
maxvaluelabel.place(x=500, y=60)

maxvalue = Scale(root, from_=0, to=100, resolution=1, orient=HORIZONTAL,
                 font=("new roman", 14, "bold"), relief=GROOVE, bd=2, width=10)
maxvalue.place(x=620, y=60)

start = Button(root, text="Sort", bg="#66ff00", font=("arial", 12, "bold"),
               relief=SUNKEN, activebackground="#05945B", activeforeground="white",
               bd=5, width=10, command=StartAlgorithm)
start.place(x=750, y=0)

speedlabel = Label(root, text="Speed : ", font=("new roman", 12, "bold"),
                   bg="#5D8AA8", height=2, width=10, fg="black", relief=FLAT, bd=5)

speedlabel.place(x=500, y=0)

speedscale = Scale(root, from_=0.2, to=5.0, digits=2, resolution=0.2, orient=HORIZONTAL,
                   font=("new roman", 14, "bold"), relief=GROOVE, bd=2, width=10)

speedscale.place(x=620, y=0)

canvas = Canvas(root, width=870, height=450, bg="black")
canvas.place(x=10, y=130)
root.mainloop()
