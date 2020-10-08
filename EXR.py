from forex_python.converter import CurrencyRates
from tkinter import *
import pyperclip
from time import sleep

c = CurrencyRates()

message = 'GBP ' + str(c.get_rate('GBP', 'USD'))
path = 'EUR ' + str(c.get_rate('EUR', 'USD'))
path2 = 'AUD ' + str(c.get_rate('AUD', 'USD'))
path3 ='CNY ' + str(c.get_rate('CNY', 'USD'))
path4 ='SGD ' + str(c.get_rate('SGD', 'USD'))
s = str(c.get_rate('GBP', 'USD')) + "\n" +str(c.get_rate('EUR', 'USD')) + "\n" +str(c.get_rate('AUD', 'USD')) + "\n" +str(c.get_rate('CNY', 'USD')) + "\n" + str(c.get_rate('SGD', 'USD'))
pyperclip.copy(s)


def alert_popup(title, message, path, path2, path3, path4):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    m += '\n'
    m += path2
    m += '\n'
    m += path3
    m += '\n'
    m += path4
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()
# Examples
alert_popup("Exchange rates",message,path,path2,path3,path4)
sleep(1)
