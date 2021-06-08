import tkinter
from tkinter import messagebox


class Gjenstand:
    def __init__(self, navn, fra_aar, til_aar, sted):
        self.navn = navn
        self.fra_aar = fra_aar
        self.til_aar = til_aar
        self.sted = sted

    def __str__(self):
        return f"Navn: {self.navn}, fra år {self.fra_aar} til {self.til_aar}. Funnet i {self.sted}"


class GjenstandGUI:
    def __init__(self):
        self.gjenstander = []
        self.hovedvindu = tkinter.Tk()

        self.gjenstandLabel = tkinter.Label(self.hovedvindu, text="Navn på gjenstanden: ")
        self.gjenstandLabel.grid(column=0, row=0)
        self.gjenstandEntry = tkinter.Entry(self.hovedvindu, width=10)
        self.gjenstandEntry.grid(column=1, row=0)

        self.tidligsteArLabel = tkinter.Label(self.hovedvindu, text="Tidligste år: ")
        self.tidligsteArLabel.grid(column=0, row=1)
        self.tidligsteArEntry = tkinter.Entry(self.hovedvindu, width=10)
        self.tidligsteArEntry.grid(column=1, row=1)

        self.seinesteArLabel = tkinter.Label(self.hovedvindu, text="Seineste år: ")
        self.seinesteArLabel.grid(column=0, row=2)
        self.seinesteArEntry = tkinter.Entry(self.hovedvindu, width=10)
        self.seinesteArEntry.grid(column=1, row=2)

        self.stedLabel = tkinter.Label(self.hovedvindu, text="Hvor er gjenstanden fra: ")
        self.stedLabel.grid(column=0, row=3)
        self.stedEntry = tkinter.Entry(self.hovedvindu, width=10)
        self.stedEntry.grid(column=1, row=3)

        self.saveButton = tkinter.Button(self.hovedvindu, text="Lagre", command=self.register_gjenstand)
        self.saveButton.grid(column=0, row=4)
        self.clearButton = tkinter.Button(self.hovedvindu, text="Fjern innhold", command=self.clear_input)
        self.clearButton.grid(column=1, row=4)

        tkinter.mainloop()

    def clear_input(self):
        self.gjenstandEntry.delete(0, tkinter.END)
        self.tidligsteArEntry.delete(0, tkinter.END)
        self.seinesteArEntry.delete(0, tkinter.END)
        self.stedEntry.delete(0, tkinter.END)

    def register_gjenstand(self):
        name = self.gjenstandEntry.get()

        try:
            tidligAr = int(self.tidligsteArEntry.get())
        except ValueError or TypeError:
            messagebox.showerror("Feil data format", "År må være et helltall!")
            return
        try:
            seinesAr = int(self.seinesteArEntry.get())
        except ValueError or TypeError:
            messagebox.showerror("Feil data format", "År må være et helltall!")
            return

        sted = self.stedEntry.get()

        gjenstand = Gjenstand(name, tidligAr, seinesAr, sted)
        self.gjenstander.append(gjenstand)
        self.clear_input()


if __name__ == "__main__":
    gui = GjenstandGUI()

    for gjenstand in gui.gjenstander:
        print(gjenstand)
