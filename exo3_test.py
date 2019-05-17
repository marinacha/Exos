import unittest
import exo3_code as ex3


class Exercice3_TestCase(unittest.TestCase):

    def setUp(self):
        self.widget = (ex3.Exercice_3(1))

    def test_aire(self):
        self.assertEqual(self.widget.aire(), 3.141592653589793)

    def test_perimetre(self):
        self.assertEqual(self.widget.perimetre(), 6.283185307179586)

    def test_dans_cercle(self):
        self.assertEqual(self.widget.dans_cercle(0.1, 0.5), True)


if __name__ == '__main__':
    unittest.main()