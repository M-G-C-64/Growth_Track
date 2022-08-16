import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Growth Tracker")

tex = tk.StringVar()

def clik():
    print(tex.get())

root.geometry("600x400+300+100")
root.resizable(False, False)
#root.attributes("-alpha",0.8)

ini = ttk.Frame(root)
ini.pack(padx=10, pady=10)

first_label = ttk.Label(ini, text="SELECT THE CATEGORY", font=("Verdana",16))
first_label.pack(ipadx=0, ipady=60)

entry1 = ttk.Entry(ini, textvariable=tex)
entry1.pack(ipadx=10, ipady=5)
entry1.focus()
print(tex.get())

cat_but = ttk.Button(
    ini,
    text = "temporary placeholder",
    command = clik
)
cat_but.pack(ipadx=10, ipady=5)

root.mainloop()