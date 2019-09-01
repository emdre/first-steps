import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.text_frame = tkinter.Frame(self.main_window)
        self.services_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.intro = tkinter.Label(self.text_frame, text='Wybierz usługi, z któych chcesz skorzystać:')
        self.intro.pack(side='left')

        self.cb1 = tkinter.Checkbutton(self.services_frame, text='Wymiana oleju: 30 zł',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.services_frame, text='Smarowanie: 20 zł',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.services_frame, text='Sprawdzanie chłodnicy: 40 zł',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.services_frame, text='Sprawdzanie skrzyni biegów: 100 zł',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.services_frame, text='Przegląd: 35 zł',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.services_frame, text='Wymiana tłumika: 200 zł',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.services_frame, text='Wyważenie kół: 20 zł',
                                       variable=self.cb_var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.show_button = tkinter.Button(self.button_frame, text='Oblicz koszt usług', command=self.show_cost)
        self.quit_button = tkinter.Button(self.button_frame, text='Zakończ', command=self.main_window.destroy)

        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.text_frame.pack()
        self.services_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show_cost(self):

        self.cost = 0

        if self.cb_var1.get() == 1:
            self.cost += 30
        if self.cb_var2.get() == 1:
            self.cost += 20
        if self.cb_var3.get() == 1:
            self.cost += 40
        if self.cb_var4.get() == 1:
            self.cost += 100
        if self.cb_var5.get() == 1:
            self.cost += 35
        if self.cb_var6.get() == 1:
            self.cost += 200
        if self.cb_var7.get() == 1:
            self.cost += 20

        tkinter.messagebox.showinfo('Koszt', 'Łączny koszt usług: ' + str(self.cost) + 'zł.')


my_gui = MyGUI()
