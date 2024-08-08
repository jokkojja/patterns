from abc import ABC, abstractmethod
from typing import TypeAlias

Role: TypeAlias = str

# Component
class Employee(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def salary(self) -> float:
        raise NotImplementedError

    @salary.setter
    def salary(self, salary: float) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def roles(self) -> list:
        raise NotImplementedError


# Leaf
class Developer(Employee):

    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary
        self.__roles: list[Role] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        self.__salary = salary

    @property
    def roles(self) -> list:
        return self.__roles

    def add_role(self, role: Role):
        self.__roles.append(role)



# Leaf
class Designer(Employee):

    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary
        self.__roles = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        self.__salary = salary

    @property
    def roles(self) -> list:
        return self.__roles

    def add_role(self, role: Role):
        self.__roles.append(role)

# Composite
class Organization:

    def __init__(self):
        self.__employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)

    def get_net_salaries(self) -> float:
        net_salary = sum(employee.salary for employee in self.__employees)
        return net_salary





if __name__ == "__main__":
    john = Developer("John Doe", 12000.0)
    jane = Designer("Jane Doe", 15000.0)

    organization = Organization()

    organization.add_employee(john)
    organization.add_employee(jane)

    print(f"New salaries: {organization.get_net_salaries()}")