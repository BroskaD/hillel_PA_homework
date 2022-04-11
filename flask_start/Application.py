from repository.DataRepository import DataRepository


class Application:

    def __init__(self):
        self.__data_repo = DataRepository()

    def get_average_height_weight(self) -> tuple[list, dict]:
        return self.__data_repo.get_average_data()

    def get_requirements(self) -> tuple[list, dict]:
        return self.__data_repo.get_requirements()
