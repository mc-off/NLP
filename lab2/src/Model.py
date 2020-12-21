import re
import string

from yargy import Parser

from src.Prediction import Prediction
from src.rules.address.address import ADDRESS
from src.rules.name.name import NAME


class NERModel:

    @staticmethod
    def predictPerson(text):
        parser = Parser(NAME)
        matches = [match for match in parser.findall(text)]
        facts = [_.fact.as_json for _ in matches]
        if len(facts) == 0:
            return Prediction()
        return Prediction(**facts[0])

    @staticmethod
    def predictAddress(text):
        parser = Parser(ADDRESS)
        matches = [match for match in parser.findall(text)]
        facts = [_.fact.as_json for _ in matches]
        if len(facts) == 0:
            return Prediction()

        return Prediction(**facts[0])
