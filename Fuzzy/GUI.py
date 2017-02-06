import scipy
import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
import tkinter.messagebox as messagebox
from Fuzzy import FuzzySystem
fuzzy = None

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Fuzzy System") # set title of the window

        container = tk.Frame(self) # create the container contains all sub_windows
        container.pack(side="top", fill="both", expand=True) # pack it
        container.grid_rowconfigure(0, weight=1) # this is like 1x1 grid
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # store references to all sub_windows

        for Frame in (Fuzzy, Settings): # for each page class
            frame = Frame(container, self) # create page
            self.frames[Frame] = frame     # store into frames
            frame.grid(row=0, column=0, sticky='nsew') # pack it into container
        self.show_frame(Fuzzy) # set HomePage as default

        # create the menu bar
        menu_bar = tk.Menu(self)
        # create fuzzy menu
        fuzzy_menu = tk.Menu(menu_bar)
        fuzzy_menu.add_command(label='Fuzzy', compound='left', command=lambda : self.show_frame(Fuzzy))
        fuzzy_menu.add_separator()
        fuzzy_menu.add_command(label='Exit', compound='left', command=lambda : exit())
        menu_bar.add_cascade(label='Fuzzy', menu=fuzzy_menu)
        #create settings menu
        settings_menu = tk.Menu(menu_bar)
        settings_menu.add_command(label='Settings', compound='left', command=lambda : self.show_frame(Settings))
        menu_bar.add_cascade(label='Settings', menu=settings_menu)
        self.config(menu=menu_bar) # after you create it, you have to set it as menu_bar

        def exit():
            if messagebox.askokcancel('Quit?', 'Really Quit?'):
                self.destroy()
            return 'break'

    def show_frame(self, Frame):
        frame = self.frames[Frame] # get the reference to page
        frame.tkraise() # raise it to the top


