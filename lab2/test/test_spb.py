import unittest

from src.Model import NERModel
from src.Prediction import Prediction


class TestStreet(unittest.TestCase):

    def setUp(self):
        self.NERInstance = NERModel()

    def test_shkolnaya(self):
        testing_address = 'санкт-петербург школьная 20'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('санкт-петербург', None), (res.city, res.city_type))
        self.assertEqual(('школьная', None), (res.street, res.street_type))
        self.assertEqual(('20', None, None), (res.house, res.corpus, res.building))

    def test_full_gagarina(self):
        testing_address = 'санкт-петербург юрия гагарина 22 к2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('санкт-петербург', None), (res.city, res.city_type))
        self.assertEqual(('юрия гагарина', None), (res.street, res.street_type))
        self.assertEqual(('22', '2', None), (res.house, res.corpus, res.building))

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('гагарина', None), (res.street, res.street_type))
        self.assertEqual(('22', '2', None), (res.house, res.corpus, res.building))

    def test_untolovsky(self):
        testing_address = "санкт-петербург юнтоловский 43 корпус 1"
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('санкт-петербург', None), (res.city, res.city_type))
        self.assertEqual(('юнтоловский', None), (res.street, res.street_type))
        self.assertEqual(('43', '1', None), (res.house, res.corpus, res.building))

    def test_untolovsky_str(self):
        testing_address = "санкт-петербург юнтоловский 43 строение 1"
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('санкт-петербург', None), (res.city, res.city_type))
        self.assertEqual(('юнтоловский', None), (res.street, res.street_type))
        self.assertEqual(('43',  None, '1'), (res.house, res.corpus, res.building))

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('юнтоловский', None), (res.street, res.street_type))
        self.assertEqual(('43',  None, '1'), (res.house, res.corpus, res.building))
