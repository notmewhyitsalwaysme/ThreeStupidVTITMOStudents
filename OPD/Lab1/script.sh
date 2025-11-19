mkdir ~/lab0
cd ~/lab0

touch boldore5 ducklett1 hypno5
mkdir camerupt0 pichu9 poochyena5

cd camerupt0
touch happiny spheal carvanha goldeen sunflora
mkdir toxicroak

cd ../pichu9
touch snorlax nuzleaf
mkdir voltorb

cd ../poochyena5
touch spoink
mkdir finneon drapion

cd ..

echo -e "Возможности  Overland=3 Jump=1 Power=4 Intelligence=4\nSinker=0">>boldore5
echo "Живет  Grassland Urban">>camerupt0/happiny
echo -e "Тип покемона  ICE\nWATER">>camerupt0/spheal
echo -e "Способности  Bite Leer Rage Focus Energy Scary Face\nIce Fang Screech Swagger Assurance Crunch Aqua Jet Agility Take\nDown">>camerupt0/carvanha
echo -e "Живет  Freshwater">>camerupt0/goldeen
echo -e "Ходы  After You Double-Edge\nEarth Power Endeavor Giga Drain Helping Hand Pound Seed Bomb Snore\nSynthesis Uproar Worry Seed">>camerupt0/sunflora
echo -e "Способности  Water Gun Water\nSport Defog Wing Attack Water Pulse Aerial Ace Bubblebeam Featherdance\nHurricane">>ducklett1
echo "Развитые способности  Inner Focus">>hypno5
echo -e "Тип\nпокемона  NORMAL NONE">>pichu9/snorlax
echo -e "Способности  Harden Growth Nature Power\nFake Out Torment Faint Attack Razor Wind Swagger\nExtrasensory">>pichu9/nuzleaf
echo "Развитые способности  Gluttony">>poochyena5/spoink

cd ~/lab0

chmod u=rw,g=w,o=r boldore5

chmod u=wx,g=wx,o=wx camerupt0
chmod 440 camerupt0/happiny
chmod u-rwx,g=r,o=r camerupt0/spheal
chmod 666 camerupt0/carvanha
chmod u=rw,g-rwx,o=r camerupt0/goldeen
chmod u=r,g=r,o-rwx camerupt0/sunflora
chmod u=rx,g=x,o=w camerupt0/toxicroak

chmod 444 ducklett1
chmod u=r,g=r,o-rwx hypno5

chmod 770 pichu9
chmod u-rwx,g=r,o=r pichu9/snorlax
chmod u=wx,g=rwx,o=wx pichu9/voltorb
chmod u=rw,g=w,o=r pichu9/nuzleaf

chmod 305 poochyena5
chmod u=rx,g=w,o=r poochyena5/finneon
chmod u-rwx,g-rwx,o=rw poochyena5/spoink
chmod 355 poochyena5/drapion

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

cd ~/lab0


echo "Подсчитать количество строк содержимого файлов: carvanha, goldeen, sunflora, snorlax, nuzleaf, результат записать в файл в директории /tmp, ошибки доступа перенаправить в файл в директории /tmp"
wc -l camerupt0/carvanha camerupt0/goldeen camerupt0/sunflora pichu9/snorlax pichu9/nuzleaf >>/tmp/out 2>>/tmp/err
echo "Вывод:"
cat /tmp/out
echo "Ошибки"
cat /tmp/err

echo ""

# для псевдорекурсии:
shopt -s globstar


echo "Вывести четыре первых элемента рекурсивного списка имен и атрибутов файлов в директории lab0, список отсортировать по убыванию размера, подавить вывод ошибок доступа"

ls -lS **/* 2>/dev/null | head -4
# -S сортирует по размеру, **/* - рекурсия, 2>/dev/null - подавление ошибок

echo ""

echo "Рекурсивно вывести содержимое файлов с номерами строк из директории lab0, имя которых заканчивается на '5', строки отсортировать по имени a->z, ошибки доступа не подавлять и не перенаправлять"

cat -n **/*5 | sort -k 2 

echo ""

echo "Вывести список имен файлов в директории camerupt0, список отсортировать по имени a->z, ошибки доступа не подавлять и не перенаправлять"
# -p добавляет к имени каталога /, конвейром перенаправляем в grep, -v инвертирует поиск, то есть все с / не будут отображены (останутся только файлы), 
# ls по умолчанию сортирует по имени, поэтому sort не нужен
# но будет ошибка(((: ls: невозможно открыть каталог 'camerupt0': Отказано в доступе
# можно выдать право на чтение camerupt0 и всё заработает
chmod u+r camerupt0
ls -p camerupt0 | grep -v "/$"
chmod u-r camerupt0

echo ""

echo "Вывести три первых элемента рекурсивного списка имен и атрибутов файлов в директории lab0, начинающихся на символ 'd', список отсортировать по возрастанию даты доступа к файлу, подавить вывод ошибок доступа"

ls -utrl **/d* 2>/dev/null | head -3
# -utr сортирует по дате доступа(от меньшего к большему), **/d* - рекурсивный вывод с d в начале

echo ""

echo "Вывести рекурсивно список имен и атрибутов файлов в директории lab0, содержащих строку "ha", список отсортировать по имени z->a, подавить вывод ошибок доступа"
# ls по умолчанию сортирует a->z, ключ -r инвертирует сортировку(теперь z->a), **/*ha* - рекурсивный поиск строки "ha"
# 2>/dev/null подавление ошибок доступа

chmod u+r camerupt0
ls -lr **/*ha* 2>/dev/null
chmod u-r camerupt0

cd ~/lab0

rm -r boldore5 

rm -r camerupt0/carvanha 

rm -r camerupt0/sphealduckle* 
# ошибка: no matches found: camerupt0/sphealduckle*
# выдадим camerupt0 право на чтение
chmod u+r camerupt0
rm -r camerupt0/sphealduckle* 

rm -r camerupt0/sphealboldo* 

# файл pichu9/snorlax защищен от записи, поэтому используем опцию -f
rm -rf pichu9
# получаем ошибку rm: pichu9/voltorb: Недостаточно привилегий.
# pichu9/voltorb не имеет права на чтение и при этом это пустая директория, можно воспользоваться rmdir
rmdir pichu9/voltorb
rm -r pichu9

# camerupt0/toxicroak зищищен от записи, исправим это
chmod u+w camerupt0/toxicroak
# файл camerupt0/toxicroak/ducklett1 защищен от записи, поэтому используем опцию -f
rm -rf camerupt0/toxicroak
