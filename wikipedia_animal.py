import wikipediaapi

from loguru import logger # Для приятного логирования
from time import time # Для того что-бы засикать время выполнения программы


# Устанавливаем язык
WIKI_WIKI = wikipediaapi.Wikipedia("ru")
PAGE_PY = WIKI_WIKI.page('Python_(programming_language)')

# Проверяем существует ли вообще данная страница 
ANIMAL_PAGES = WIKI_WIKI.page("Категория:Животные_по_алфавиту")
    
# Русский словарь 
RUSSIAN_DICT = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ')


""" Функция вывод все страницы из категории животные """
def main():
    # Выводим все члены данной категории 
    all_animals = ANIMAL_PAGES.categorymembers 
    """ 
    Цикл который проходится по буквам алфавита и животными.
    Далее заносит данный в словарь. Где ключь - это буква алфавита,
    а значение - это кол-во животных которые принадлежат данной группе
    """
    for animals_dict in RUSSIAN_DICT:
        animals_count = get_all_animals(all_animals, animals_dict)
        print(f"{animals_dict}: {animals_count}")


""" Функция проходит по всем животным и подсчитывает их кол-во по title """
logger.info("Established a connection")
def get_all_animals(all_animals, animals_dict):
    counter = 0
    for animal in all_animals.values():
        if animal.title[:1] == animals_dict:
            counter += 1
    return counter
    

if __name__ == "__main__":
    t0 = time() # Засикаем время    
    logger.info("Wait")
    main()
    print(f"Затрачено на работу скрипта: {(time() - t0)}")
logger.debug("Everything went well")
