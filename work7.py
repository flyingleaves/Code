import unittest
import seuif97


class Tend1_test(unittest.TestCase):

    def setUp(self):
        self.data1 = [[3, 300, 
                       0.0010021516796866943, 115.3312730214384, 112.32481798237833,
                       0.39229479240262427, 4.173012184067783, 1507.7392096690312],
                     [80, 300,
                       0.0009711808940216297, 184.14282773425438, 106.44835621252402,
                       0.36856385239848066, 4.010089869646331, 1634.6905431116586],
                      [3, 500, 
                       0.001202418003378339, 975.5422390972251, 971.9349850870901,
                       2.58041912005181, 4.6558068221112086, 1240.7133731017252]]

    def test_Vol(self):
        places = 6
        for item in self.data1:
            self.assertAlmostEqual(seuif97.Volume(item[0], item[1]), item[2],6)

    def test_Entha(self):
        places = 9
        for item in self.data1:
            self.assertAlmostEqual(seuif97.Enthalpy(item[0], item[1]), item[3],9)

    def test_IntEne(self):
        places = 8
        for item in self.data1:
            self.assertAlmostEqual(seuif97.InternalEnergy(item[0], item[1]), item[4],8)

    def test_Entr(self):
        places = 7
        for item in self.data1:
            self.assertEqual(seuif97.Entropy(item[0], item[1]), item[5],7)

    def test_IHC(self):
        places = 9
        for item in self.data1:
            self.assertEqual(seuif97.IHCapacity(item[0], item[1]), item[6],9)

    def test_Sou(self):
        places = 6
        for item in self.data1:
            self.assertEqual(seuif97.Sound(item[0], item[1]), item[7],6)


class Tend2_test(unittest.TestCase):

    def setUp(self):
        self.data2 = [[50, 2000, 690.5721252159439],
                      [100, 2100, 733.9305075450569]]
        self.data3 = [[50, 2400, 735.1848617922307],
                      [100, 2700, 842.046087633262]]

    def test_Bu3a(self):
        for item in self.data2:
            self.assertEqual(seuif97.Buchong_BE3a(item[0], item[1]), item[2])

    def test_Bu3b(self):
        for item in self.data3:
            self.assertEqual(seuif97.buchong_BE3b(item[0], item[1]), item[2])


def suitetext():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Tend1_test))
    suite.addTest(unittest.makeSuite(Tend2_test))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suitetext')