from tkinter import *
from tkinter import ttk # theme of tk เป็นmoduleของtkinter
from tkinter import messagebox

GUI = Tk() #นี้คือจอหลังของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี้คือชื่อของโปรแกรม
GUI.geometry('600x600') #ขนาดของโปรแกรม

#L1 = Label(GUI,text='โปรแกรมบันทึก',font('Angsana New'),fg='Blue')
B1 = ttk.Button(GUI,text='เงินมีเท่าไหร') #มาจาก*
B1.pack(ipadx=20,ipady=20)

#FB1 = labelFrame(GUI) #คล้ายกระดาน
#FB1.place(x=50,y=50)



#B2 = ttk.Button(GUI,text ='เงินมีอยู่กี่บาท') #มาจาก*
#B2.pack(ipadx=20,ipdy=20)
#B2.place(x=50,y=50)

B3 = ttk.Button(GUI,text='เงินมีเท่าไหร') #มาจาก*
B3.place(x=50,y=50)

#def  button2(): #ชื่อbuttonจะเปลี่ยนเป็นอะไรก็ได้
#    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
 #    messagebox.shoinfo('เงินในบัญชี',text)




GUI.mainloop()
