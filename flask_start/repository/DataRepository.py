import os

import pandas as pd

from flask_start.datamodel.DataColumns import DataColumns, AverageTableColumns, RequirementsTableColumns


class DataRepository:
    """
    Provides access to data.
    """

    def __init__(self):
        self.__data_path = f'{os.path.dirname(__file__)}/../data'
        self.__data_file_name = 'hw.csv'
        self.__requirements_file_name = 'requirements.txt'

    def get_requirements(self) -> tuple[list, dict]:
        """
        Provides access to requirements data.
        :return: tuple of list with result table column names and dictionary with package name: version structure.
        """

        file_path = f'{self.__data_path}/{self.__requirements_file_name}'

        data = self.__read_txt_file(file_path)
        data = self.__parse_requirements_file(data)

        columns = [RequirementsTableColumns.package, RequirementsTableColumns.version]

        return columns, data

    @staticmethod
    def __parse_requirements_file(data: list) -> dict:
        """
        Splits each row in requirements.txt file by '==' symbol.
        :param data: list of strings in input file.
        :return: dictionary with package name as the key and version as the value.
        """

        res = {package.strip().split('==')[0]: package.strip().split('==')[1] for package in data}

        return res

    @staticmethod
    def __read_txt_file(file_path: str) -> list:
        """
        Provides reading .txt file.
        :param file_path: path to the file to read.
        :return: list of rows in file.
        """

        if not os.path.isfile(file_path):
            raise FileExistsError('Data file does not exist')

        with open(file_path, 'r') as f:
            res = f.readlines()

        return res

    def get_average_data(self) -> tuple[list, dict]:
        """
        Provides access to the hw.csv file and computing average data parameters
        :return: tuple of list with result table column names and dictionary with unit: average value structure.
        """

        file_path = f'{self.__data_path}/{self.__data_file_name}'

        df = self.__read_raw_data_file(file_path)
        self.__clean_dataframe(df)
        self.__transform_units(df)

        columns = [AverageTableColumns.units, AverageTableColumns.average_value]
        res = self.__calculate_average(df)

        return columns, res

    @staticmethod
    def __read_raw_data_file(file_path: str) -> pd.DataFrame:
        """
        Provides reading .csv file via Pandas.
        :param file_path: path to the file to read.
        :return: pandas.Dataframe
        """

        if not os.path.isfile(file_path):
            raise FileExistsError('Data file does not exist')

        res = pd.read_csv(file_path)

        return res

    @staticmethod
    def __clean_dataframe(df: pd.DataFrame) -> None:
        """
        Provides inplace cleaning column names of the dataframe from unnecessary symbols
        and dropping unnecessary columns
        :param df: dataframe to clean
        :return: None
        """

        df.drop(columns=[DataColumns.index_column], inplace=True)
        new_columns_name = {
            DataColumns.raw_height_column_inches: DataColumns.height_column_inches,
            DataColumns.raw_weight_column_pounds: DataColumns.weight_column_pounds
        }
        df.rename(columns=new_columns_name, inplace=True)

    @staticmethod
    def __transform_units(df: pd.DataFrame) -> None:
        """
        Provides inplace transforming units from inches and pounds to cm and kg with renaming relevant columns.
        :param df: dataframe to transform
        :return: None
        """

        inches_to_cm = 2.54
        pounds_to_kg = 0.453592

        df[DataColumns.height_column_inches] = (df[DataColumns.height_column_inches] * inches_to_cm).round(2)
        df[DataColumns.weight_column_pounds] = (df[DataColumns.weight_column_pounds] * pounds_to_kg).round(2)

        new_columns_name = {
            DataColumns.height_column_inches: DataColumns.height_column_cm,
            DataColumns.weight_column_pounds: DataColumns.weight_column_kg
        }

        df.rename(columns=new_columns_name, inplace=True)

    @staticmethod
    def __calculate_average(df: pd.DataFrame) -> dict:
        """
        Provides calculating average value by each column in the dataframe.
        :param df: dataframe to calculate average value.
        :return: dictionary with column name as the key and average value as the value.
        """

        res = df.mean().round(2).to_dict()

        return res
