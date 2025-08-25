from enum import Enum

from body.math_utils import Vec2, Vec2Avg, Vec2Pair


class BodyParts(Enum):
    LEFT_ARM = "left_arm"
    RIGHT_ARM = "right_arm"
    LEFT_LEG = "left_leg"
    RIGHT_LEG = "right_leg"
    TORSO = "torso"
    HEAD = "head"

class Arm:
    def __init__(self, avg_count: int):
        self.shoulder = Vec2Avg(avg_count)
        self.elbow = Vec2Avg(avg_count)
        self.wrist = Vec2Avg(avg_count)
        self.first = Vec2Pair(self.shoulder, self.elbow)
        self.second = Vec2Pair(self.elbow, self.wrist)

    def update(self, shoulder, elbow, wrist):
        self.shoulder.add_point(shoulder.x, shoulder.y)
        self.elbow.add_point(elbow.x, elbow.y)
        self.wrist.add_point(wrist.x, wrist.y)


class Leg:
    def __init__(self, avg_count: int):
        self.hip = Vec2Avg(avg_count)
        self.knee = Vec2Avg(avg_count)
        self.ankle = Vec2Avg(avg_count)
        self.first = Vec2Pair(self.hip, self.knee)
        self.second = Vec2Pair(self.knee, self.ankle)

    def update(self, hip, knee, ankle):
        self.hip.add_point(hip.x, hip.y)
        self.knee.add_point(knee.x, knee.y)
        self.ankle.add_point(ankle.x, ankle.y)


class Torso:
    def __init__(self, avg_count: int):
        self.right_shoulder = Vec2Avg(avg_count)
        self.left_shoulder = Vec2Avg(avg_count)
        self.right_hip = Vec2Avg(avg_count)
        self.left_hip = Vec2Avg(avg_count)
        self.right = Vec2Pair(self.right_shoulder, self.right_hip)
        self.left = Vec2Pair(self.left_shoulder, self.left_hip)

    def update(self, left_shoulder, right_shoulder, left_hip, right_hip):
        self.left_shoulder.add_point(left_shoulder.x, left_shoulder.y)
        self.right_shoulder.add_point(right_shoulder.x, right_shoulder.y)
        self.left_hip.add_point(left_hip.x, left_hip.y)
        self.right_hip.add_point(right_hip.x, right_hip.y)



class Head:
    def __init__(self, avg_count: int):
        self.nose = Vec2Avg(avg_count)
        self.left_eye = Vec2Avg(avg_count)
        self.right_eye = Vec2Avg(avg_count)

    def update(self, nose, left_eye, right_eye):
        self.nose.add_point(nose.x, nose.y)
        self.left_eye.add_point(left_eye.x, left_eye.y)
        self.right_eye.add_point(right_eye.x, right_eye.y)

