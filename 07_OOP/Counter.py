from typing import Optional


class Counter:
    """
    Implementing a simple counter for integers.

    Parameters
    ----------
    min_value: int, default=0
        A min value counter start.

    max_value: int, default=100
        A max value that counter can reach.

    current_value: int, default=None
        A current value of the counter.
    """

    def __init__(self, min_value: int = 0, max_value: int = 100, current_value: Optional[int] = None) -> None:

        if current_value is None:
            current_value = min_value

        if min_value > max_value or current_value < min_value or current_value > max_value:
            raise ValueError('Wrong initial parameters of the counter')

        self.__min_value = min_value
        self.__max_value = max_value
        self.__current_value = current_value

    def increase(self) -> None:
        """
        Increments the current value of the counter by one
        :return:
        None
        """

        if self.__current_value != self.__max_value:
            self.__current_value += 1
        else:
            raise ValueError('The counter has reached its maximum value')

    def get_current_value(self) -> int:
        """
        Get current value of the counter
        :return:
        int: Current value of the counter
        """

        return self.__current_value


c = Counter(13, 15)
print(c.get_current_value())            # 13
c.increase()
print(c.get_current_value())            # 14
c.increase()
print(c.get_current_value())            # 15
c.increase()                            # ValueError: The counter has reached its maximum value
print(c.get_current_value())
