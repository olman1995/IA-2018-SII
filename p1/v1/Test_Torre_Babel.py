import unittest
from torre_babel import Torre_Babel
#python -m unittest Test_Torre_Babel
class Test_Torre_Babel(unittest.TestCase):

    def test_0(self):
        print("test de la clase torre babel")

    def test_1(self):
        print("test 1: Movimiento abajo")
        tb=Torre_Babel()
        tb.estado_actual={"casilla":-1,"estado":[[1,2,3],[2,-1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        tb.fin=[[1,2,3],[1,2,3],[1,2,3]]
        print(tb.t1(1,1))
       
    def test_2(self):
        print("test 2: Movimiento arriba")
        tb=Torre_Babel()
        tb.estado_actual={"casilla":-1,"estado":[[1,2,3],[2,-1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        tb.fin=[[1,2,3],[1,2,3],[1,2,3]]
        print(tb.t2(1,1))
       
    def test_3(self):
        print("test 3: Movimiento derecha")
        tb=Torre_Babel()
        tb.estado_actual={"casilla":-1,"estado":[[1,2,3],[2,-1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        tb.fin=[[1,2,3],[1,2,3],[1,2,3]]
        print(tb.t3(1,1))

    def test_4(self):
        print("test 4: izquierda")
        tb=Torre_Babel()
        tb.estado_actual={"casilla":-1,"estado":[[1,2,3],[2,-1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        tb.fin=[[1,2,3],[1,2,3],[1,2,3]]
        print(tb.t4(1,1))
       
    def test_5(self):
        print("test 5: es igual")
        tb=Torre_Babel()
        retorno=tb.es_igual([[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]])
        self.assertTrue(retorno)
        retorno=tb.es_igual([[2,3,1],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]])
        self.assertFalse(retorno)

    def test_6(self):
        print("test 6: copia")
        tb=Torre_Babel()
        tb.estado_actual={"casilla":-1,"estado":[[1,2,3],[2,-1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        estado=tb.copia()
        retorno=tb.es_igual([[1,2,3],[2,-1,3],[1,2,3]],estado)
        self.assertTrue(retorno)

    def test_7(self):
        print("test 7: casilla vacia")
        tb=Torre_Babel()
        tb.estado_actual={"casilla":-1,"estado":[[1,2,3],[2,-1,3],[1,2,3]],"heuristico":0,"costo":0,"ruta":[]}
        casilla=tb.casilla_vacia()
        print(casilla)

    def test_8(self):
        print("test 8: calcular heuristica")
        tb=Torre_Babel()
        tb.fin=[[-1,2,3],[1,2,3],[1,2,3]]
        print(tb.calcular_heuristica([[3,2,1],[3,2,-1],[3,2,1]]))   
        print(tb.calcular_heuristica([[1,2,3],[2,-1,3],[1,2,3]]))        
        print(tb.calcular_heuristica([[1,2,3],[-1,2,3],[1,2,3]])) 
        
        
if __name__ == '__main__':
    unittest.main()