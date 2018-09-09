import collections
from torre_babel import Torre_Babel
from gui import GUI
def main():
    #print("*************   Torre de babel   *************")
    inicio=[[1,2,3,4],[2,1,3,4],[2,3,-1,4]]
    fin=[[-1,2,3,4],[1,2,3,4],[1,2,3,4]]
    tb=Torre_Babel()
    #g = GUI()
    #g.iniciar()
    tb.iniciar(inicio,fin)

main()
