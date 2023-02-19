from tkinter import *
from tkinter import ttk, messagebox
import math

GUI = Tk()
GUI.title('โปรแกรมจัดการ Layout')
GUI.geometry('500x300')

L1 = Label(GUI,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_kilo, width=10, justify='right', font=('Angsana New',25))
E1.pack(pady=20)

def calc(event=None):
    print('กำลังคำนวณ....กรุณารอสักครู่')
    kilo = float(v_kilo.get())
    print(kilo * 10)
    calc_result = kilo * 299
    messagebox.showinfo('รวมราคาทั้งหมด', 'ลูกค้าต้องจ่ายเงินทั้งหมด: {:.2f} บาท (กิโลกรัมละ 299 บาท)'.format(calc_result))

B1 = ttk.Button(GUI, text='คำนวณราคา', command=calc)
B1.pack(ipadx=40, ipady=30)
E1.bind('<Return>', calc)
GUI.mainloop()
