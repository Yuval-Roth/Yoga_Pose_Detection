import math
from enum import IntEnum, Enum


class Vec3:
    def __init__(self, x, y, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        mag = self.magnitude()
        return Vec3(self.x / mag, self.y / mag, self.z / mag) if mag > 0 else Vec3(0, 0, 0)

    def __repr__(self):
        return f"Vec3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    @staticmethod
    def cross(v1, v2):
        return Vec3(
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )


class BodyParts(Enum):
    LEFT_ARM = "left_arm"
    RIGHT_ARM = "right_arm"
    LEFT_LEG = "left_leg"
    RIGHT_LEG = "right_leg"
    TORSO = "torso"
    HEAD = "head"


class BodyPart:
    def __init__(self, start, end):
        self.vector = (Vec3(end.x, end.y, end.z) - Vec3(start.x, start.y, start.z)).normalize()
