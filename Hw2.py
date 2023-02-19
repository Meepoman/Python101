from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkinter import filedialog as fd

GUI = Tk()
GUI.title('PEDFE')
GUI.geometry('500x300')

L1 = Label(GUI, text='Progarm Export Data From Excel')
L1.place(x=20,y=20)

B1 = ttk.Button(GUI,text='Project Name')
B1.place(x=20,y=60)

B2 = ttk.Button(GUI,text='Data')
B2.place(x=20,y=100)

def Show():
    messagebox.showinfo('Date & Time', 'Current Date & Time: ' + str(datetime.now()))

B3 = ttk.Button(GUI,text='Current Date & Time',command=Show)
B3.place(x=240,y=100)

L1 = ttk.Label(GUI,text='Excel File Location')
L1.place(x=20,y=140)

B4 = ttk.Button(GUI,text='Seclect Excel file')
B4.place(x=20,y=170)

L2 = ttk.Label(GUI,text='Export to')
L2.place(x=200,y=140)

L3 = ttk.Label(GUI,text='Name Progarm')
L3.place(x=380,y=140)

B5 = ttk.Button(GUI,text='Seclection Progarm')
B5.place(x=360,y=170)


p_name = StringVar()
E1 = ttk.Entry(GUI, textvariable=p_name, width=10, justify='right', font=('Angsana New',15))
E1.place(x=120, y=60)

d_name = StringVar()
E1 = ttk.Entry(GUI, textvariable=d_name, width=10, justify='right', font=('Angsana New',15))
E1.place(x=120, y=100)

GUI.mainloop()
