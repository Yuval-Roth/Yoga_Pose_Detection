from abc import ABC, abstractmethod
from typing import Callable, override

from body.body import Body
from math_utils import signed_angle_diff


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
    def __init__(self, target, bottom_tolerance, upper_tolerance):
        self.target = target
        self.bottom_tolerance = bottom_tolerance
        self.upper_tolerance = upper_tolerance

    @override
    def is_satisfied(self, number) -> bool:
        diff = signed_angle_diff(number, self.target)
        return -self.bottom_tolerance <= diff <= self.upper_tolerance