class Fuzzy(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ###############################################
        input_frame = tk.LabelFrame(self, text="Input")
        input_frame.grid(row=0, column=0, sticky='wens', padx=5, pady=5)

        # BMI INPUTs
        self.button_question_mark_1 = tk.Button(input_frame, text='?')
        self.button_question_mark_1.grid(row=0, column=0, sticky='e', padx=(5,0))
        tk.Label(input_frame, text='Body Mass Index(kg/m^2)').grid(row=0, column=1, sticky='e', padx=10)
        self.bmi_slider_var = tk.DoubleVar()
        self.bmi_slider = tk.Scale(input_frame, variable=self.bmi_slider_var, orient=tk.HORIZONTAL, from_=0, to=35, resolution=0.1, command=lambda e: bmi_slider_handler())
        self.bmi_slider.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=(5,0))
        self.bmi_entry_var = tk.StringVar()
        self.bmi_entry = tk.Entry(input_frame, width=6, textvariable=self.bmi_entry_var)
        self.bmi_entry.bind('<Key>', lambda e: bmi_entry_handler())
        self.bmi_entry.grid(row=1, column=2, sticky=tk.S, padx=(0,5))

        # BF INPUTs
        self.button_question_mark_2 = tk.Button(input_frame, text='?')
        self.button_question_mark_2.grid(row=2, column=0, sticky='e', pady=(5,0))
        tk.Label(input_frame, text='Body Fat(%)').grid(row=2, column=1, sticky='w', padx=10,pady=(5,0))
        self.bf_slider_var = tk.DoubleVar()
        self.bf_slider = tk.Scale(input_frame, variable=self.bf_slider_var, orient=tk.HORIZONTAL, from_=0, to=35,resolution=0.1, command=lambda e: bf_slider_handler())
        self.bf_slider.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E, padx=(5,0))
        self.bf_entry_var = tk.StringVar()
        self.bf_entry = tk.Entry(input_frame, width=6, textvariable=self.bf_entry_var)
        self.bf_entry.bind('<Key>', lambda e: bf_entry_handler())
        self.bf_entry.grid(row=3, column=2, sticky=tk.S, padx=(0,5))

        # WC INPUTs
        self.button_question_mark_3 = tk.Button(input_frame, text='?')
        self.button_question_mark_3.grid(row=4, column=0, sticky='e', pady=(5, 0))
        tk.Label(input_frame, text='Waist Circumference(cm)').grid(row=4, column=1, sticky='w', padx=10, pady=(5, 0))
        self.wc_slider_var = tk.DoubleVar()
        self.wc_slider = tk.Scale(input_frame, variable=self.wc_slider_var, orient=tk.HORIZONTAL, from_=0, to=120,
                                  resolution=0.1, command=lambda e: wc_slider_handler())
        self.wc_slider.grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E, padx=(5,0))
        self.wc_entry_var = tk.StringVar()
        self.wc_entry = tk.Entry(input_frame, width=6, textvariable=self.wc_entry_var)
        self.wc_entry.bind('<Key>', lambda e: wc_entry_handler())
        self.wc_entry.grid(row=5, column=2, sticky=tk.S)

        start_button = tk.Button(input_frame, text='Start')
        start_button.grid(row=6, column=1, sticky=tk.E+tk.W, padx=(0,5))


        ##################################################
        output_frame = tk.LabelFrame(self, text="Output")
        output_frame.grid(row=0, column=1, sticky='news', padx=5, pady=5)
        tk.Label(output_frame, text='Obesity Level:').grid(row=0, column=0, sticky='w', padx=(5,0))
        self.ol_entry_var = tk.StringVar()
        self.ol_entry = tk.Entry(output_frame, textvariable=self.ol_entry_var)
        self.ol_entry.grid(row=0, column=1, sticky='w')
        tk.Label(output_frame, text='Suggestion:').grid(row=1, column=0, sticky='w', padx=(5,0))
        temp = tk.Frame(output_frame, borderwidth=3, relief=tk.RAISED)
        temp.grid(row=2, column=0, columnspan=2, rowspan=2, padx=5)
        self.suggest_text = tk.Text(temp, cursor='plus', wrap=tk.WORD, width=47, height=10)
        self.suggest_text.grid(row=0, column=0, sticky='news')
        self.suggest_text.config(state=tk.DISABLED) # read only text
        tk.Label(output_frame, text='Your should ask your doctor if obesity level >= 60!!').grid(row=5, column=0, columnspan=2, sticky='ne', padx=5)


        ##################################################
        process_frame = tk.LabelFrame(self, text="Process")
        process_frame.grid(row=1, column=0, columnspan=2, sticky='news', padx=5, pady=5)
        temp1 = tk.Frame(process_frame, borderwidth=3, relief=tk.RAISED)
        temp1.grid(row=0, column=0, padx=5, pady=5)
        self.process_text = tk.Text(temp1, cursor='plus', wrap=tk.WORD, width=90)
        self.process_text.grid(row=0, column=0, sticky='news')



        ###############--Handlers--###############
        def bmi_entry_handler(event=None):
            try:
                self.bmi_slider_var.set(float(self.bmi_entry_var.get()))
            except:
                pass

        def bmi_slider_handler(event=None):
            self.bmi_entry_var.set(str("%.2f" % (self.bmi_slider_var.get())))

        def bf_entry_handler(event=None):
            try:
                self.bf_slider_var.set(float(self.bf_entry_var.get()))
            except:
                pass

        def bf_slider_handler(event=None):
            self.bf_entry_var.set(str("%.2f" % (self.bf_slider_var.get())))

        def wc_entry_handler(event=None):
            try:
                self.wc_slider_var.set(float(self.wc_entry_var.get()))
            except:
                pass

        def wc_slider_handler(event=None):
            self.wc_entry_var.set(str("%.2f" % (self.wc_slider_var.get())))


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Settings')
        label.pack(padx=10, pady=10)




if __name__ == '__main__':
    fuzzy_system = FuzzySystem(0, 35, 0, 35, 0, 120, 0, 100)
    fuzzy_system.set_bmi(0, 15, 22, 15, 22, 29, 22, 29, 35)
    fuzzy_system.set_bf(0, 15, 22, 15, 22, 29, 22, 29, 35)
    fuzzy_system.set_wc(0, 30, 60, 30, 60, 90, 60, 90, 120)
    fuzzy_system.set_o(0, 20, 40, 30, 50, 70, 60, 80, 100)
    fuzzy_system.make_variables()
    fuzzy_system.make_member_functions()
    fuzzy_system.make_rules()

    print(fuzzy_system.simulate(20, 15, 45))

    root = MainWindow()
    root.mainloop()