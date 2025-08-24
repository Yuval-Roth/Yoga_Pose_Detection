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


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        return Vec2(self.x / mag, self.y / mag) if mag > 0 else Vec2(0, 0)

    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"


    @staticmethod
    def angle(v1, v2):
        """
        Calculate the signed angle in degrees between two vectors v1 and v2.
        Positive = counter-clockwise, Negative = clockwise.
        """
        dot_product = v1.x * v2.x + v1.y * v2.y
        cross_product = v1.x * v2.y - v1.y * v2.x

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

def angle_diff(first, second):
    """
    Calculate the smallest difference in angle between two vectors in degrees.
    The result is always between 0 and 180 degrees.
    """
    diff = abs(first - second) % 360
    return diff if diff <= 180 else 360 - diff


if __name__ == "__main__":
    v1 = Vec2(1, 0)
    v2 = Vec2(0, 1)
    print("Angle between v1 and v2:", Vec2.angle(v1, v2))  # Should be 90 degrees
    print("Angle difference between 30 and 150:", angle_diff(30, 150))  # Should be 120 degrees
    print("Angle difference between 350 and 10:", angle_diff(350, 10))  # Should be 20 degrees
