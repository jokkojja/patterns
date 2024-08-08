from abc import ABC, abstractmethod
from typing import Callable

# Словил шизу, почему бы не соответствовать OCP

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

    def __init__(self):
        self.__strategies = {}

    def register_strategy(self, condition: Callable[[list[int]], bool], strategy: SortStrategy) -> None:
        self.__strategies[condition] = strategy

    def sort(self, array: list[int]) -> list[int]:
        for condition, strategy in self.__strategies.items():
            if condition(array):
                return strategy.sort(array)

        raise ValueError("No strategy found for the given array")


if __name__ == "__main__":

    small_array = [1, 3, 4, 2]
    big_array = [1, 4, 3, 2, 8, 10, 5, 6, 9, 7]

    sorter = Sorter()

    sorter.register_strategy(lambda arr: len(arr) <= 5, BubbleSortStrategy())
    sorter.register_strategy(lambda arr: len(arr) > 5, QuickSortStrategy())

    sorted_small_array = sorter.sort(small_array)
    sorted_big_array = sorter.sort(big_array)

