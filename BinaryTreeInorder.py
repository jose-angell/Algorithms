class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

def recorrido_Inorden(nodo):
    if nodo:
        recorrido_Inorden(nodo.izquierda)
        print(nodo.dato, end=" ")
        recorrido_Inorden(nodo.derecha)


raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

recorrido_Inorden(raiz)
