import unittest

from src.Model import NERModel
from src.Prediction import Prediction


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( ('комсомольский', 'проспект'), (res.street, res.street_type))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( ('катукова', 'улица'), (res.street, res.street_type))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('рабочая', 'улица'), (res.street, res.street_type))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('доватора', None), (res.street, res.street_type))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('бехтеева', None), (res.street, res.street_type))

    def test_6(self):
        testing_address = 'улица меркулова дом 24'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('меркулова', 'улица'), (res.street, res.street_type))

    def test_7(self):
        testing_address = 'октябрьская 48 частный дом город сургут'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('октябрьская', None), (res.street, res.street_type))

    def test_8(self):
        testing_address = 'сколько улица 30 лет победы 50 46'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('30 лет победы', 'улица'), (res.street, res.street_type))

    def test_9(self):
        testing_address = 'тюменский тракт 10'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('тюменский', 'тракт'), (res.street, res.street_type))

    def test_10(self):
        testing_address = 'сургут югорская 30/2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('югорская', None), (res.street, res.street_type))

    def test_11(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((None, None), (res.street, res.street_type))

    def test_12(self):
        testing_address = 'старый оскол микрорайон олимпийский дом 23 квартира 105'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('олимпийский', 'микрорайон'), (res.street, res.street_type))

    def test_13(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( ('фармана салманова', 'улица'), (res.street, res.street_type))

    def test_14(self):
        testing_address = 'ты сургут улица 30 лет победы'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( ('30 лет победы', 'улица'), (res.street, res.street_type))

    def test_15(self):
        testing_address = 'проезд мунарева 2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('мунарева', 'проезд'), (res.street, res.street_type))

    def test_16(self):
        testing_address = 'домашний адрес где я живу'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((None, None), (res.street, res.street_type))

    def test_17(self):
        testing_address = 'артема 32 квартира 8'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( ('артема', None), (res.street, res.street_type))

    def test_18(self):
        testing_address = 'знаете знаете у меня дорогая девочка у меня уже все есть и менять из из одного переходить на другой я не хочу поэтому какой город квартира какой ничего я вам сообщать не хочу поэтому до свидания я ничего не'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( (None, None), (res.street, res.street_type))

    def test_19(self):
        testing_address = 'новогиреевская 34'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual( ('новогиреевская', None), (res.street, res.street_type))

    def test_20(self):
        testing_address = 'мое 3 парковая'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('парковая', None), (res.street, res.street_type))

    def test_21(self):
        testing_address = 'москва мусы джалиля 38 корпус 2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('мусы джалиля', None), (res.street, res.street_type))

    def test_22(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('горького', None), (res.street, res.street_type))

    def test_23(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('каширское', 'шоссе'), (res.street, res.street_type))

    def test_24(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('зеленые', 'аллеи'), (res.street, res.street_type))

    def test_25(self):
        testing_address = 'дмитрия ульянова 17 корпус 1 москва'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('дмитрия ульянова', None), (res.street, res.street_type))

    def test_26(self):
        testing_address = 'null'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((None, None), (res.street, res.street_type))

    def test_27(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('алтуфьевское', None), (res.street, res.street_type))

    def test_28(self):
        testing_address = 'маршала захарова дом 12'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('маршала захарова', None), (res.street, res.street_type))

    def test_29(self):
        testing_address = 'а зачем'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual((None, None), (res.street, res.street_type))

    def test_30(self):
        testing_address = 'Кавказский 16'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('Кавказский', None), (res.street, res.street_type))

    def test_31(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('Старый Гай'.lower(), None), (res.street.lower(), res.street_type))

    def test_32(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res: Prediction = self.NERInstance.predictAddress(testing_address)
        self.assertEqual(('зелинского', 'улица'), (res.street, res.street_type))


if __name__ == '__main__':
    unittest.main()
