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

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def center_between(self, other: 'Vec2'):
        return Vec2((self.x + other.x) / 2, (self.y + other.y) / 2)

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


class Vec2Avg(Vec2):
    def __init__(self, count):
        super().__init__(0, 0)
        self.count = count
        self.currentCount = 0
        self.vectors = []
        self.x_sum = 0
        self.y_sum = 0

    def add_vec2(self, vec: Vec2):
        self.add_point(vec.x, vec.y)

    def add_point(self,x: int, y: int):
        vec = Vec2(x, y)
        if self.currentCount < self.count:
            self.currentCount += 1
        else:
            old_vec = self.vectors.pop(0)
            self.x_sum -= old_vec.x
            self.y_sum -= old_vec.y
        self.vectors.append(vec)
        self.x_sum += x
        self.y_sum += y
        self.x = int(self.x_sum / self.currentCount)
        self.y = int(self.y_sum / self.currentCount)

class Vec2Pair:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def vector(self):
        return (self.end - self.start).normalize()

    def center(self):
        self.start.center_between(self.end)


def angle_diff(first, second):
    """
    Calculate the smallest difference in angle between two vectors in degrees.
    The result is always between 0 and 180 degrees.
    """
    diff = abs(first - second) % 360
    return diff if diff <= 180 else 360 - diff

def signed_angle_diff(first, second):
    """
    Calculate the signed difference in angle between two vectors in degrees.
    Positive = clockwise, Negative = counter-clockwise.
    The result is always between -180 and +180 degrees.
    """
    diff = (first - second) % 360
    if diff > 180:
        diff -= 360
    return diff

def relatively_close(a, b, factor):
    """
    Check if two values are relatively close within a given factor.
    using division of the larger by the smaller.
    """
    if a > b:
        return a / b <= factor
    else:
        return b / a <= factor


