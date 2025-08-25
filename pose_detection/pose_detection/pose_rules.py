from abc import ABC, abstractmethod
from typing import Callable, override

from body.body import Body

class PoseRule(ABC):
    @abstractmethod
    def is_satisfied(self, param) -> bool:
        pass


class AcceptAllPoseRule(PoseRule):
    def is_satisfied(self, value) -> bool:
        return True


class GenericPoseRule(PoseRule):
    def __init__(self, test_func: Callable[[Body], bool]):
        self.test_func = test_func

    def is_satisfied(self, body: Body) -> bool:
        return self.test_func(body)


class RangePoseRule(PoseRule):
    def __init__(self, target, bottom_tolerance, upper_tolerance, relax_factor=1.0):
        if relax_factor < 1.0 or relax_factor >= 2.0:
            raise ValueError("relax_factor must be in the range [1.0, 2.0)")
        self.target = target
        self.bottom_tolerance = bottom_tolerance
        self.upper_tolerance = upper_tolerance
        self.relax_factor = relax_factor
        self.satisfied = False

    @override
    def is_satisfied(self, number) -> bool:
        if self.satisfied:
            bottom_limit = self.target - self.target * (self.relax_factor - 1.0) - self.bottom_tolerance
            upper_limit = self.target * self.relax_factor + self.upper_tolerance
            return self.target - self.target * (self.relax_factor - 1.0)  - self.bottom_tolerance <= number <= self.target * self.relax_factor + self.upper_tolerance
        else:
            return self.target - self.bottom_tolerance <= number <= self.target + self.upper_tolerance

