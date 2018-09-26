from torre_babel import Torre_Babel
from tkinter import *
import random

class GUI:
    def __init__(self):
        self.inicio={"casilla":-1,"estado":[[2,5,3,4,1],[1,3,5,4,2],[1,2,3,4,5],[3,3,4,4,1],[2,1,5,2,5]],"heuristico":0,"costo":0,"ruta":[]}
        self.fin={"casilla":-1,"estado":[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],"heuristico":0,"costo":0,"ruta":[]}
        self.ruta=[]
        self.tb=Torre_Babel()
        self.window = Tk()
        self.color_1="#000000"
        self.color_2="#222222"
        self.color_3="#F9F9F9"
        self.color_4="#FFFFFF"
        self.color_5="#9D9D9D"
        self.color_6="#7C7CAD"
        self.color_7="#C6C6C6"
        self.window.title("Torre de babel")
        self.window.geometry('1000x650')
        self.frame_main = Frame(self.window)
        self.frame_main.config(bg=self.color_3)
        self.frame_main.place( width=1000, height=650,x=0, y=0)
        self.label = Label(self.frame_main, text="  Torre de babel")
        self.label.config(bg=self.color_2,fg=self.color_4,font=("Helvetica", 20),anchor=W,justify=LEFT)
        self.label.place(x=0, y=0,width=1000,height=50)

        self.l_tamanno = Label(self.frame_main, text="Tamaño: ")
        self.l_tamanno.config(bg="white", bd=0,fg="black",font=("Helvetica", 14))
        self.l_tamanno.place(x=40, y=100)
        
        self.e_tamanno = Entry(self.frame_main)
        self.e_tamanno.config(bg="white", bd=0,fg="black",font=("Helvetica", 14))
        self.e_tamanno.place(x=120, y=100,width=50,height=30)

        self.l_conf = Label(self.frame_main, text="Configuración: ")
        self.l_conf.config(bg="white", bd=0,fg="black",font=("Helvetica", 14))
        self.l_conf.place(x=40, y=150)

        self.e_conf = Entry(self.frame_main)
        self.e_conf.config(bg="white", bd=0,fg="black",font=("Helvetica", 14))
        self.e_conf.place(x=170, y=150,width=100,height=30)
        
        self.frame_init = Frame(self.window)
        self.frame_init.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_init.place( width=250, height=250,x=360, y=75)

        self.frame_final = Frame(self.window,bd=1)
        self.frame_final.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_final.place( width=250, height=250,x=700, y=75)

        self.frame_step = Frame(self.window)
        self.frame_step.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_step.place( width=250, height=250,x=360, y=350)
        
        self.frame_steps = Frame(self.window)
        self.frame_steps.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_steps.place( width=250, height=250,x=700, y=350)

        s = Scrollbar(self.frame_steps)
        self.L = Listbox(self.frame_steps)
        s.pack(side=RIGHT, fill=Y)
        self.L.place( width=230, height=220,x=0, y=25)
        s['command'] = self.L.yview
        self.L['yscrollcommand'] = s.set
        self.L.bind('<<ListboxSelect>>',self.mostrar_pasos)


        self.b_init = Button(self.frame_init, text="Save", command=self.resolver)
        self.b_init.config(bg=self.color_6, bd=0,fg=self.color_4)
        self.b_init.place(x=200, y=200, width=46, height=46)

        self.b_final = Button(self.frame_final, text="Save", command=self.window.quit)
        self.b_final.config(bg=self.color_6, bd=0,fg=self.color_4)
        self.b_final.place(x=200, y=200, width=46, height=46)

        self.b_step = Button(self.frame_step, text="resolver", command=self.resolver)
        self.b_step.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_step.place(x=180, y=210, width=68, height=38)

        self.b_crear = Button(self.frame_main, text="Crear", command=self.crear)
        self.b_crear.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_crear.place(x=800, y=2, width=98, height=46)

        self.b_cargar = Button(self.frame_main, text="Cargar archivo", command=self.crear)
        self.b_cargar.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_cargar.place(x=900, y=2, width=98, height=46)

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


    def color(self,color):
        if color==1:
            return "violet"
        elif color==2:
            return "green"
        elif color==3:
            return "red"
        elif color==4:
            return "orange"
        elif color==5:
            return "purple"
        elif color==6:
            return "blue"
        elif color==7:
            return "gray"
        elif color==8:
            return "pale green"
        elif color==9:
            return "gold"
        elif color==10:
            return "aqua"
        elif color==11:
            return "pink"
        elif color==12:
            return "snow"
        elif color==13:
            return "blanched almond"
        elif color==14:
            return "navajo white"
        elif color==15:
            return "light slate gray"
        elif color==16:
            return "slate blue"
        elif color==17:
            return "dark turquoise"
        elif color==18:
            return "dark olive green"
        elif color==19:
            return "black"
        else:
            return "lime green" 

        

    def mostrar_piezas(self,frame,estado,casilla):
        x=125/len(estado)
        y=125/len(estado[0])
        l = Label(frame)
        l.config(bg=self.color(casilla),highlightbackground=self.color_1,relief=GROOVE, bd=2)
        l.place(x=25, y=50,width=x,height=y)
        for i in range(len(estado)):
            for j in range(len(estado[i])):
                l = Label(frame)
                l.config(bg=self.color(estado[i][j]),highlightbackground=self.color_1,relief=GROOVE, bd=2)
                l.place(x=25+(j*x), y=50+y+(i*y),width=x,height=y)
            
                
        frame.update()

    def matriz_trans(self,mat):
        matriz=[[]]
        c=0
        x=0
        while c<len(mat):
            while x<len(mat):
                matriz[c]+=[mat[x][c]]
                x+=1
            if len(matriz)<len(mat):
                matriz+=[[]]
            c+=1
            x=0
        return matriz

    def matriz_final_vertical(self):
        matriz=[[]]
        c=0
        x=1
        while c<int(self.e_tamanno.get()):
            while x<=int(self.e_tamanno.get()):
                matriz[c]+=[x]
                x+=1
            if len(matriz)<int(self.e_tamanno.get()):
                matriz+=[[]]
            c+=1
            x=1
        return matriz

    def matriz_inicial_vertical(self):
        matriz=[[]]
        c=0
        x=1
        while c<int(self.e_tamanno.get()):
            while x<=int(self.e_tamanno.get()):
                n=random.randint(0, int(self.e_tamanno.get()))
                while n in matriz[c]:
                    n=random.randint(0, int(self.e_tamanno.get()))
                matriz[c]+=[n]
                x+=1
            if len(matriz)<int(self.e_tamanno.get()):
                matriz+=[[]]
            c+=1
            x=1
        return matriz
        
    def crear(self):
        #self.frame_step()
        conf=self.e_conf.get()
        if conf=="vertical":
            self.mat_ini=self.matriz_inicial_vertical()
            self.mat_estado_final=self.matriz_final_vertical()
        else:
            self.mat_ini=self.matriz_inicial_vertical()
            self.mat_ini=self.matriz_trans(self.mat_ini)
            self.mat_estado_final=self.matriz_final_vertical()
            self.mat_estado_final=self.matriz_trans(self.mat_estado_final)
        self.mostrar_piezas(self.frame_init,self.mat_ini,self.inicio.get("casilla"))
        self.mostrar_piezas(self.frame_final,self.mat_estado_final,self.fin.get("casilla"))
        
    def mostrar_pasos(self,evt):
        elemento=int(self.L.get(ACTIVE))
        self.mostrar_piezas(self.frame_step,self.ruta[elemento].get("estado"),self.ruta[elemento].get("casilla"))

    def resolver(self):
        self.ruta=self.tb.iniciar(self.mat_ini,self.mat_estado_final)
        for i in range(len(self.ruta)): 
            self.L.insert(i, str(i))

    
