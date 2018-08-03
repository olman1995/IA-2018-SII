
class Torre_Babel:
    estados=[]
    fin=[]
    inicio=[]
    salir=False
    
    def __init__(self):
        self.estado=[]
        self.casilla=-1
        self.sub_estados=[]

    def obtener_copia_estado(self):
        copia=[]
        for i in self.estado:
            copia.append(i[:])
        return copia

    def mover_linea(self,linea,columna,movimiento=1):
        estado=self.obtener_copia_estado()
        casilla=self.casilla
        if movimiento==1:
            valor=estado[linea][len(estado[linea])-1]
            del estado[linea][len(estado[linea])-1]
            estado[linea].insert(0,valor)
        else:
            valor=estado[linea][0]
            del estado[linea][0]
            estado[linea].insert(len(estado[linea]),valor)
        tb = Torre_Babel()
        tb.estado=estado
        tb.casilla=casilla
        return tb

    def mover_columna(self,linea,columna,movimiento=1):
        estado=self.obtener_copia_estado()
        casilla=self.casilla
        if linea==-1 and columna==-1:
            valor=estado[0][0]
            estado[0][0]=casilla
            casilla=valor    
        elif movimiento==1:
            valor=estado[linea][columna]
            estado[linea][columna]=estado[linea-1][columna]
            estado[linea-1][columna]=valor
        else:
            valor=estado[linea][columna]
            estado[linea][columna]=estado[linea+1][columna]
            estado[linea+1][columna]=valor
        
        tb = Torre_Babel()
        tb.estado=estado
        tb.casilla=casilla
        return tb
    
    def iniciar(self,inicio,fin):
        Torre_Babel.inicio=inicio
        Torre_Babel.fin=fin
        self.estado=inicio
        self.solucionar()

    def solucionar(self):
        linea,columna=self.encontrar_espacio()     
        
        if not self.esta_final():
      
            if linea==-1 and columna==-1:
                self.sub_estados.append(self.mover_columna(linea,columna,1))
            else:            
                if linea == 0:
                    self.sub_estados.append(self.mover_linea(linea,columna,1))
                    self.sub_estados.append(self.mover_linea(linea,columna,2))
                    self.sub_estados.append(self.mover_columna(linea,columna,2))
                elif linea == len(self.estado)-1:
                    self.sub_estados.append(self.mover_linea(linea,columna,1))
                    self.sub_estados.append(self.mover_linea(linea,columna,2))
                    self.sub_estados.append(self.mover_columna(linea,columna,1))
                else:
                    self.sub_estados.append(self.mover_linea(linea,columna,1))
                    self.sub_estados.append(self.mover_linea(linea,columna,2))
                    self.sub_estados.append(self.mover_columna(linea,columna,1))
                    self.sub_estados.append(self.mover_columna(linea,columna,2))
        
        if not Torre_Babel.salir:
            for i in self.sub_estados:
                i.solucionar()
                print(self.estado)

    def encontrar_espacio(self):
        x=0
        for i in self.estado:
            y=0
            for j in i:
                if j==-1:
                    return x,y
                y+=1
            x+=1
        return -1,-1

    def esta_final(self):
        valor = True
        if not Torre_Babel.salir:
            for i in range(len(Torre_Babel.fin)):
                for j in range(len(Torre_Babel.fin[i])):
                    if Torre_Babel.fin[i][j] != self.estado[i][j]:
                        valor=False

        Torre_Babel.salir = valor
        return valor

    