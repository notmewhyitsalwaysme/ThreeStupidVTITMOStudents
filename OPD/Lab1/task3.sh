cd ~/lab0

cp boldore5 camerupt0/happinyboldore

cat poochyena5/spoink camerupt0/happiny>boldore5_26
# ошибка: cat: poochyena5/spoink: Отказано в доступе
# выдадим право на чтение poochyena5/spoink
chmod u+r poochyena5/spoink
cat poochyena5/spoink camerupt0/happiny>boldore5_26


cp -r camerupt0/. poochyena5/drapion
# ошибка: cp: невозможно получить доступ к 'camerupt0': Отказано в доступе
# выдадим право на чтение camerupt0
chmod u+r camerupt0
cp -r camerupt0/. poochyena5/drapion
# ошибка: cp: невозможно открыть 'camerupt0/spheal' для чтения: Отказано в доступе
# выдадим право на чтение camerupt0/spheal
chmod u+r camerupt0/spheal
# добавим атрибут -n чтобы игнорировать сообщения о перезаписи
cp -rn camerupt0/. poochyena5/drapion

ln boldore5 camerupt0/sphealboldore 

ln -s ~/lab0/ducklett1 camerupt0/sphealducklett

ln -s ~/lab0/poochyena5 Copy_58

cp ducklett1 camerupt0/toxicroak
# ошибка: cp: невозможно создать обычный файл 'camerupt0/toxicroak/ducklett1': Отказано в доступе
# выдадим право на запись в каталоге camerupt0/toxicroak
chmod u+w camerupt0/toxicroak
cp ducklett1 camerupt0/toxicroak

# у каталога pichu9/voltorb отсутствует право на чтение, добавим его
# chmod u+r pichu9/voltorb
# покажем дерево каталогов
# ls -lRi

# возвращаем все права на место

# chmod u-r poochyena5/spoink
# chmod u-r poochyena5 poochyena5/drapion
# chmod u-r poochyena5/drapion/camerupt0
# chmod u-r camerupt0
# chmod u-r camerupt0/spheal
# chmod u-w camerupt0/toxicroak
