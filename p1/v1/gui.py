from torre_babel import Torre_Babel
from tkinter.filedialog import askopenfilename
from tkinter import *
import copy

class GUI:
    def __init__(self):
        self.inicio={"casilla":-1,"estado":[[1,2,3],[2,1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        self.fin={"casilla":-1,"estado":[[1,2,3],[1,2,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        self.ruta=[]
        self.tb=None
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
        self.crear_init()

        self.frame_final = Frame(self.window,bd=1)
        self.crear_final()

        self.frame_step = Frame(self.window)
        self.crear_step()
        
        self.frame_steps = Frame(self.window)
        self.crear_steps()

        self.b_crear = Button(self.frame_main, text="Crear", command=self.crear)
        self.b_crear.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_crear.place(x=700, y=2, width=98, height=46)

        self.b_archivo = Button(self.frame_main, text="Cargar archivo", command=self.leer_archivo)
        self.b_archivo.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_archivo.place(x=375, y=2, width=98, height=46)

        self.l_x = Label(self.frame_main, text="X:")
        self.l_x.config(bg=self.color_2,fg=self.color_4,font=("Helvetica", 20),anchor=W,justify=LEFT)
        self.l_x.place(x=500, y=2,width=46,height=46)

        self.e_x = Entry(self.frame_main)
        self.e_x.config(bg=self.color_4,fg=self.color_1,font=("Helvetica", 20))
        self.e_x.place(x=550, y=6,width=38,height=38)

        self.l_y = Label(self.frame_main, text="Y:")
        self.l_y.config(bg=self.color_2,fg=self.color_4,font=("Helvetica", 20),anchor=W,justify=LEFT)
        self.l_y.place(x=600, y=6,width=38,height=38)

        self.e_y = Entry(self.frame_main)
        self.e_y.config(bg=self.color_4,fg=self.color_1,font=("Helvetica", 20))
        self.e_y.place(x=650, y=6,width=38,height=38)

        
    def iniciar(self):
        self.window.mainloop()
    def color(self,color):
        if color==1:
            return "#66ff66"
        elif color==2:
            return "#6666ff"
        elif color==3:
            return "#006666"
        elif color==4:
            return "#66f6f6"
        elif color==5:
            return "#060666"
        else:
            return "#ffffff"

    def mostrar_piezas(self,frame,estado,casilla):
        x=110/len(estado[0])
        y=110/len(estado)
        l = Label(frame)
        l.config(bg=self.color(casilla),highlightbackground=self.color_1,relief=GROOVE, bd=2)
        l.place(x=25, y=25+abs(55-y),width=x,height=y)
        for i in range(len(estado)):
            for j in range(len(estado[i])):
                l = Label(frame)
                l.config(bg=self.color(estado[i][j]),highlightbackground=self.color_1,relief=GROOVE, bd=2)
                l.place(x=25+(j*x), y=25+abs(55-y)+y+(i*y),width=x,height=y)
                
        frame.update()
    def leer_archivo(self):
        filename = askopenfilename() 
        f = open(filename)
        data = f.readlines()
        f.close()
        inicio=[]
        final=[]
        cambio= True
        for i in data:

            if i.replace("\n","") == "final" :
                cambio = False
            elif i.replace("\n","") == "init":
                cambio = True
            else:
                if cambio:
                    inicio.append(i.replace("\n","").split(","))
                else:
                    final.append(i.replace("\n","").split(","))
        init=[]
        fin=[]
        for i in range(len(inicio)):
            init.append([])
            fin.append([])
            for j in range(len(inicio[i])):
                init[i].append(int(inicio[i][j]))
                fin[i].append(int(final[i][j]))
        self.inicio["casilla"]=init[0][0]
        self.fin["casilla"]=init[0][0]
        mi=init[1:]
        mf=fin[1:]
        self.inicio["estado"]=mi
        self.fin["estado"]=mf
        self.tb=Torre_Babel()
        
        self.ruta=[]
        self.crear_init()
        self.crear_final()
        self.crear_step()
        self.crear_steps()
        self.e_data.insert(0,self.m_to_text(mi))
        self.mostrar_piezas(self.frame_init,self.inicio.get("estado"),self.inicio.get("casilla"))
        self.mostrar_piezas(self.frame_final,self.fin.get("estado"),self.fin.get("casilla"))
        

    def crear_matriz(self,x,y):
        m=[]
        for i in range(y):
            m.append([]) 
            for j in range(x):
                m[i].append(j+1)
        return m

    def crear_final(self):
        self.frame_final.destroy()

        self.frame_final = Frame(self.window,bd=1)
        self.frame_final.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_final.place( width=250, height=250,x=450, y=75)

        self.b_final = Button(self.frame_final, text="Cambiar", command=self.window.quit)
        self.b_final.config(bg=self.color_6, bd=0,fg=self.color_4)
        self.b_final.place(x=180, y=210, width=68, height=38)

        self.l_final = Label(self.frame_final, text="  Estado Final")
        self.l_final.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_final.place(x=-1, y=-1,width=250,height=25)


    def crear_step(self):
        self.frame_step.destroy()

        self.frame_step = Frame(self.window)
        self.frame_step.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_step.place( width=250, height=250,x=100, y=350)

        self.b_step = Button(self.frame_step, text="resolver", command=self.resolver)
        self.b_step.config(bg=self.color_6,bd=0,fg=self.color_4)
        self.b_step.place(x=180, y=210, width=68, height=38)

        self.l_step = Label(self.frame_step, text="  Paso")
        self.l_step.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_step.place(x=-1, y=-1,width=250,height=25)

    def crear_steps(self):
        self.frame_steps = Frame(self.window)
        self.frame_steps.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_steps.place( width=250, height=250,x=450, y=350)

        s = Scrollbar(self.frame_steps)
        self.L = Listbox(self.frame_steps)
        s.pack(side=RIGHT, fill=Y)
        self.L.place( width=230, height=220,x=0, y=25)
        s['command'] = self.L.yview
        self.L['yscrollcommand'] = s.set
        self.L.bind('<<ListboxSelect>>',self.mostrar_pasos)
        self.l_steps = Label(self.frame_steps, text="  Pasos")
        self.l_steps.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_steps.place(x=-1, y=-1,width=250,height=25)

    def crear_init(self):
        self.frame_init.destroy()
        self.frame_init = Frame(self.window)
        self.frame_init.config(bg=self.color_4,highlightbackground=self.color_1,relief=GROOVE, bd=2)
        self.frame_init.place( width=250, height=250,x=100, y=75)

        self.e_data = Entry(self.frame_init)
        self.e_data.config(bg=self.color_4,fg=self.color_1,font=("Helvetica", 10))
        self.e_data.place(x=0, y=210, width=180, height=38)


        self.b_init = Button(self.frame_init, text="Cargar", command=self.cargar)
        self.b_init.config(bg=self.color_6, bd=0,fg=self.color_4)
        self.b_init.place(x=180, y=210, width=68, height=38)

        self.l_init = Label(self.frame_init, text="  Estado inicial")
        self.l_init.config(bg=self.color_6,fg=self.color_4,font=("Helvetica", 10),anchor=W,justify=LEFT)
        self.l_init.place(x=-1, y=-1,width=250,height=25)

    def cargar(self):
        data=self.e_data.get()
        lineas = data.split(";")
        matriz=[]
        for i in range(len(lineas)):
            matriz.append([])
            for j in lineas[i].split(","):
                matriz[i].append(int(j))
        self.inicio["estado"]=matriz
        self.crear_init()
        self.e_data.insert(0,self.m_to_text(matriz))
        self.mostrar_piezas(self.frame_init,self.inicio.get("estado"),self.inicio.get("casilla"))

    def crear(self):
        self.tb=Torre_Babel()
        self.ruta=[]
        #self.frame_step()
        self.crear_init()
        self.crear_final()
        self.crear_step()
        self.crear_steps()
        x=int(self.e_x.get())
        y=int(self.e_y.get())
        m1=self.crear_matriz(x,y)
        m2=copy.deepcopy(m1)
        m1[1][0]=2
        m1[0][1]=1
        self.inicio["estado"]=m1
        self.fin["estado"]=m2
        self.e_data.insert(0,self.m_to_text(m1))
        self.mostrar_piezas(self.frame_init,self.inicio.get("estado"),self.inicio.get("casilla"))
        self.mostrar_piezas(self.frame_final,self.fin.get("estado"),self.fin.get("casilla"))
    
    def m_to_text(self,m):
        text=""
        for i in range(len(m)):
            for j in range(len(m[i])):
                if len(m[i])-1 == j:
                    text=text+str(m[i][j])
                else:
                    text=text+str(m[i][j])+","
            if len(m)-1 != i:
                text=text+";"
        return text



    def mostrar_pasos(self,evt):
        elemento=int(self.L.get(ACTIVE))
        self.mostrar_piezas(self.frame_step,self.ruta[elemento].get("estado"),self.ruta[elemento].get("casilla"))

    def resolver(self):
        self.ruta=self.tb.iniciar(self.inicio.get("estado"),self.fin.get("estado"))
        for i in range(len(self.ruta)): 
            self.L.insert(i, str(i))