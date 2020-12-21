from yargy import rule, and_, not_, or_
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.predicates import normalized, gram, eq, type, in_, length_eq

ABBR = gram('Abbr')
ADJF = gram('ADJF')
ANIM = gram('anim')
APRO = gram('Apro')
NOUN = gram('NOUN')
GEOX = gram('Geox')
SURN = gram('Surn')
NAME = gram('Name')
GENT = gram('gent')
PLUR = gram('plur')
INT = type('INT')
RU = type('RU')
SLASH = eq('/')

Address = fact(
    'AddressInformation',
    ['city', 'city_type', 'street', 'street_type', 'house', 'house_type', 'corpus', 'corpus_type', 'building',
     'building_type', 'apartment', 'apartment_type']
)

CITY_TYPE = or_(
    rule(eq('город')),
).interpretation(Address.city_type)

CITY_WORD = or_(
    rule(morph_pipeline(['санкт-петербург'])),
    rule(
        and_(
            ADJF,
            not_(APRO)
        ).optional(),
        GEOX
    )
).interpretation(Address.city)

CITY = or_(
    rule(CITY_TYPE, CITY_WORD),
    CITY_WORD
)

street_type_pipeline = morph_pipeline([
    'аллеи', 'бульвар', 'микрорайон', 'переулок',
    'проезд', 'проспект', 'тракт', 'улица', 'шоссе'
])

STREET_TYPE = or_(
    rule(street_type_pipeline)
).interpretation(Address.street_type)

STREET_WORD = or_(
    # маршала Жукова, мусы Джаиля
    rule(
        and_(
            NOUN, ANIM
        ),
        or_(SURN, NAME)
    ),
    # героя труда Егорова
    rule(
        and_(
            NOUN, ANIM
        ),
        and_(
            NOUN, GENT
        ),
        SURN
    ),
    # малый арбат, арбат, тверской тракт
    rule(
        ADJF.optional(),
        or_(
            and_(
                not_(APRO),
                ADJF
            ),
            GEOX,
            SURN,
            NAME
        ),
        and_(
            NOUN,
            not_(in_(street_type_pipeline))
        ).optional()
    ),
    # проспект Героев
    rule(
        and_(
            NOUN, GENT, PLUR
        )
    ),
    # 30 лет победы
    rule(
        INT,
        NOUN.optional(),
        and_(
            or_(
                and_(
                    not_(APRO),
                    ADJF
                ),
                NOUN,
            ),
            not_(
                or_(
                    GEOX,
                    SURN,
                    NAME
                )
            )
        )
    ),
    # чисто рул для N почтового отделения
    rule(
        INT,
        and_(
            ADJF,
            not_(APRO)
        ),
        and_(
            or_(
                and_(
                    not_(APRO),
                    ADJF
                ),
                NOUN,
            ),
            not_(
                or_(
                    GEOX,
                    SURN,
                    NAME
                )
            )
        )
    ),
    # улица фармана салманова
    rule(
        NAME,
        SURN
    ),
    # улица имени меня (артема)
    rule(
        NAME,
    ),

).interpretation(Address.street)

STREET = or_(
    rule(STREET_TYPE, STREET_WORD),
    # для случаев с типом сзади
    rule(STREET_WORD, STREET_TYPE),
    STREET_WORD
)

HOUSE_TYPE = or_(
    # дом дом дом
    rule(normalized('дом'), normalized('дом'), normalized('дом')),
    rule(normalized('дом')),
).interpretation(Address.house_type)

HOUSE_WORD = or_(
    rule(
        # плюс номер
        eq('номер').optional(),
        or_(
            rule(
                INT,
                or_(
                    and_(
                        ABBR,
                        length_eq(1)
                    ),
                    and_(
                        RU,
                        length_eq(1),
                    )
                ).optional()
            ).interpretation(Address.house),
            # вот это прям спорно, но ок, для случаев по типу 9/2
            rule(
                INT,
                SLASH,
                INT
            ).interpretation(Address.house)
        )
    )
)

HOUSE = or_(
    rule(HOUSE_TYPE, HOUSE_WORD),
    HOUSE_WORD
)

CORPUS_TYPE = or_(
    rule(normalized('корпус')),
    rule(normalized('к')),
).interpretation(Address.corpus_type)

CORPUS_WORD = rule(
    INT
).interpretation(Address.corpus)

CORPUS = or_(
    rule(CORPUS_TYPE, CORPUS_WORD),
    CORPUS_WORD
)

BUILDING_TYPE = or_(
    rule(normalized('строение')),
    rule(normalized('ст')),
).interpretation(Address.building_type)

BUILDING_WORD = rule(
    INT
).interpretation(Address.building)

BUILDING = or_(
    rule(BUILDING_TYPE, BUILDING_WORD),
    BUILDING_WORD
)

APARTMENT_TYPE = or_(
    rule(normalized('квартира')),
    rule(normalized('кв')),
).interpretation(Address.apartment_type)

APARTMENT_WORD = rule(
    INT
).interpretation(Address.apartment)

APARTMENT = or_(
    rule(APARTMENT_TYPE, APARTMENT_WORD),
    APARTMENT_WORD
)

ADDRESS = or_(
    rule(CITY, STREET, HOUSE, CORPUS),
    rule(STREET, CITY, HOUSE, CORPUS, APARTMENT),
    rule(STREET, CITY, HOUSE, BUILDING, APARTMENT),
    rule(STREET, CITY, HOUSE, APARTMENT),
    rule(STREET, CITY, HOUSE, CORPUS),
    rule(STREET, CITY, HOUSE, BUILDING),
    rule(STREET, CITY, HOUSE),
    rule(STREET, HOUSE, CORPUS, APARTMENT, CITY),
    rule(STREET, HOUSE, BUILDING, APARTMENT, CITY),
    rule(STREET, HOUSE, APARTMENT, CITY),
    rule(STREET, HOUSE, CORPUS, CITY),
    rule(STREET, HOUSE, BUILDING, CITY),
    rule(STREET, HOUSE, CITY),
    rule(STREET, CITY),
    rule(STREET, HOUSE, CORPUS, APARTMENT),
    rule(STREET, HOUSE, BUILDING, APARTMENT),
    rule(STREET, HOUSE, APARTMENT),
    rule(STREET, HOUSE, CORPUS),
    rule(STREET, HOUSE, BUILDING),
    rule(STREET, HOUSE),
    rule(HOUSE, APARTMENT, STREET),
    rule(STREET_TYPE, STREET_WORD),
    rule(CITY, STREET, HOUSE, CORPUS, APARTMENT),
    rule(CITY, STREET, HOUSE, BUILDING, APARTMENT),
    rule(CITY, STREET, HOUSE, APARTMENT),
    rule(CITY, STREET, HOUSE, BUILDING),
    rule(CITY, STREET, HOUSE),
    rule(CITY, STREET),
    rule(CITY),
    rule(HOUSE, STREET, CITY),
    rule(HOUSE, STREET),
).interpretation(Address)
