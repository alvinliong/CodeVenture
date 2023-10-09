"""

"""

import tkinter as tk
import tkinter.font as tkFont

class GUI:
    def __init__(self, root):
        #setting title
        root.title("Code Venture")
        #setting window size
        width=1000
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        WindowTitle=tk.Label(root)
        WindowTitle["anchor"] = "center"
        WindowTitle["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=18)
        WindowTitle["font"] = ft
        WindowTitle["fg"] = "#333333"
        WindowTitle["justify"] = "center"
        WindowTitle["text"] = "Code Venture"
        WindowTitle.place(x=380,y=150,width=200,height=25)

        UsernameTextBox=tk.Entry(root)
        UsernameTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        UsernameTextBox["font"] = ft
        UsernameTextBox["fg"] = "#333333"
        UsernameTextBox["justify"] = "center"
        UsernameTextBox["text"] = ""
        UsernameTextBox.place(x=500,y=190,width=70,height=25)

        PasswordTextBox=tk.Entry(root)
        PasswordTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        PasswordTextBox["font"] = ft
        PasswordTextBox["fg"] = "#333333"
        PasswordTextBox["justify"] = "center"
        PasswordTextBox["text"] = ""
        PasswordTextBox.place(x=500,y=230,width=70,height=25)
        PasswordTextBox["show"] = "*"

        LoginButton=tk.Button(root)
        LoginButton["anchor"] = "center"
        LoginButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        LoginButton["font"] = ft
        LoginButton["fg"] = "#000000"
        LoginButton["justify"] = "center"
        LoginButton["text"] = "Login"
        LoginButton.place(x=500,y=270,width=70,height=35)
        LoginButton["command"] = self.LoginButton_command

        CreateAccButton=tk.Button(root)
        CreateAccButton["anchor"] = "center"
        CreateAccButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        CreateAccButton["font"] = ft
        CreateAccButton["fg"] = "#000000"
        CreateAccButton["justify"] = "center"
        CreateAccButton["text"] = "Create Account"
        CreateAccButton.place(x=420,y=270,width=70,height=35)
        CreateAccButton["command"] = self.CreateAccButton_command

        UsernameTXT=tk.Message(root)
        UsernameTXT["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=10)
        UsernameTXT["font"] = ft
        UsernameTXT["fg"] = "#333333"
        UsernameTXT["justify"] = "center"
        UsernameTXT["text"] = "Username"
        UsernameTXT.place(x=410,y=190,width=80,height=25)

        PasswordTXT=tk.Message(root)
        PasswordTXT["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=10)
        PasswordTXT["font"] = ft
        PasswordTXT["fg"] = "#333333"
        PasswordTXT["justify"] = "center"
        PasswordTXT["text"] = "Password"
        PasswordTXT.place(x=410,y=230,width=80,height=25)

    def LoginButton_command(self):
        print("command")

    def CreateAccButton_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
