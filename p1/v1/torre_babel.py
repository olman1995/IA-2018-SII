import copy

class Torre_Babel:
    
    def __init__(self):    
        self.cerrados=[]
        self.abiertos=[]
        self.inicio=[]
        self.fin=[]
        self.estado_actual={"casilla":-1,"estado":[],"heuristico":0,"costo":0,"ruta":[]}
        
    def es_igual(self,m1,m2):
        for i in range(len(m1)):
            if m1[i] != m2[i]:
                return False
        return True
        
    def copia(self):
        copia=[]
        for i in range(len(self.estado_actual.get("estado"))):
            copia.append([])
            for j in self.estado_actual["estado"][i]:
                copia[i].append(j)
        return copia

    def casilla_vacia(self):
        for i in range(len(self.estado_actual.get("estado"))):
            for j in range(len(self.estado_actual.get("estado")[i])):
                if self.estado_actual.get("estado")[i][j] == -1:
                    return j,i
        return -1,-1

    def buscar(self,m,n):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == n:
                    return j,i
        return -1,-1
    
    def t1(self,x,y):
        sub_estado=None
        if(y!=0):
            m=self.copia()
            t=m[y][x]
            m[y][x]=m[y-1][x]
            m[y-1][x]=t
            sub_estado= {"casilla":self.estado_actual.get("casilla"),
                    "estado":m,
                    "heuristico":0,
                    "costo":0,
                    "ruta":[]}
        return sub_estado
    
    def t2(self,x,y):
        sub_estado=None
        if y != (len(self.estado_actual["estado"])-1):
            m=self.copia()
            t=m[y][x]
            m[y][x]=m[y+1][x]
            m[y+1][x]=t
            sub_estado= {"casilla":self.estado_actual.get("casilla"),
                    "estado":m,
                    "heuristico":0,
                    "costo":0,
                    "ruta":[]}
        return sub_estado

    def t3(self,x,y):
        sub_estado=None
        m=self.copia()
        t=m[y][0]
        del m[y][0]
        m[y].append(t)
        sub_estado= {"casilla":self.estado_actual.get("casilla"),
                    "estado":m,
                    "heuristico":0,
                    "costo":0,
                    "ruta":[]}
        return sub_estado

    def t4(self,x,y):
        sub_estado=None
        m=self.copia()
        t=m[y][len(m[y])-1]
        del m[y][len(m[y])-1]
        m[y].insert(0,t)  
        sub_estado= {"casilla":self.estado_actual.get("casilla"),
                    "estado":m,
                    "heuristico":0,
                    "costo":0,
                    "ruta":[]}
        return sub_estado
    
    def no_esta(self,tb):
        if tb==None:
            return False
        else:
            for i in self.cerrados:
                if self.es_igual(tb.get("estado"),i.get("estado")):
                    return False
            for i in self.abiertos:
                if self.es_igual(tb.get("estado"),i.get("estado")):
                    return False
            return True

    def calcular_heuristica(self,estado):
        valores_actual=[]
        valores_final=[]
        for i in range(len(estado[1])):
            valores_actual.append([])
            valores_final.append([])
        for i in range(len(estado)):
            for j in range(len(estado[i])):
                if estado[i][j] != -1:
                    valores_actual[estado[i][j]-1].append([i,j])
                if self.fin[i][j] != -1:
                    valores_final[self.fin[i][j]-1].append([i,j])
        subtotal=[]
        for i in range(len(estado[i])):
            subtotal.append(0)
            for j in valores_actual[i]:
                r=0
                for k in valores_final[i]:
                    r=r+(abs(j[0]-k[0])+abs(j[1]-k[1]))
                subtotal[i]=subtotal[i]+(r/len(j))
        del valores_actual
        del valores_final
        total=(sum(subtotal)/len(subtotal))
        return total
    
    def A_estrella(self):
        #for w in range(100):
        while not self.es_igual(self.estado_actual.get("estado"),self.fin):
            x,y=self.casilla_vacia()
            tb1=self.t1(x,y)
            tb2=self.t2(x,y)
            tb3=self.t3(x,y)
            tb4=self.t4(x,y)
            estados=[]
            if self.no_esta(tb1):
                estados.append(tb1)
                tb1["costo"]=self.estado_actual.get("costo")+1
            if self.no_esta(tb2):
                estados.append(tb2)
                tb2["costo"]=self.estado_actual.get("costo")+1
            if self.no_esta(tb3):
                estados.append(tb3)
                tb3["costo"]=self.estado_actual.get("costo")+1
            if self.no_esta(tb4):
                estados.append(tb4)
                tb4["costo"]=self.estado_actual.get("costo")+1

            for i in estados:
                h=self.calcular_heuristica(i.get("estado"))
                i["heuristico"]=h
                i["ruta"]=self.estado_actual.get("ruta")[:]
                i["ruta"].append(copy.deepcopy(self.estado_actual))
                self.abiertos.append(i)
            del estados
            temp=self.abiertos[0]
            for i in self.abiertos:
                if i.get("costo")+i.get("heuristico") < temp.get("costo")+temp.get("heuristico"):
                    temp=i
            self.abiertos.remove(temp)
            self.estado_actual["estado"]=temp["estado"]
            self.estado_actual["casilla"]=temp["casilla"]
            self.estado_actual["heuristico"]=temp["heuristico"]
            self.estado_actual["ruta"]=temp["ruta"][:]
            self.estado_actual["costo"]=temp["costo"]
            self.cerrados.append(temp)
        self.estado_actual["ruta"].append(self.estado_actual)
        return self.estado_actual["ruta"]
        
    def solucionar(self):
        p=[]
        self.inicio
        x,y=self.buscar(self.inicio,self.fin[0][0])
        if x==0 and y==0:
            print("hola")
        else:
            p.append({"casilla":-1,"estado":self.copia(),"heuristico":0,"costo":0,"ruta":[]})
            i=self.copia()
            f=self.copia()
            c=i[0][0]
            i[0][0]=-1
            f[0][0]=-1
            z=i[0][1]
            i[0][1]=i[y][x]
            i[y][x]=z
            tb=Torre_Babel()
            p+=tb.resolver(f,i,c)
            es=copy.deepcopy(p[len(p)-1])
            es["ruta"]=[]
            es["estado"][0][0]=es["casilla"]
            es["casilla"]=-1
            p.append(es)
            self.estado_actual=es
            s=self.t3(0,0)
            p.append(copy.deepcopy(s))                    
            s["casilla"]=s["estado"][0][0]
            s["estado"][0][0]=-1
            p.append(s)
            self.estado_actual=copy.deepcopy(s)
        self.fin[0][0]=-1

        p+=self.A_estrella()
        es=copy.deepcopy(p[len(p)-1])
        for i in p:
            print(i.get("estado"))
        es["estado"][0][0]=es["casilla"]
        es["casilla"]=-1
        p.append(es)
        return p

    def resolver(self,inicio,fin,casilla):
        self.estado_actual["estado"]=inicio
        self.estado_actual["casilla"]=casilla
        self.inicio=inicio
        self.fin=fin
        return self.A_estrella()

    def iniciar(self,inicio,fin):
        self.estado_actual["estado"]=inicio
        self.inicio=inicio
        self.fin=fin
        return self.solucionar()
