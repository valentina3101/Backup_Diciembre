import unittest
from insercion_sort import insercion_sort

class TestInsercionSort(unittest.TestCase):
    
    def test_listaVacia(self):
        self.assertEqual([],insercion_sort([]))
   
    def test_unElemento(self):
        self.assertEqual([3],insercion_sort([3]))
     
    def test_dosElementosOrdenados(self):
        self.assertEqual([1,2],insercion_sort([1,2]))
     
    def test_dosElementosDesordenados(self):
        self.assertEqual([1,2],insercion_sort([2,1]))
    
    def test_conMasDeDosElementos(self):
        self.assertEqual([1,2,3,4,5,6],insercion_sort([3,4,6,1,5,2]))
    
    def test_casoEspecialCaracteres(self):
        self.assertEqual(["a","b","c","d","e"],insercion_sort(["b","c","d","a","e"]))

    def test_tuplas(self):
        self.assertEqual(
            [("a",1),("b",4)],
            insercion_sort([("b",4),("a",1)]))

if __name__=='__main__':
    unittest.main()
