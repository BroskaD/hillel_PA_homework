class DataColumns:
    """
    Stores the names of the columns related to the file hw.csv and its transforming.
    """

    raw_height_column_inches = ' "Height(Inches)"'
    raw_weight_column_pounds = ' "Weight(Pounds)"'
    height_column_inches = 'Height(Inches)'
    weight_column_pounds = 'Weight(Pounds)'
    height_column_cm = 'Height(cm)'
    weight_column_kg = 'Weight(Pounds)'
    index_column = 'Index'


class AverageTableColumns:
    """
    Stores the names of the columns of result table with average values.
    """

    units = 'Units'
    average_value = 'Average value'


class RequirementsTableColumns:
    """
    Stores the names of the columns of result table with package versions.
    """

    package = 'Package'
    version = 'Version'
