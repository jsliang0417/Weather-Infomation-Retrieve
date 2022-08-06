# import io
# from PIL import Image, ImageTk
# try:
#     # Python2
#     import Tkinter as tk
#     from urllib2 import urlopen
# except ImportError:
#     # Python3
#     import tkinter as tk
#     from urllib.request import urlopen

# root = tk.Tk()
# root.title("Show image from URL")


# pic_url = "https://openweathermap.org/img/wn/09d@2x.png"

# # open the web page picture and read it into a memory stream
# # and convert to an image Tkinter can handle
# my_page = urlopen(pic_url)
# # create an image file object
# my_picture = io.BytesIO(my_page.read())
# # use PIL to open image formats like .jpg  .png  .gif  etc.
# pil_img = Image.open(my_picture)
# # convert to an image Tkinter can use
# tk_img = ImageTk.PhotoImage(pil_img)

# # put the image on a typical widget
# label = tk.Label(root, image=tk_img)
# label.pack(padx=5, pady=5)

# root.mainloop()


import tkinter as tk
import info_retrieve
from info_retrieve import retrieve_api
from time import sleep


class NewprojectApp:
    def __init__(self, master=None):
        
        self.city = ""
        self.state = ""
        # build ui
        
        self.Test = tk.Tk() if master is None else tk.Toplevel(master)
        self.Button_1 = tk.Button(self.Test)
        self.Button_1.configure(
            background="#ceffa9",
            cursor="arrow",
            disabledforeground="#ff4464",
            font="TkDefaultFont",
        )
        self.Button_1.configure(justify="center", text="Research", command=self.get_info)
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

        # api = info_retrieve(self.Entry_1.get(), self.Entry_2.get())

        
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

    
    def getCity(self):
        if self.Entry_1.get() != "":
            print("city: {0}".format(self.Entry_1.get()))
            self.city = self.Entry_1.get()
            return True
        else:
            print("Please enter the name of the City")
            return False

    
    def getState(self):
        if self.Entry_2.get() != "":
            print("State: {0}".format(self.Entry_2.get()))
            self.state = self.Entry_2.get()
            return True
        else:
            print("Please enter the name of the State")
            return False
        
    def get_info(self):
        self.getCity()
        self.getState()
        if self.getCity() == True and self.getState() == True:
            app = retrieve_api(self.city, self.state)
            # sleep(0.5)
            self.Text_3.insert(tk.END, "Temperature: " + str(app.get_weather_temp_fah())+"\n")
            self.Text_3.insert(tk.END, "Humidity: " + str(app.weather_humidity())+"\n")
            self.Text_3.insert(tk.END, "The weather today feels like: " + str(app.feels_like_fah())+"\n")
            self.Text_3.insert(tk.END, "Lowest Temperature: " + str(app.temp_min_fah())+"\n")
            self.Text_3.insert(tk.END, "Highest Temperature: " + str(app.temp_max_fah())+"\n")
            self.Text_3.insert(tk.END, "Description: " + str(app.get_weather_description())+"\n")
            
            

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()