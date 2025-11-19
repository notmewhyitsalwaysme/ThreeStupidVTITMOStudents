# Author = Shulai Roman Yurievich
# Group = P3115
# Date = 18.10.2025

# 501595 % 3 = 1

# Проблема того решение в том, что некоторые слова с окончаниями или частями окончаниями похожих
# на окончания прилагательных не различаются, напишем решение с библиотекой PyMorphy2
from Informatics_Lab3_Task3 import tests
import re
from pymorphy2 import MorphAnalyzer

def main():
    for test in tests:
        print(changeAdjectivesForms(test[0], test[1]))
        print()

def changeAdjectivesForms(number, text):
    adjEnding = r"(ий|ый|его|ого|ему|ому|им|ым|ем|ом|ая|яя|ей|ой|ую|юю|ое|ее|ых|ые|ыми|ие|их|ими)"

    # ищем слова с окончаниями прилагательных
    adjPattern = rf"\b([А-ЯЁ]?[а-яё]+){adjEnding}\b"
    words = re.findall(adjPattern, text)

    # отбираем только прилагательные
    adjectives = []
    morph = MorphAnalyzer()
    for word in words:
        s = word[0] + word[1]
        part = morph.parse(s)[0]
        if part.tag.POS == "ADJF":
            adjectives += [word]

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