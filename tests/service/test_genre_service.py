import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0, 'Ошибка'

    def test_get_one(self):
        genre = self.genre_service.get_one(3)

        assert genre is not None
        assert genre.id is not None

    def test_create(self):
        genre_created = {"name": "Ужасы"}
        genre = self.genre_service.create(genre_created)

        assert genre.id is not None

    def test_partially_update(self):
        genre_created = {"id": 3, "name": "Ужасы"}
        self.genre_service.partially_update(genre_created)

    def test_update(self):
        genre_created = {"id": 3, "name": "Ужасы"}
        self.genre_service.update(genre_created)

    def test_delete(self):
        self.genre_service.delete(1)