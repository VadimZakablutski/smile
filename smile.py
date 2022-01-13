from tkinter import *
def kontroll():
    lbl.configure(text=v.get())
    if v.get()==1:
        print("esmaspäev")
    elif v.get()==2:
        print("teisipäev")
tk = Tk() 
c = Canvas(tk, width=300, height=300, bg="white") 
c.create_oval((0,0,90,90))
c.create_oval((25,20,35,30))
c.create_oval((50,20,60,30))
c.create_arc((20,40,70,70))
c.create_arc((20,70,70,70), style=CHORD, start=0, extent=150)
c.create_arc((0, 180, 0,0),style=ARC)
c.pack()
tk.mainloop()
