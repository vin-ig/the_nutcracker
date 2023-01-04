## "Щелкунчик и мышиный король" на Python
***Задача***: перевести отрывок из одноименной сказки с человеческого языка на Python
___
### Запуск проекта
```git clone https://github.com/vin-ig/the_nutcracker.git```  # склонировать репозиторий на 
локальную машину и перейти в директорию с проектом

```python -m venv venv```  # установить виртуальное окружение

```venv/sripts/activate.ps1``` / ```source venv/bin/activate```  # активировать виртуальное окружение (Win / Mac)

```pip install -r requirements.txt```  # установить зависимости

```python main.py```  # запустить исполняемый файл
___
### Структура проекта
**dataclasses_.py** - описаны датаклассы и классы перечислений

**exceptions.py** - описаны пользовательские ошибки

**main.py** - исполняемый файл, содержится основной текст перевода

**objects.py** - описаны классы объектов (персонажей)
___
### Отрывок для перевода
"Едва в столице распространился слух о возвращении Дроссельмейера с астрономом, как тотчас же 
были сделаны необходимые приготовления, и оба путешественника, явившиеся ко двору с привезенными 
ими лекарством, нашли там множество желающих попробовать раскусить орех и вылечить принцессу, 
среди них было даже несколько принцев.

Оба с немалым испугом увидели принцессу вновь. Ее маленькое тело с крошечными, тощими ручонками
едва держало огромную, уродливую голову. Безобразие ее лица еще более увеличилась из-за белой, 
точно нитяной, бороды, которой обросли ее губы и подбородок.

Дальше все произошло именно так, как предсказал по гороскопу звездочет. Молокососы в башмаках
один за другим напрасно пытались разгрызть орех, но только переломали себе зубы и испортили челюсти,
а принцессе ничуть не полегчало. Каждый, кого выносили, был почти без памяти; зубные врачи только
приговаривали:

— Ну! Вот так орех!

Наконец, когда сокрушаемый горем король объявил, что отдаст счастливцу, который раскусит орех, 
свою дочь в супруги и сделает своим наследником, скромно явился ко двору молодой Дроссельмейер и 
попросил позволения сделать попытку.

Этот юноша понравился принцессе больше всех остальных, так что она даже положила на сердце свою
маленькую ручку и сказала, вздохнув:

— Ах, если бы он раскусил орех и стал моим мужем!"