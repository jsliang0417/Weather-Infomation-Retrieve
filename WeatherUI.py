#!/usr/bin/python3
import tkinter as tk
import WeatherData


class WeatherUI:
    def __init__(self, master=None):
        # build ui
        
        self.Test = tk.Tk() if master is None else tk.Toplevel(master)
        self.Button_1 = tk.Button(self.Test)
        self.Button_1.configure(
            background="#ceffa9",
            cursor="arrow",
            disabledforeground="#ff4464",
            font="TkDefaultFont",
        )
        self.Button_1.configure(justify="center", text="Research")
        self.Button_1.place(
            anchor="sw", relx="0.26", rely="0.07", width="200", x="0", y="120"
        )
        self.Entry_1 = tk.Entry(self.Test)
        self.Entry_1.place(anchor="nw", relx="0.26", rely="0.03", x="0", y="0")
        self.Entry_2 = tk.Entry(self.Test)
        self.Entry_2.place(anchor="nw", relx="0.26", rely="0.11", x="0", y="0")
        self.Text_1 = tk.Text(self.Test)
        self.Text_1.configure(height="10", width="50")
        _text_ = """City"""
        self.Text_1.insert("0.0", _text_)
        self.Text_1.place(
            anchor="nw", height="20", relx="0.06", rely="0.03", width="45", x="0", y="0"
        )
        self.Text_2 = tk.Text(self.Test)
        self.Text_2.configure(height="10", width="50")
        _text_ = """State"""

        api = WeatherData(self.Entry_1.get(), self.Entry_2.get())
        
        self.Text_2.insert("0.0", _text_)
        self.Text_2.place(
            anchor="nw", height="20", relx="0.06", rely="0.11", width="45", x="0", y="0"
        )
        self.Text_3 = tk.Text(self.Test)
        self.Text_3.configure(height="10", width="50")
        self.Text_3.place(anchor="n", relx="0.27", rely="0.26", x="90", y="100")
        self.Test.configure(background="#72a4d4", height="600", width="400")
        self.Test.overrideredirect("False")
        self.Test.resizable(False, False)

        # Main widget
        self.mainwindow = self.Test

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = WeatherUI()
    app.run()
