import unittest

from src.Model import NERModel, Prediction


class TestPersons(unittest.TestCase):

    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'Иванов Петр Васильевич'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'Петр')
        self.assertEqual(res.middle, 'Васильевич')
        self.assertEqual(res.last, 'Иванов')

    def test_2(self):
        testing_address = 'шипицын дмитрий вячеславович'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'дмитрий')
        self.assertEqual(res.middle, 'вячеславович')
        self.assertEqual(res.last, 'шипицын')

    def test_3(self):
        testing_address = 'елена владимировна'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'елена')
        self.assertEqual(res.middle, 'владимировна')
        self.assertEqual(res.last, None)

    def test_4(self):
        testing_address = 'басалаева юлия михайловна'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'юлия')
        self.assertEqual(res.middle, 'михайловна')
        self.assertEqual(res.last, 'басалаева')

    def test_5(self):
        testing_address = 'ну я как раз по фамилии есть смотри мам'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, None)
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, None)

    def test_6(self):
        testing_address = 'глушенков власти на android'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, None)
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, 'глушенков')

    def test_7(self):
        testing_address = 'фамилию сказать что за фамилия терентьева людмила'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'людмила')
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, 'терентьева')

    def test_8(self):
        testing_address = 'елена владимировна'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'елена')
        self.assertEqual(res.middle, 'владимировна')
        self.assertEqual(res.last, None)

    def test_9(self):
        testing_address = 'анюта'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'анюта')
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, None)

    def test_10(self):
        testing_address = 'р1 артем витальевич'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'артем')
        self.assertEqual(res.middle, 'витальевич')
        self.assertEqual(res.last, None)
        
    def test_11(self):
        testing_address = 'фитнес веретельников олег викторович'
        res: Prediction = self.NERInstance.predictPerson(testing_address)
        self.assertEqual(res.first, 'олег')
        self.assertEqual(res.middle, 'викторович')
        self.assertEqual(res.last, 'веретельников')


