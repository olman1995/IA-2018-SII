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
        if x != 0:
            t=m[y][x]
            m[y][x]=m[y][x-1]
            m[y][x-1]=t
        else:
            t=m[y][x]
            m[y][x]=m[y][len(self.estado_actual[y])-1]
            m[y][len(self.estado_actual[y])-1]=t
        tb=Torre_Babel()
        tb.agregar_estado_actual(m,self.casilla)
        return tb
    
    def t4(self,x,y):
        tb=None
        m=self.copia()
        if x != (len(self.estado_actual[y])-1):
            t=m[y][x]
            m[y][x]=m[y][x+1]
            m[y][x+1]=t
        else:
            t=m[y][x]
            m[y][x]=m[y][0]
            m[y][0]=t
            
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
        self.valor_heuristico=self.valor_heuristico+1
    
    def solucionar_1(self):
        if(not Torre_Babel.final):
            self.es_fin()
        Torre_Babel.cerrados.append(self)

        if(Torre_Babel.final):
            print("Estado final")
        else:
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
                print(i.estado_actual)
                i.solucionar_1()
            
    def solucionar_2(self):

        for i in range(250):
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
                if i.valor_heuristico > temp.valor_heuristico:
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
        
    def solucionar(self,tipo=1):
        if tipo==1:
            self.solucionar_1()
        else:
            self.solucionar_2()
            
    def iniciar(self,inicio,fin):
        self.estado_actual=inicio
        Torre_Babel.inicio=inicio
        Torre_Babel.fin=fin
        self.solucionar(2)

def main():
    print("*************   Torre de babel   *************")
    inicio=[[3,-1,2],[1,2,3],[1,2,3]]
    fin=[[-1,2,3],[1,2,3],[1,2,3]]
    tb=Torre_Babel()
    tb.iniciar(inicio,fin)

main()
