import tkinter


class GasUsageGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.tank_frame = tkinter.Frame(self.main_window)
        self.km_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.tank_label = tkinter.Label(self.tank_frame, text='Podaj pojemność baku w litrach:')
        self.tank_entry = tkinter.Entry(self.tank_frame, width=10)
        self.tank_label.pack(side='left')
        self.tank_entry.pack(side='left')

        self.km_label = tkinter.Label(self.km_frame, text='Podaj liczbę km, jaką można przejechać na pełnym baku:')
        self.km_entry = tkinter.Entry(self.km_frame, width=10)
        self.km_label.pack(side='left')
        self.km_entry.pack(side='left')

        self.result_label = tkinter.Label(self.result_frame, text='Liczba km, które przejedziesz na 1 l paliwa:')
        self.gas_usage = tkinter.StringVar()
        self.gas_usage_label = tkinter.Label(self.result_frame, textvariable=self.gas_usage)
        self.result_label.pack(side='left')
        self.gas_usage_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame, text='Oblicz zużycie paliwa', command=self.calc_gas_usage)
        self.quit_button = tkinter.Button(self.button_frame, text='Zakończ', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.tank_frame.pack()
        self.km_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calc_gas_usage(self):
        self.tank = float(self.tank_entry.get())
        self.km = float(self.km_entry.get())

        self.usage = self.km / self.tank

        self.gas_usage.set(self.usage)


gas_usage = GasUsageGUI()
