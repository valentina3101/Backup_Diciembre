import unittest
from selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    
    def test_listaVacia(self):
        self.assertEqual([],selection_sort([]))
   
    def test_unElemento(self):
        self.assertEqual([5],selection_sort([5]))
     
    def test_dosElementosOrdenados(self):
        self.assertEqual([2,3],selection_sort([2,3]))
     
    def test_dosElementosDesordenados(self):
        self.assertEqual([4,5],selection_sort([5,4]))
    
    def test_MasDeDosElementosDesordenados(self):
        self.assertEqual([1,2,3,4,5,6],selection_sort([3,4,6,1,5,2]))

    def est_variosElementosOrdenados(self):
        self.assertEqual([1,2,3,4,5,6],selection_sort([1,2,3,4,5,6]))
    
    def test_conCaracteres(self):
        self.assertEqual(["a","b","c","d","e"],selection_sort(["b","c","d","a","e"]))

    def test_tuplas(self):
        self.assertEqual([("a",1),("b",4)],selection_sort([("b",4),("a",1)]))

if __name__=='__main__':
    unittest.main()

