import tkinter as tk
from tkinter import Scrollbar

class PyInfoFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        self.configure(background="blue")
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        

        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Python Information",
                               font=("Arial Bold", 25))
        login_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)
        
        # The back button
        back_button = tk.Button(master=self, text="Back", command=self.back_command)
        back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

        self.text_box = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        self.text_box.config(state=tk.NORMAL)
        # The text is from "https://www.python.org/doc/essays/blurb/"
        self.text_box.insert(tk.END, """
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.
""")
        self.text_box.config(state=tk.DISABLED)
        self.text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.EW)

        scrollbar = Scrollbar(self, command=self.text_box.yview)
        scrollbar.grid(row=1, column=2, sticky='nsew')

        self.text_box['yscrollcommand'] = scrollbar.set

    def back_command(self):
        self.place_forget()
        #self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)