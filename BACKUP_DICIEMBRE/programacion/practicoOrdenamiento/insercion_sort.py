def insercion_sort (array):
        
    i = 1    # contador del paso 
#inicializa en la segunda posicion de la lista
  
    while i < len(array) : #se hace una vez por cada posicion
        j = i 
        while j > 0: # mientras j sea mayor a 0
            #print ("comparando:", array[j-1] , "con" , array[j])
            if array[j-1] > array[j]: # si el elemento de la lista en posicion [j-1]  sea mayor al elmento de la lista en la posicion [j] 
               #print ("deberia intercambiar" ,array[j], "con", array[j-1])
                # hace intercambio
                tmp= array[j] 
                array[j] = array[j-1]
                array[j-1] = tmp 
            j -= 1
        i += 1 #para terminar el while
    return array


#a= list(reversed(range(7000)))
#import random
#b=[random.randint(0,1000)for _ in range(9000)]
c=list(range(9000))



