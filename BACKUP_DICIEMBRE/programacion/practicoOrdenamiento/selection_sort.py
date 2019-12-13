def selection_sort (array):    
    i = 0    # contador del paso
  
    while i < len(array) :
        j = i + 1
        pos_min = i # pos_min es mi candidato a ser el menor elemento 
        while j < len(array): # mientras j sea  menor que el largo de la lista
            if array[j] < array[pos_min]: #  si el elmento(j) es menor que el elemento(pos_min) que yo pensaba que era menor
                pos_min = j
            j += 1
# ahora estoy seguro de que mi pos_min es el elemento menor
            
        tmp= array[i] # se hace intercambio
        array[i] = array[pos_min]
        array[pos_min] = tmp 
        i += 1 #para terminar el while
        
    return array

a= selection_sort([3,2,1,14,3,6,8,10,45,67]*100)
#print (array)

        
