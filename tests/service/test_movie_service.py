import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0, 'Ошибка'

    def test_get_one(self):
        movie = self.movie_service.get_one(2)

        assert movie is not None
        assert movie.id is not None

    def test_create(self):
        movie_created = {"title": 'Название',
                         "description": 'Описание',
                         "trailer": 'Ссылка', 'year': 0000, "rating": 0.1, 'genre_id': 3, 'director_id': 4}
        movie = self.movie_service.create(movie_created)

        assert movie.id is not None

    def test_partially_update(self):
        movie_created = {"id": 2, "title": 'Название'}
        self.movie_service.partially_update(movie_created)

    def test_update(self):
        movie_created = {"id": 2, "title": 'Название',
                         "description": 'Описание',
                         "trailer": 'Ссылка', 'year': 0000, "rating": 0.1, 'genre_id': 3, 'director_id': 4}
        self.movie_service.update(movie_created)

    def test_delete(self):
        self.movie_service.delete(2)
