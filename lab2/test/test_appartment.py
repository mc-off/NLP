import unittest

from src.Model import NERModel, Prediction


class TestApartment(unittest.TestCase):

    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, '310')

    def test_6(self):
        testing_address = 'Кусковская 19 корпус 1'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)

    def test_7(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)

    def test_8(self):
        testing_address = 'null'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(res.apartment, None)


if __name__ == '__main__':
    unittest.main()
