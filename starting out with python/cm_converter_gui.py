import tkinter
import tkinter.messagebox


class CmConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='Podaj wartość w centymetrach:')
        self.cm_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.cm_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Konwertuj na metry', command=self.convert_meters)
        self.calc_button2 = tkinter.Button(self.bottom_frame, text='Konwertuj na cale', command=self.convert_inches)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Zakończ', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.calc_button2.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert_meters(self):
        cm = float(self.cm_entry.get())
        m = cm/100

        tkinter.messagebox.showinfo('Wynik', '{} cm to {:.4f} m'.format(cm, m))

    def convert_inches(self):
        cm = float(self.cm_entry.get())
        cal = cm * 0.3937

        tkinter.messagebox.showinfo('Wynik', '{} cm to {:.4f} in'.format(cm, cal))


cm_conv = CmConverterGUI()
