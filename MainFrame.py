# Third party imports
import tkinter as tk

# Local application imports
from LoginFrame import LoginFrame

class MainFrame(tk.Tk):
    """
    Class definition for the Main class
    """
    def __init__(self, title, width=960, height=540):
        """
        Constructor for the Interface class,
        the main window for the HCMS.
        :param title: str
        :param width: int - default 960 pixels
        :param height: int - default 540 pixels
        """
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

if __name__ == "__main__":
    MainFrame = MainFrame("Code Venture")
    LoginFrame = LoginFrame(MainFrame)
    LoginFrame.grid(column=0, row=0, sticky="nsew")
    LoginFrame.mainloop()
    print("--- End of program execution ---")