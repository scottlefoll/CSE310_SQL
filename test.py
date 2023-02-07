import tkinter as tk                    # imports
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import scrolledtext


# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0: monty2.configure(text='Blue')
    elif radSel == 1: monty2.configure(text='Gold')
    elif radSel == 2: monty2.configure(text='Red')
    
    
# Spinbox callback 
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')
    
    
win = tk.Tk()                           # Create instance      
win.title("Python GUI")                 # Add a title 

tabControl = ttk.Notebook(win)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible
# tab3 = ttk.Frame(tabControl)            # Add a third tab
# tabControl.add(tab3, text='Tab 3')      # Make second tab visible
tab3 = tk.Frame(tab3, bg='blue')
tab3.pack()
for orangeColor in range(2):
    canvas = tk.Canvas(tab3, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)
    
tabControl.pack(expand=1, fill="both")  # Pack to make visible

monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)

# Using a scrolled Text control       # 3
scrolW  = 30                          # 4
scrolH  =  3                          # 5
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)                         # 6
scr.grid(column=0, columnspan=3)      # 7

# Adding a Spinbox widget
spin = Spinbox(monty, from_=0, to=10, width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)

# Adding a second Spinbox widget 
spin = Spinbox(monty, values=(0, 50, 100), width=5, bd=20, command=_spin) 
spin.grid(column=1, row=2)

# Adding a Spinbox widget using a set of values
# spin = Spinbox(monty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin) 
# spin.grid(column=0, row=2)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty2, text="Disabled", variable=chVarDis, state='disabled')

win.mainloop()                          # Start GUI
