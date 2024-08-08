from abc import ABC, abstractmethod

class SortStrategy(ABC):

    @staticmethod
    @abstractmethod
    def sort(array: list[int]) -> list[int]:
        raise NotImplementedError

class BubbleSortStrategy(SortStrategy):

    @staticmethod
    def sort(array: list[int]) -> list[int]:
        print("using buble sort")
        return array

class QuickSortStrategy(SortStrategy):

    @staticmethod
    def sort(array: list[int]) -> list[int]:
        print("using quick sort")
        return array

class Sorter:

    def __init__(self, sorter_small: SortStrategy, sorter_big: SortStrategy):
        self.__sorter_small = sorter_small
        self.__sorter_big = sorter_big

    def sort(self, array: list[int]) -> list[int]:
        if len(array) > 5:
            return self.__sorter_big.sort(array)

        return self.__sorter_small.sort(array)


if __name__ == "__main__":

    small_array = [1, 3, 4, 2]
    big_array = [1, 4, 3, 2, 8, 10, 5, 6, 9, 7]

    bubble_sort_strategy = BubbleSortStrategy()
    quick_sort_strategy = QuickSortStrategy()

    sorter = Sorter(sorter_small=bubble_sort_strategy, sorter_big=quick_sort_strategy)

    sorter.sort(small_array)
    sorter.sort(big_array)


