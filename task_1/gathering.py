"""
ЗАДАНИЕ

Выбрать источник данных и собрать данные по некоторой предметной области.

Цель задания - отработать навык написания программ на Python.
В процессе выполнения задания затронем области:
- организация кода в виде проекта, импортирование модулей внутри проекта
- unit тестирование
- работа с файлами
- работа с протоколом http
- работа с pandas
- логирование

Требования к выполнению задания:

- собрать не менее 1000 объектов

- в каждом объекте должно быть не менее 5 атрибутов
(иначе просто будет не с чем работать.
исключение - вы абсолютно уверены что 4 атрибута в ваших данных
невероятно интересны)

- сохранить объекты в виде csv файла

- считать статистику по собранным объектам


Этапы:

1. Выбрать источник данных.

Это может быть любой сайт или любое API

Примеры:
- Пользователи vk.com (API)
- Посты любой популярной группы vk.com (API)
- Фильмы с Кинопоиска
(см. ссылку на статью ниже)
- Отзывы с Кинопоиска
- Статьи Википедии
(довольно сложная задача,
можно скачать дамп википедии и распарсить его,
можно найти упрощенные дампы)
- Статьи на habrahabr.ru
- Объекты на внутриигровом рынке на каком-нибудь сервере WOW (API)
(желательно англоязычном, иначе будет сложно разобраться)
- Матчи в DOTA (API)
- Сайт с кулинарными рецептами
- Ebay (API)
- Amazon (API)
...

Не ограничивайте свою фантазию. Это могут быть любые данные,
связанные с вашим хобби, работой, данные любой тематики.
Задание специально ставится в открытой форме.
У такого подхода две цели -
развить способность смотреть на задачу широко,
пополнить ваше портфолио (вы вполне можете в какой-то момент
развить этот проект в стартап, почему бы и нет,
а так же написать статью на хабр(!) или в личный блог.
Чем больше у вас таких активностей, тем ценнее ваша кандидатура на рынке)

2. Собрать данные из источника и сохранить себе в любом виде,
который потом сможете преобразовать

Можно сохранять страницы сайта в виде отдельных файлов.
Можно сразу доставать нужную информацию.
Главное - постараться не обращаться по http за одними и теми же данными много раз.
Суть в том, чтобы скачать данные себе, чтобы потом их можно было как угодно обработать.
В случае, если обработать захочется иначе - данные не надо собирать заново.
Нужно соблюдать "этикет", не пытаться заддосить сайт собирая данные в несколько потоков,
иногда может понадобиться дополнительная авторизация.

В случае с ограничениями api можно использовать time.sleep(seconds),
чтобы сделать задержку между запросами

3. Преобразовать данные из собранного вида в табличный вид.

Нужно достать из сырых данных ту самую информацию, которую считаете ценной
и сохранить в табличном формате - csv отлично для этого подходит

4. Посчитать статистики в данных
Требование - использовать pandas (мы ведь еще отрабатываем навык использования инструментария)
То, что считаете важным и хотели бы о данных узнать.

Критерий сдачи задания - собраны данные по не менее чем 1000 объектам (больше - лучше),
при запуске кода командой "python3 -m gathering stats" из собранных данных
считается и печатается в консоль некоторая статистика

Код можно менять любым удобным образом
Можно использовать и Python 2.7, и 3

Зачем нужны __init__.py файлы
https://stackoverflow.com/questions/448271/what-is-init-py-for

Про документирование в Python проекте
https://www.python.org/dev/peps/pep-0257/

Про оформление Python кода
https://www.python.org/dev/peps/pep-0008/


Примеры сбора данных:
https://habrahabr.ru/post/280238/

Для запуска тестов в корне проекта:
python3 -m unittest discover

Для запуска проекта из корня проекта:
python3 -m gathering gather
или
python3 -m gathering transform
или
python3 -m gathering stats


Для проверки стиля кода всех файлов проекта из корня проекта
pep8 .

"""

import logging
import sys

import pandas as pd
import matplotlib.pyplot as plt

from scrappers.scrapper import Scrapper
from storages.file_storage import FileStorage

from parsers.JSONparser import JSONParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPPED_FILE = 'data.txt'
TABLE_FORMAT_FILE = 'data.csv'


def gather_process():
    logger.info("gather")

    storage = FileStorage(SCRAPPED_FILE)

    # You can also pass a storage
    scrapper = Scrapper()
    scrapper.scrap_process(storage)


def convert_data_to_table_format():
    logger.info("transform")

    # Your code here
    # transform gathered data from txt file to pandas DataFrame and save as csv
    
    storage = FileStorage(SCRAPPED_FILE)
    parser  = JSONParser()
    
    data = storage.read_data()
    
    df = parser.parse(data)

    df.to_csv(TABLE_FORMAT_FILE)

def stats_of_data():
    logger.info("stats")
    
    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use not only describe and info.
    # Ask yourself what would you like to know about this data (most frequent word, or something else)
    
    df = pd.read_csv(TABLE_FORMAT_FILE)
    
    print("Lets print some technical data about data.")
    print("Data frame shape is: ")
    
    print( df.shape)
    
    print("Data frame columns are: ")
    
    print(df.columns)
    
    print("Data description: ")
    
    print( df.describe() )
    
    print("")
    print("We're going to explore the sun's coronal mass ejections, " )
    print("details: https://en.wikipedia.org/wiki/Coronal_mass_ejection")
    print("")
    print("We can see that NASA experts divided all CME in different groups or types")
    print("Lets understand it in figures.")
    print("")
    print("Calculate mean parameters of each type.")
    print("First, all ocasions of each type:" )
    
    types = df.type.value_counts().to_dict()
    for type__ in types:
        print("CME type is ", type__, " , number of ocasions: ", types[type__], \
              " and frequency is ", \
              types[type__]/sum(types.values())*100, " percents." )
        
    print("")
    print("We can see that S and C types are the most frequent,")
    print("while O and R is near zero.")
    print("")
    print("Second, explore the mean and the median for each type")
    
    gr = df.groupby(['type'])[['speed', 'halfAngle']]
    
    print("Mean first")
    print(gr.mean())
    print("")
    print("Median then")
    print(gr.median())
    print("")
    print("We can see categories, each type differ by speed and angle")
    print("Now lets make plot and show when the most significant CME (type R)" \
          " occur")
    print("")
    
    df['date'] = df["activityID"]
    df['date'] = df['date'].apply( lambda x: ".".join( x.split('-')[0:2] ) )
    plt.plot( df.groupby(['date'])[['type']].count() )
    plt.title('Occurance of CME by time.')
    plt.show()
    


if __name__ == '__main__':
    """
    why main is so...?
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather_process()

    elif sys.argv[1] == 'transform':
        convert_data_to_table_format()

    elif sys.argv[1] == 'stats':
        stats_of_data()

    logger.info("work ended")
