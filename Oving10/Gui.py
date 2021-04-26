import tkinter as tk

class Gui():
    def __init__(self,game):
        self.game = game
        self.root = tk.Tk()
        self.list = []
        for y in range(10):
            for x in range(10):
                self.list.append(tk.Button(self.root,
                                        text="",padx=17, pady=10,bg="gray",
                                        command=lambda coord_x=x, coord_y=y:self.changeColor(coord_x,coord_y)))
                coord = y*10+x
                self.list[coord].grid(row=y, column=x)

        self.root.mainloop()

    def changeColor(self,x,y):
        self.game.shoot(x, y)

        for y_all in range(10):
            for x_all in range(10):
                color = self.game.tile_status(x_all, y_all)
                if color == 2: # shot at but empty
                    self.list[y_all*10+x_all].configure(bg="blue")
                elif color == 3: # shot at and sunk
                    self.list[y_all*10+x_all].configure(bg="white")
                elif color == 4: # shot at but still alive
                    self.list[y_all*10+x_all].configure(bg="black")

        if self.game.victory() == True:
            self.root.destroy()
            vic = tk.Tk()
            vic.geometry("250x100")
            label = tk.Label(vic, text="You won!", font =25, padx=50, pady=50)
            label.pack()
            tk.mainloop()

        if self.game.shotat == 1:
            shotat = tk.Tk()
            shotat.geometry("250x100")
            label = tk.Label(shotat, text="This tile was already shot at!", font=25, padx=50, pady=50)
            label.pack()
            shotat.after(1500, lambda: shotat.destroy())
            shotat.mainloop()