from yargy import Parser, rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.relations import gnc_relation
from yargy.predicates import gram, is_capitalized, type, caseless, eq, custom, normalized, length_eq
from yargy.tokenizer import Tokenizer


def is_excep(value):
    return_value = value
    if value == 'по':
        return_value = None
    return return_value


Name = fact(
    'Name',
    ['first', 'last', 'middle']
)

NAME = gram('Name')
SURN = gram('Surn')
PATR = gram('Patr')

FIRST = NAME.interpretation(Name.first)
LAST = SURN.interpretation(Name.last.custom(is_excep))
MIDDLE = PATR.interpretation(Name.middle)

FIRST_LAST = rule(FIRST, LAST)
LAST_FIRST = rule(LAST, FIRST)

FIRST_MIDDLE = rule(FIRST, MIDDLE)
FIRST_MIDDLE_LAST = rule(FIRST, MIDDLE, LAST)
LAST_FIRST_MIDDLE = rule(LAST, FIRST, MIDDLE)

SINGLE_FIRST = FIRST
SINGLE_LAST = LAST
SINGLE_MIDDLE = MIDDLE

NAME = or_(
    LAST_FIRST_MIDDLE,
    FIRST_MIDDLE_LAST,
    FIRST_MIDDLE,
    FIRST_LAST,
    LAST_FIRST,

    SINGLE_LAST,
    SINGLE_MIDDLE,
    SINGLE_FIRST
).interpretation(Name)
