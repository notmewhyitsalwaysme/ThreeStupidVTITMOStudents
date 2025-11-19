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