if __name__ == '__main__':
    unittest.main()

    list_of_persons = ['Иванов Петр Васильевич']
    list_of_persons = list_of_persons + """елена владимировна
        близнюк федор александрович
        или долги арсен арамович передал бьянка карина арсеновна элиза gardiyan анжела арсеновна я не помню
        шипицын дмитрий вячеславович
        армения
        какая именно
        дорогая наталья евгеньевна
        только одно не могу понять мельникова
        юрьев владимир иванович юрист владимир иванович я вам говорю иванович
        я же вам сказал сейчас
        на захаренко наталья леонидовна
        nissan мосин синицин василий николаевич
        тупой я вообще ребенок звони сейчас сброшу
        а меня хамидов азамат пулатович
        сколько будет сколько тихомирова
        а я не помню теперь спокойно новоярково светлана николаевна
        болдырева анастасия александровна
        леоненко сергей васильевич
        клепиков александр николаевич
        хорошо дела багратян нормальных шаевич
        до свидания мазитов владимир
        сальников дмитрий владимирович
        необязательно
        так якимова екатерина владимировна
        терминов артем игоревич
        напольный марина владимировна
        белоусов сергей алексеевич
        не поет понял у вас
        кристина валерьевна
        фамилия анатольевич
        карта хабалка виталик одном фунте
        давайте надо я вообще не пользоваться сим картой в основном ладно
        ковалева мария александровна
        ларионова галина владимировна
        на ульянова николай наверх ну я думаю на ульянова николая
        соловьев евгений александрович
        а я и не помню женская он оформлен на меня
        на ленина 1 моя sim карта
        дома ой давайте попрощаемся у меня не понимаете
        калинин андрей юрьевич
        грешно максим владимирович
        тютин александр валентинович
        на кого наверное алексей викторович
        чем отказаться чукурова фаины
        галина аркадьевна
        ну там трибунал денис я сейчас вопрос телефон у меня давайте я домой приду он как там можно там будет потом
        0 тимур и анализ
        школьник нина викторовна
        ну я не знаю
        а где твой заехали звоните es2 вы должны знать
        янков илья петрович
        ну я не знаю радоваться вчера об этом говорить останется жива
        что сейчас нужно сделать вообще то то я покупала симку для ребенка наверное на меня если честно не помню федорова эльвира
        я сказал виталий иванович
        погода котовск треповского александра григорьева
        ну вы по идее это все должны это знать
        дмитрий николаевич
        либо до выдавали бучельникова ирина анатольевна аспарт меня поэтому скажу
        поспелов никита владиславович
        кавалеров алексей юрьевич
        а я не знаю кого анастан или это я не помню
        3 нефедова наталья алексеевна
        125 руб в месяц ирина михайловна шевелева
        я подумаю хорошо
        марченков сергей валентинович
        давыдова елена петровна
        быкова елена леонидовна
        королев на 31
        беспалова елена сергеевна
        давайте я вам перезвоню приду номер я сейчас занят
        вот надо
        патенты надежда юрьевна
        тернополь владимировна черный холодильник
        кабакова валентина ивановна
        рузавина михалевич
        ананьев николай сергеевич
        фармакотерапия петровна
        буду знать мне позвони саня не буду ничего делать
        бардакова татьяна анатольевна
        ну если перезвонишь туда
        ишак валерьевна
        я не знаю там у меня оформляли в магазине именно
        на просто старая я не знаю
        я не помню надо мне на ольгу николаевну
        что для этого нужно когда щенкам полина иванова
        шиян татьяна петровна
        людмила александровна тищенко людмила александровна
        алина алина рудольфовна
        палатки сплав владимир
        титулы жанна петровна
        хулиганка ульяна сергеевна
        надо доплачивать а я не заплачу редковский сергей георгиевич
        ой оценка кристина геннадьевна
        амбарцумян артур арсенович
        забрать роман олегович
        гаврилова татьяна анатольевна
        шаляпина валентина анатольевна
        мне нужно деньги положить да на сейчас маханько александр владимирович
        а сейчас он так сейчас секундочку ратов сергей валентинович
        ахметшин ренат
        оксана анатольевна блокада
        карманчик максим николаевич
        лук
        почему валиде
        авито это симка на меня вот никита федорович
        я посмотрю информацию более подробное когда узнали что
        разговаривать и некогда позвонить алексеев александр николаевич
        новый на меня на кабанов юрий леонидович
        юдина татьяна ивановна
        кудряшова марина владимировна
        бунин игорь александрович
        хорошо я я позвоню
        русаков артем тарасович
        но там еще заиграев николай васильевич
        копылов максим борисович
        блогер татьяна яковлевна
        чебыкин викторович
        поговорила беляев сергей валерьевич
        светлана толстая безопасности перезвоните пожалуйста насчет раз посмотрим
        не нравишься приходи
        иванова елена анатольевна
        коков юрий юрьевич
        спасибо большое по моему просвирнин анатолий анатольевич если я правильно помню
        жкх александр петрович
        михална старикова наталья михайловна
        воронцов сергей викторович
        языка в любовь александровна
        я не помню сейчас
        по моему на маму плотникова
        ронда назад конечно кошатника василий иванович вы сейчас мне его переключить еда
        нет она меня сказала валерий петрович
        геворгян каринэ самвеловна
        вы прикалываетесь что ли объясняю
        черенков андрей викторович
        рубанов федор александрович
        куценко сергей петрович
        ничего нам не надо от нас по моему она меня чабанова
        лисина надежда николаевна
        татьяна александрович
        герасим татьяна ивановна
        графова елена борисовна
        потапова ирина викторовна потапова ирина викторовна
        головин сергей витальевич
        степанов василий михайлович
        денис широких юрьевич
        атланова евгения петровна
        сколько скинуть сервис шахмарданов многих низамович
        хайбулаев михаил андреевич
        степан станислав николаевич
        я хочу я хочу я хочу это попробовать у меня две sim карты 1 sim карта на булат веруклин равно sim карта на моего мужа галкова сергея алексеевича
        казань я не знаю не помню
        ладно
        борисов михаил александрович
        135 руб виктор валерьевич
        вчера я на работе я на работе я на работе help me пожалуйста я на работе вечером
        изменить наталья викторовна
        калинина маргарита александровна
        сарай ульяновск
        зайцев переулке славы
        наталья леонидовна капранова
        ну или ну или на меня не давайте этот иванович
        нам еще на девичьей фамилии пигорева наталья александровна и не помню переделывала нет
        я дома я же сказала я не знаю
        карта запломбирована айлин опять александровна она забыла
        кофта марина александровна
        ульяна черникова татьяна
        бачурина елена анатольевна
        ну хорошо по поводу николай николаевич
        салон полина логунова
        согласен бойко александрович
        ирина милана викторовна
        выглядеть
        я вот не знаю у меня надеюсь наверное фамилию полякова юлия александровна или моисеенкова
        касьянов владимир григорьевич
        ольга николаевна
        марчук иван анатольевич
        да ну когда оформляли давно пользуюсь это из родителей либо она виктор александрович николаевич
        финансовые средства в хорошем качестве анна васильевна
        владимирова светлана владимировна
        у меня фамилия усольцева ксения яковлевна я
        белова татьяна николаевна
        шевцова елена григорьевна
        позвонить спросить
        айсуру наталья
        татьяна собираться
        салахова гузалия талгатовна
        зеленскому зеленская мария васильевна
        белянин александр александрович вроде бы белянин александр александрович по моему
        ермачков сергей николаевич
        тележка в магазине советчик
        досвидос привет
        иммуно любовь викторовна
        у меня вроде сейчас шучу как дамирович
        спасибо данильченко
        русин николай владимирович
        вывоз анатолий александрович
        алексеев николай филиппович
        когтева алена александровна
        герасименко игорь васильевич
        чудаева наталья ивановна
        овсянников кирилл евгеньевич
        вот я не помню или архипова александра ивановна или или на меня архипов алексей
        а я с роботом разговариваю с человеком
        евсеева оксана алексеевна
        евгений игоревич
        решетников максим геннадьевич
        воронин константин владимирович
        эйхвальд анна владимировна
        левченко владимир александрович
        лдс
        фитнес веретельников олег викторович
        mos ru лилия маликовна
        долгополов юрий николаевич
        надеждинская алло
        алина алина можешь на меня и даже не помню но потапова оксана викторовна по моему так
        инженер нефтяник желаю что
        андрей андреевич
        бокалом надежда викторовна если ошибаюсь
        погода новоалександровск
        спасибо малыгина
        а в гости михайловна вроде бы
        так подожди подождите подождите подождите минутку у меня нет гигабайта мне не нужны мне нужен телефон 3 разговоров в месяц все на все
        анисимова анисимова анна анисимова наталья сергеевна
        sim карта на меня анисимов александр 10
        бурлакова людмила владимировна
        кузнецова валентина александровна
        если вы перезвоните тоже смогу
        очень как доеду сейчас но наверное на меня долганова лидия константиновна
        здравствуй вадим олегович
        продал наталья алексеевна
        я снова что сказал до 12 00 наталье
        брянский юрий николаевич
        арюткин максим иванович
        попов игорь борисович
        но она и на меня оформлена слабой русю николаевич
        на меня решетникова ирина владимировна
        25 руб в месяц есть петрова екатерина анатольевна
        ой у нас наверное михайловна я точно не помню это рабочий телефон
        как она может быть оформлена если она куплена на улице
        не умею ветеркова зинаида
        sim карта оформленного кравченко наталья васильевна
        versace елена сергеевна
        виктор васильевич болотов
        владимир евгеньевич
        colossians
        малышкин александр зорич
        эхо сергей александрович
        смирнова светлана сергеевна
        о а вот это уже проблема просто у меня спички него склад 10 я не знаю что нашло сергей николаевич или чернышева ксения анатольевна
        бухтиярова геннадьевна
        брунька вадим викторович
        ты другой с россиянами все
        у меня на меня туйчиев от хадижа мирзоевич гражданин россия пожалуйста давайте
        ульяна николаевна
        не помнящих корзину асановна
        данил андрей васильевич
        я могу в tele2 пойти и там это все обсудить
        мою фамилию прокофьевна
        исмаилов
        никулина анна владимировна
        медведева надежда ивановна
        николаенко наталья михайловна
        ну я буду кабакова елена юрьевна
        бирюков сергей игоревич
        а если я не ошибаюсь лопатина анастасия александровна
        анализ на вич александр емельянович
        что алена михайловна
        архипова
        москаленко елена владимировна
        на тебя хабибуллина регина суреновна
        белый было николаевна
        михаил любовь алексеевна
        масленникова анастасия владимировна
        большой котик павел константинович
        ящик радченко лариса валентиновна
        volkswagen дорофеев алексей сергеевич
        информация по телефону не дам смогу
        вот который больше сильно
        р1 артем витальевич
        делали сильно
        карта тверь юлия владимировна юлия владимировна
        сообщение
        демина юлия валерьевна
        владимир lanos
        звонок павел николаевич
        а кольцов николай
        зубов максим петрович
        асташкина ивановна
        затворов евгений сергеевич
        youtube
        давайте а я вот не помню шепелев михаил борисович
        евгения александровна
        вакула ирина александровна
        это нисколько нагло период времени
        на меня оформили стоит замена александр дмитриевич
        мухаммад как много я же на какой по какому
        тураев кушать хасанович
        ну удовенко наталья васильевна
        мокрушина светлана анатольевна
        анюта
        сергеев александр арсентьевич
        волкова анна викторовна
        я не нашего виталий витальевич
        план валерьевич
        алло уедет либо екатерина валерьевна байкова страница 11
        попиченко артем евгеньевич
        да макушина ольга владимировна
        да конечно классический поменяла по моему тариф
        крючок михайловна была
        новые тарифы рязань чуканова надежда владимировна
        дементьев александр геннадьевич
        согласна забалуев вячеслав николаевич
        а если на александра борисовна
        наконечники михайловна
        пузанков александр сергеевич
        телефон телефон использовать
        скачкова ирина валерьевна
        фамилию сказать что за фамилия терентьева людмила
        новиков александр юрьевич
        моисеев александр викторович
        вартанян анна кашинская
        плотникова наталья ефимовна
        носова наталья михайловна
        шляхов евгений викторович
        юрок марина александровна
        горюнов сергей александрович артем александрович
        одинцовский район
        степанов павел анатольевич
        белоцерковский алексей витальевич
        ананина меня записана а наверное меня не
        шерл анастасия сергеевна
        сборник английский
        у меня речник андрей владимирович
        ребенкова
        хостелы владимир владимирович
        монах дмитриевич
        попов виктор михайлович
        машина виталий анатольевич
        ой это я не знаю наверное моисеева ольга николаевна
        никольский александр леонидович
        рыжов евгений викторович
        тимошин александр александрович
        солдатова елена степановна что не ли
        на меня оформлена кубическая карина юрьевна
        карта умывайся пашкевич андрей олегович
        так это на силантьева или васильева не помню точно на кого то одна на двоих
        да меня картошки марина ивановна
        багров юрий николаевич
        константин леонидович не так
        филиппова елена алексеевна
        спасибо кашель елена геннадьевна
        мне удобнее будет если подойти к салону
        ну так коля это tele2 это же моя карта да
        по моему снимать анастасия павловна
        буланцев николай николаевич
        деткино нина анатольевна
        рукавишников андрей александрович
        басалаева юлия михайловна
        ну я как раз по фамилии есть смотри мам
        а афонино афонино афонина татьяна борисовна
        самохин алексей николаевич
        моторин евгений павлович
        кто на лебедева мария валерьевна
        голимбиевский николай юрьевич
        августинович ринатович
        глушенков власти на android
        хитарьян артем артурович
        юрий владимирович саратов
        так попова диана ивановна
        вроде зимина анна герман
        буду спасибо ты меня оставил сергеевич
        лукашов андрей иванович
        а я не помню""".splitlines()
