# Author = Shulai Roman Yurievich
# Group = P3115
# Date = 18.10.2025

# 501595 % 3 = 1

import re

test0 = (2, """
Футбольный клуб «Реал Мадрид» является 15-кратным обладателем главного
футбольного европейского трофея – Лиги Чемпионов. Данный турнир организован
Союзом европейских футбольных ассоциаций (УЕФА). Идея о континентальном
футбольном турнире пришла к журналисту Габриэлю Ано в 1955 году.
""")

test1 = (5, """
Этот замечательный тест проверит запустится ли замечательный код
""")

test2 = (2, """
Прилагательные удивительная часть речи с удивительным количеством слов, значений, с помощью них
можно передать удивительные красоты нашего мира
""")

test3 = (1, """
Красивый сад и красивый дом стояли на красивом холме. Красивая картина открывалась с красивой вершины.
""")

test4 = (4, """
Старый дуб и старая береза росли у старого пруда. Старые ветви склонялись к старым водам.
""")

test5 = (6, """
Большой город, большие улицы и большое движение создавали большую суету. Большие здания теснились в большом пространстве.
""")

test6 = (1, """
Такой большой, но таКие маленький и такая больших
""")

tests = [test0, test1, test2, test3, test4, test5, test6]

def main():
    for test in tests:
        print(changeAdjectivesForms(test[0], test[1]))
        print()

def changeAdjectivesForms(number, text):
    adjEnding = r"(ий|ый|его|ого|ему|ому|им|ым|ем|ом|ая|яя|ей|ой|ую|юю|ое|ее|ых|ые|ыми|ие|их|ими)"

    # ищем слова с окончаниями прилагательных
    adjPattern = rf"\b([А-ЯЁ]?[а-яё]+){adjEnding}\b"
    adjectives = re.findall(adjPattern, text)
    wordBases = [x[0].lower() for x in adjectives]

    # выбираем основу, которая встречается макс кол-во раз
    commonBase = max(wordBases, key=lambda x: wordBases.count(x))
    if wordBases.count(commonBase) == 1:
        return "Ошибка ввода, нет повторяющихся слов"
    
    # оставляем только самые часто встречаемые прилагательные
    adjectives = [x for x in adjectives if x[0].lower() == commonBase]

    # запоминаем окончание нужного вхождения
    if number-1 > len(adjectives):
        return "Ошибка ввода, мало повторяющихся слов"
    newForm = adjectives[number-1][1]
   
    # меняем вхождения с маленькой буквы
    changedText = re.sub(rf"\b({commonBase}){adjEnding}\b", rf"\1{newForm}", text)

    # меняем вхождения с заглавной буквы
    changedText = re.sub(rf"\b({commonBase[0].upper()+commonBase[1:]}){adjEnding}\b", rf"\1{newForm}", changedText)

    return changedText


if __name__ == "__main__":
    main()