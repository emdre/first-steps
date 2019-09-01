import tkinter


class PersonalDataGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.text_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.show_button = tkinter.Button(self.button_frame, text='Show info', command=self.show_info)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.text_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        self.label = tkinter.Label(self.text_frame, text='M.D.\nulica Jakaśtam 1/2\n00-000 Miasto')
        self.label.pack()


personal_data = PersonalDataGUI()
