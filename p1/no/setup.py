from torre_babel.torre_babel import Torre_Babel
def main():
    inicio=[[2,3,4,-1],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    fin=[[-1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    tb = Torre_Babel()
    tb.iniciar(inicio,fin)
main()