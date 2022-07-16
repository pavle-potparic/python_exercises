import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Vezba")
# mainWindow.geometry("640x480+8+400")

label = tkinter.Label(mainWindow, text="Naslov")
label.pack(side="top")

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1)
canvas.pack(side="top", fill=tkinter.BOTH, expand=True)

mainWindow.mainloop()
