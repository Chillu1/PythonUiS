import tkinter, random

class Gui:
    def __init__(self):
        self.window = tkinter.Tk()
        self.random_number = random.randint(1, 1000)
        self.is_number_guessed = False
        self.previous_guess = None
        self.index = 1

        self.number_status_text = tkinter.StringVar()
        self.number_status_text.set("")
        self.approach_status_text = tkinter.StringVar()
        self.approach_status_text.set("")
        self.index_info_text = tkinter.StringVar()
        self.index_info_text.set("This is your 1. try.")

        self.title = tkinter.Label(self.window, text="Guess a number from 1 to 1000: ")
        self.title.grid(column=0, row=0, padx=0, pady=3 )

        self.input = tkinter.Entry(self.window, width=4)
        self.input.grid(column=1, row=0, padx=5, pady=3 )


        self.index_info = tkinter.Label(self.window, textvariable=self.index_info_text)
        self.index_info.grid(column=0, row=1, padx=5, pady=7, columnspan=2, sticky =(tkinter.W, tkinter.E))

        self.button = tkinter.Button(self.window, text="Guess a number", command=self.input_handler)
        self.button.grid(column=0, row=2, padx=50, pady=3, columnspan=2 , sticky =(tkinter.W, tkinter.E))

        self.number_status = tkinter.Label(self.window, textvariable=self.number_status_text)
        self.number_status.grid(column=0, row=3, padx=7, pady=3, columnspan=2, sticky=(tkinter.W, tkinter.E))

        self.approach_status = tkinter.Label(self.window, textvariable=self.approach_status_text)
        self.approach_status.grid(column=0, row=4, padx=3, pady=3, columnspan=2, sticky=(tkinter.W, tkinter.E))

        tkinter.mainloop()


    def index_handler(self):
        self.index_info_text.set("This is your {} try.".format(self.index))

    def approach_handler(self, number):
        if self.previous_guess is not None:
            if abs(self.random_number - number) < abs(self.random_number - self.previous_guess):
                self.approach_status_text.set(f"You're getting closer, your previous guess was {self.previous_guess}")
            elif abs(self.random_number - number) > abs(self.random_number - self.previous_guess):
                self.approach_status_text.set(f"You're getting further, your previous guess was {self.previous_guess}")
            else:
                self.approach_status_text.set("")
        self.previous_guess = int(number)

    def victory_check(self):
        if self.is_number_guessed:
            self.number_status_text.set(f"You guessed the correct number! It took you {self.index} guesses")
            self.input.destroy()
            self.index_info_text.set("")
            self.title.destroy()
            self.button.destroy()
            self.approach_status.destroy()

    def input_handler(self):
        number = self.input.get()
        if number.isnumeric():
            if int(number) == self.random_number:
                self.is_number_guessed = True
            elif int(number) > 1000:
                self.number_status_text.set("Your number is too big.")
                return
            elif int(number) < 1:
                self.number_status_text.set("Your number is too small.")
                return
        else:
            self.number_status_text.set("Not a number.")
            return

        self.index += 1
        self.index_handler()
        self.approach_handler(int(number))
        self.victory_check()


if __name__ == "__main__":
    gui = Gui()