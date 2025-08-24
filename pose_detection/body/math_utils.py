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
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        return Vec3(self.x / mag, self.y / mag, self.z) if mag > 0 else Vec3(0, 0, 0)

    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


    @staticmethod
    def angle2(v1, v2):
        """
        Calculate the signed angle in degrees between two vectors v1 and v2.
        Based on x and y components only, ignoring z.
        Positive = counter-clockwise, Negative = clockwise.
        """
        dot_product = v1.x * v2.x + v1.y * v2.y
        cross_product = v1.x * v2.y - v1.y * v2.x  # 2D equivalent of z-component of cross

        magnitude_v1 = v1.magnitude()
        magnitude_v2 = v2.magnitude()
        if magnitude_v1 == 0 or magnitude_v2 == 0:
            return 0.0

        cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
        cos_angle = max(-1.0, min(1.0, cos_angle))  # clamp to avoid NaNs

        angle_rad = math.acos(cos_angle)

        # Use cross product to determine sign
        if cross_product < 0:
            angle_rad = -angle_rad

        return math.degrees(angle_rad)

