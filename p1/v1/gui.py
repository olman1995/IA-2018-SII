from tkinter import *
class GUI:
    def __init__(self):
        self.window = Tk()
        self.color_1="#000000"
        self.color_2="#222222"
        self.color_3="#F9F9F9"
        self.color_4="#FFFFFF"
        self.color_5="#9D9D9D"
        self.color_6="#7C7CAD"
        self.color_7="#C6C6C6"
        self.window.title("Torre de babel")
        self.window.geometry('800x625+25+25')
        self.frame_main = Frame(self.window)
        self.frame_main.config(bg=self.color_3)
        self.frame_main.place( width=800, height=625,x=0, y=0)
        self.label = Label(self.frame_main, text="  Torre de babel")
        self.label.config(bg=self.color_2,fg=self.color_4,font=("Helvetica", 20),anchor=W,justify=LEFT)
        self.label.place(x=0, y=0,width=800,height=50)
        
        self.frame_init = Frame(self.window)
        self.frame_init.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_init.place( width=250, height=250,x=100, y=75)

        self.frame_final = Frame(self.window,bd=1)
        self.frame_final.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_final.place( width=250, height=250,x=450, y=75)

        self.frame_step = Frame(self.window)
        self.frame_step.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_step.place( width=250, height=250,x=100, y=350)
        
        self.frame_steps = Frame(self.window)
        self.frame_steps.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_steps.place( width=250, height=250,x=450, y=350)

        self.b_init = Button(self.frame_init, text="Save", command=self.init)
        self.b_init.config(bg=self.color_6, bd=0,fg=self.color_4)
        self.b_init.place(x=200, y=200, width=46, height=46)

        self.b_final = Button(self.frame_final, text="Save", command=self.window.quit)
        self.b_final.config(bg=self.color_6, bd=0,fg=self.color_4)
        self.b_final.place(x=200, y=200, width=46, height=46)

        self.b_step = Button(self.frame_step, text="Save", command=self.window.quit)
        self.b_step.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_step.place(x=200, y=200, width=46, height=46)

        self.l_init = Label(self.frame_init, text="  Estado inicial")
        self.l_init.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_init.place(x=-1, y=-1,width=250,height=25)

        self.l_final = Label(self.frame_final, text="  Estado Final")
        self.l_final.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_final.place(x=-1, y=-1,width=250,height=25)

        self.l_step = Label(self.frame_step, text="  Paso")
        self.l_step.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_step.place(x=-1, y=-1,width=250,height=25)

        self.l_steps = Label(self.frame_steps, text="  Pasos")
        self.l_steps.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_steps.place(x=-1, y=-1,width=250,height=25)

    def iniciar(self):
        self.window.mainloop()
    
    def init(self):
        print("hola mundo")