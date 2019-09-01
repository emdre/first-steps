import tkinter


class DictionaryGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.word1_frame = tkinter.Frame(self.main_window)
        self.word2_frame = tkinter.Frame(self.main_window)
        self.word3_frame = tkinter.Frame(self.main_window)

        self.word_button1 = tkinter.Button(self.word1_frame, text='sinister', command=self.show_translation1)
        self.word_button2 = tkinter.Button(self.word2_frame, text='dexter', command=self.show_translation2)
        self.word_button3 = tkinter.Button(self.word3_frame, text='medium', command=self.show_translation3)

        self.word_button1.pack(side='left')
        self.word_button2.pack(side='left')
        self.word_button3.pack(side='left')

        self.word1_frame.pack()
        self.word2_frame.pack()
        self.word3_frame.pack()

        tkinter.mainloop()

    def show_translation1(self):
        self.label = tkinter.Label(self.word1_frame, text='lewy')
        self.label.pack(side='left')

    def show_translation2(self):
        self.label = tkinter.Label(self.word2_frame, text='prawy')
        self.label.pack(side='left')

    def show_translation3(self):
        self.label = tkinter.Label(self.word3_frame, text='środkowy')
        self.label.pack(side='left')


dictionary = DictionaryGUI()
