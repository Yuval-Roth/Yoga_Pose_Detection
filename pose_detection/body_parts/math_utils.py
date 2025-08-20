import math


def pixel_to_cartesian(px: int, py: int, width: int, height: int):
    """
    Convert pixel coordinates (px, py) from a screen of size (width, height)
    into Cartesian coordinates where (0,0) is at the center,
    +x is right, +y is up.
    """
    x = px - width / 2
    y = (height / 2) - py
    return x, y


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

    @staticmethod
    def cross2(v1,v2):
        """
        Calculate the 2D cross product of two vectors v1 and v2.
        between x and y
        """
        return v1.x * v2.y - v1.y * v2.x

    @staticmethod
    def angle(v1, v2):
        """
        Calculate the angle in degrees between two vectors v1 and v2.
        """
        dot_product = v1.x * v2.x + v1.y * v2.y
        magnitude_v1 = v1.magnitude()
        magnitude_v2 = v2.magnitude()
        if magnitude_v1 == 0 or magnitude_v2 == 0:
            return 0.0
        cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        return math.degrees(angle_rad)
