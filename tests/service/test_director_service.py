import pytest

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0, 'Ошибка в кол-ве директоров'

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_create(self):
        director_created = {"name": "Теодор"}
        director = self.director_service.create(director_created)

        assert director.id is not None

    def test_partially_update(self):
        director_created = {"id": 1, "name": "Теодор"}
        self.director_service.partially_update(director_created)

    def test_update(self):
        director_created = {"id": 1, "name": "Теодор"}
        self.director_service.update(director_created)

    def test_delete(self):
        self.director_service.delete(1)
