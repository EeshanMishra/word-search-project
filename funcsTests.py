# Project 3
# Name: Eeshan Mishra
# Instructor: S. Einakian
# Section: 05


import unittest
from funcs import*


class TestCases(unittest.TestCase):
    def test_word_forward(self):
        self.assertEqual(word_forward('UNIX', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (True, '(FORWARD) ', 9, 3))
        self.assertEqual(word_forward('SLO', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (True, '(FORWARD) ', 7, 2))
        self.assertEqual(word_forward('COMPILE', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (False, 'NOT FOUND', 'A', 'A'))

    def test_word_up(self):
        self.assertEqual(word_up('COMPILE', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (True, '(UP) ', 6, 8))
        self.assertEqual(word_up('CHICKEN', ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']), (True, '(UP) ', 8, 8))
        self.assertEqual(word_up('SLO', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (False, 'NOT FOUND', 'A', 'A'))

    def test_word_backward(self):
        self.assertEqual(word_backward('VIM', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (True, '(BACKWARD) ', 1, 4))
        self.assertEqual(word_backward('BEAR', ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']), (True, '(BACKWARD) ', 1, 6))
        self.assertEqual(word_backward('UNIX', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (False, 'NOT FOUND', 'A', 'A'))

    def test_word_down(self):
        self.assertEqual(word_down('CALPOLY', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (True, '(DOWN) ', 1, 0))
        self.assertEqual(word_down('RABBIT', ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']), (True, '(DOWN) ', 1, 3))
        self.assertEqual(word_down('COMPILE', ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), (False, 'NOT FOUND', 'A', 'A'))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
