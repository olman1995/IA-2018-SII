import collections
from torre_babel import Torre_Babel
from gui import GUI
def main():
    #print("*************   Torre de babel   *************")
    inicio=[[1,2,3],[2,1,3],[2,3,-1]]
    fin=[[-1,2,3],[1,2,3],[1,2,3]]
    tb=Torre_Babel()
    #g = GUI()
    #g.iniciar()
    tb.iniciar(inicio,fin)

main()
