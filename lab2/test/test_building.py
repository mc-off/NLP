import unittest

from src.Model import NERModel
from src.Prediction import Prediction


class TestHome(unittest.TestCase):

    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('50', None))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 а'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('36 а', None))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('31а', None))


    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('18', None))

    def test_5(self):
        testing_address = 'ну бехтеева 9/2 квартира 310'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('9/2', None))

    def test_6(self):
        testing_address = 'артема 32 квартира 8'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('32', None))

    def test_7(self):
        testing_address = 'город липецк полиграфическая дом 4'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('4', None))

    def test_8(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('55', '1'))

    def test_9(self):
        testing_address = 'люберцы октябрьский проспект 10 корпус 1'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('10', '1'))

    def test_10(self):
        testing_address = 'бульвар миттова 24'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('24', None))

    def test_11(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((res.house, res.corpus), ('78', None))


if __name__ == '__main__':
    unittest.main()
