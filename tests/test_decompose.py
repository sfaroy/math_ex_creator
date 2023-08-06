import unittest
from ex_creator.integer_decompose import integer_decompose
class TestDecompose(unittest.TestCase):

    def test_decompose(self):
        decomposed = integer_decompose(20)
        self.assertEqual(tuple(decomposed),(2,2,5))

if __name__ == '__main__':
    unittest.main()