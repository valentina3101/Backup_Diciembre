    def bfs(self,v): # v:vertice -> [vertice] 
        resultado = []
        cola = []
        while cola != []:
            v = cola.pop()
            for i in vecinos(v):
                if i not in resultado
                    cola.insert(0,i)
                    resultado.append(i)
        return resultado
        
    def dfs(self,v):
        resultado= [v]
        pila = [v]
        while pila != []:
            v = pila.top()
            vecinosnv = []
            for i in vecinos(v):
                if i not in resultado:
                    vecinosnv.append(i)
            if vecinosnv !=[] :
                siguiente = min(vecinosnv)
                resultado.append(siguiente)
                pila.append(siguiente)
            else:
                pila.pop()
        return resultado
