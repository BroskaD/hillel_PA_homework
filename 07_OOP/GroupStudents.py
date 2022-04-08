from typing import Optional

from prettytable import PrettyTable


class Student:
    """
    Student describing

    Parameters
    ----------
    name: str
        Name of the student
    surname: str
        Second name of the student
    grades: dict
        As the key name of the subject and as the value - grade of this subject
    """

    def __init__(self, name: str, surname: str, grades: dict[str: int]) -> None:

        if not name or not surname:
            raise ValueError('Name or surname can not be empty!')

        for key, value in grades.items():
            if not key:
                raise ValueError('Name of the subject can not be empty!')
            if value < 1 or value > 12 or not isinstance(value, int):
                raise ValueError('Grade has incorrect format!')

        self.__name = name
        self.__surname = surname
        self.__grades = grades

    def add_grade(self, grade: dict[str: int]) -> None:
        """
        Add or update grades of the student
        :param grade: Dictionary that contains new grades
        :return: None
        """
        self.__grades |= grade

    def del_grade(self, subject: str) -> None:
        """
        Deleting grades by subject name
        :param subject: Name of the subject to delete
        :return: None
        """
        if subject in self.__grades.keys():
            del self.__grades[subject]
        else:
            print(f'{subject} does not exist in the grade table. Nothing to delete')

    def display(self) -> None:
        """
        Displaying student information
        :return: None
        """

        # performing table visualization with str.format() method
        print(f'Student: {self.__name} {self.__surname}')
        print('_' * 30)
        print('{:<20} | {:<10}'.format('Subject', 'Grade'))
        print('_' * 30)
        for subject, grade in self.__grades.items():
            print('{:<20} |{:<10}'.format(subject, grade))

    def get_name_surname(self) -> tuple[str, str]:
        """
        Provides access to the name and surname of the student
        :return: Name and surname
        """
        return self.__name, self.__surname

    def get_grades(self) -> dict:
        """
        Provides access to the grades of the student
        :return: Dictionary with the grades
        """
        return self.__grades


class Group:
    """
    Group Describing

    Parameters
    ----------
    name: str
        Name of the group
    students: list default=None
        List of the Student instances
    """

    def __init__(self, name: str, students: Optional[list[Student]] = None) -> None:

        if not name:
            raise ValueError('Name of the group can not be empty!')

        if students is None:
            students = list()

        self.__name = name
        self.__students = students

    def add_student(self, student: Student) -> None:
        """
        Adding new student to the group
        :param student: Student instance
        :return: None
        """
        self.__students.append(student)

    def remove_student_by_name_surname(self, name_surname: tuple) -> None:
        """
        Provides deleting student by name and surname
        :param name_surname: Tuple that contains name and surname
        :return: None
        """
        counter = 0
        for student in self.__students:
            if name_surname == student.get_name_surname():
                self.__students.remove(student)
                counter += 1
        print(f'Deleted {counter} records')

    def display(self) -> None:
        """
        Displaying group information in the form of a table
        :return: None
        """
        subjects, grades = self.__get_students_grades()
        # performing table visualization with PrettyTable
        headers = ['Name', 'Surname'] + subjects
        table = PrettyTable()
        table.title = self.__name
        table.field_names = headers

        for i in grades:
            table.add_row(i)

        print(table)

    def __get_all_subjects(self) -> list:
        """
        Provide access to the list of all possible subjects
        :return: List of subjects
        """
        subjects = set()

        for student in self.__students:
            subjects = subjects.union(set(student.get_grades().keys()))

        return list(subjects)

    def __get_students_grades(self) -> tuple[list, list]:
        """
        Provide unify data structure of the students grades
        :return: tuple that contains two lists: first contains sorted subjects, second - lists of name, surname
        and grades by student
        """
        subjects = self.__get_all_subjects()
        subjects.sort()
        grades = []
        for student in self.__students:
            temp_list = [student.get_name_surname()[0], student.get_name_surname()[1]]
            for sub in subjects:
                # if subject name is missing place '-' symbol
                try:
                    temp_list.append(student.get_grades()[sub])
                except KeyError:
                    temp_list.append('-')
            grades.append(temp_list)

        return subjects, grades

    def del_all_students(self) -> None:
        """
        Clear group from all students. Not deleting group!
        :return: None
        """
        self.__students.clear()
