from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture  # фикстура режиссёров
def director_dao():
    dd = DirectorDAO(None)

    dir_01 = Director(id=1, name='Тейлор Шеридан')
    dir_02 = Director(id=2, name='Квентин Тарантино')
    dir_03 = Director(id=3, name='Владимир Вайншток')

    dd.get_all = MagicMock(return_value=[dir_01, dir_02, dir_03])
    dd.get_one = MagicMock(return_value=dir_01)
    dd.create = MagicMock(return_value=Director(id=1))
    dd.delete = MagicMock()
    dd.update = MagicMock()
    dd.partially_update = MagicMock()

    return dd


@pytest.fixture  # фикстура фильмов
def movie_dao():
    md = MovieDAO(None)

    mov_01 = Movie(id=1, title='Йеллоустоун',
                   description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
                   trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', year=2018, rating=8.6, genre_id=3, director_id=4)
    mov_02 = Movie(id=2, title='Омерзительная восьмерка',
                   description='США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.',
                   trailer='https://www.youtube.com/watch?v=lmB9VWm0okU', year=2015, rating=7.8, genre_id=3, director_id=4)
    mov_03 = Movie(id=3, title='Вооружен и очень опасен',
                   description='События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...',
                   trailer='https://www.youtube.com/watch?v=hLA5631F-jo', year=1978, rating=6, genre_id=3, director_id=4)

    md.get_all = MagicMock(return_value=[mov_01, mov_02, mov_03])
    md.get_one = MagicMock(return_value=mov_02)
    md.create = MagicMock(return_value=Movie(id=2))
    md.delete = MagicMock()
    md.update = MagicMock()
    md.partially_update = MagicMock()

    return md


@pytest.fixture  # фикстура жанров
def genre_dao():
    gd = GenreDAO(None)

    gen_01 = Genre(id=1, name='Комедия')
    gen_02 = Genre(id=2, name='Семейный')
    gen_03 = Genre(id=3, name='Фэнтези')

    gd.get_all = MagicMock(return_value=[gen_01, gen_02, gen_03])
    gd.get_one = MagicMock(return_value=gen_03)
    gd.create = MagicMock(return_value=Genre(id=3))
    gd.delete = MagicMock()
    gd.update = MagicMock()
    gd.partially_update = MagicMock()

    return gd
