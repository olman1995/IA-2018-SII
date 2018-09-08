import copy

class Torre_Babel:
    cerrados=[]
    abiertos=[]
    inicio=[]
    fin=[]
    final=False
    
    def __init__(self):

        self.estado_actual=[]
        self.casilla=-1
        self.sub_estados=[]
        self.valor_heuristico=0
        self.ruta=[]

    def es_fin(self):
        for i in range(len(self.estado_actual)):
            for j in range(len(self.estado_actual[i])):
                if Torre_Babel.fin[i][j] != self.estado_actual[i][j]:
                    Torre_Babel.final=False
                    return False
        Torre_Babel.final=True
        return True

    def agregar_estado_actual(self,estado_actual,casilla):
        self.estado_actual=estado_actual
        self.casilla=casilla
        
    def copia(self):
        copia=[]
        for i in range(len(self.estado_actual)):
            copia.append([])
            for j in self.estado_actual[i]:
                copia[i].append(j)
        return copia

    def casilla_vacia(self):
        for i in range(len(self.estado_actual)):
            for j in range(len(self.estado_actual[i])):
                if self.estado_actual[i][j] == -1:
                    return j,i
        return -1,-1
    
    def t1(self,x,y):
        tb=None
        if(y!=0):
            m=self.copia()
            t=m[y][x]
            m[y][x]=m[y-1][x]
            m[y-1][x]=t
            tb=Torre_Babel()
            tb.agregar_estado_actual(m,self.casilla)
        return tb
    
    def t2(self,x,y):
        tb=None
        if y != (len(self.estado_actual)-1):
            m=self.copia()
            t=m[y][x]
            m[y][x]=m[y+1][x]
            m[y+1][x]=t
            tb=Torre_Babel()
            tb.agregar_estado_actual(m,self.casilla)
        return tb
    
    def t3(self,x,y):
        tb=None
        m=self.copia()
    
        t=m[y][0]
        del m[y][0]
        m[y].append(t)

        tb=Torre_Babel()
        tb.agregar_estado_actual(m,self.casilla)
        return tb
    
    def t4(self,x,y):
        tb=None
        m=self.copia()

        t=m[y][len(m[y])-1]
        del m[y][len(m[y])-1]
        m[y].insert(0,t)  

        tb=Torre_Babel()
        tb.agregar_estado_actual(m,self.casilla)
        return tb
    
    def es_igual(self,m1,m2):
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                if m1[i][j] != m2[i][j]:
                    return False
        return True
    
    def no_esta(self,tb):
        if tb==None:
            return False
        else:
            for i in Torre_Babel.cerrados:
                if self.es_igual(tb.estado_actual,i.estado_actual):
                    return False
            return True

    def calcular_heuristica(self):
        valores_actual=[]
        valores_final=[]
        for i in range(len(self.estado_actual)):
            valores_actual.append([])
            valores_final.append([])
    
        for i in range(len(self.estado_actual)):
            for j in range(len(self.estado_actual[i])):
                if self.estado_actual[i][j] != -1:
                    valores_actual[self.estado_actual[i][j]-1].append([i,j])
                if Torre_Babel.fin[i][j] != -1:
                    valores_final[Torre_Babel.fin[i][j]-1].append([i,j])
        subtotal=[]
        for i in range(len(self.estado_actual[i])):
            
            subtotal.append([])
            for j in valores_actual[i]:
                total=0
                for k in valores_final[i]:
                    total=total+(abs(j[0]-k[0])+abs(j[1]-k[1]))
                subtotal[i].append(total/len(j))
        resultado=[]
        for i in subtotal:
            t=0
            for j in i:
                t=t+j
            resultado.append(t/len(i))
        s=0
        for i in resultado:
            s=s+i
        
        self.valor_heuristico=s/len(resultado)
    
    def A_estrella(self):

        for i in range(50):
        #while not self.es_fin():
            x,y=self.casilla_vacia()
            tb1=self.t1(x,y)
            tb2=self.t2(x,y)
            tb3=self.t3(x,y)
            tb4=self.t4(x,y)
            if self.no_esta(tb1):
                self.sub_estados.append(tb1)
            if self.no_esta(tb2):
                self.sub_estados.append(tb2)
            if self.no_esta(tb3):
                self.sub_estados.append(tb3)
            if self.no_esta(tb4):
                self.sub_estados.append(tb4)

            for i in self.sub_estados:
                i.calcular_heuristica()
                i.ruta=self.ruta[:]
                i.ruta.append(copy.deepcopy(self))
                Torre_Babel.abiertos.append(i)
          
            
            temp=Torre_Babel.abiertos[0]
            for i in Torre_Babel.abiertos:
                if i.valor_heuristico < temp.valor_heuristico:
                    temp=i

            Torre_Babel.abiertos.remove(temp)
            self.estado_actual=temp.estado_actual
            self.casilla=temp.casilla
            self.sub_estados=[]
            self.valor_heuristico=temp.valor_heuristico
            self.ruta=temp.ruta[:]
            Torre_Babel.cerrados.append(temp)


        print("*************   Ruta   *************")
        for i in self.ruta:
            print(i.estado_actual)
        
    def solucionar(self):
        self.A_estrella()

    def iniciar(self,inicio,fin):
        self.estado_actual=inicio
        Torre_Babel.inicio=inicio
        Torre_Babel.fin=fin
        print(self.estado_actual)
        print(self.casilla_vacia())
        print(self.t2(1,0).estado_actual)
        print(self.t3(1,0).estado_actual)
        print(self.t4(1,0).estado_actual)
        #self.t1()
        #self.solucionar()


