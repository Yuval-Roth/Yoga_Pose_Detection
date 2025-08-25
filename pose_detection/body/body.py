from mediapipe.python.solutions.pose import PoseLandmark

from body.body_parts import *


class Body:
    def __init__(self, screen_width: int, screen_height: int, avg_count: int):
        self.width = screen_width
        self.height = screen_height

        self.parts = {
            BodyParts.LEFT_ARM: Arm(avg_count),
            BodyParts.RIGHT_ARM: Arm(avg_count),
            BodyParts.LEFT_LEG: Leg(avg_count),
            BodyParts.RIGHT_LEG: Leg(avg_count),
            BodyParts.TORSO: Torso(avg_count),
            BodyParts.HEAD: Head(avg_count)
        }

    def update(self, pose_landmarks):
        landmarks = dict()
        for idx, landmark in enumerate(pose_landmarks):
            landmarks[idx] = Vec2(int(landmark.x * self.width), int(landmark.y * self.height))

        self.parts[BodyParts.LEFT_ARM].update(
            landmarks[PoseLandmark.LEFT_SHOULDER],
            landmarks[PoseLandmark.LEFT_ELBOW],
            landmarks[PoseLandmark.LEFT_WRIST]
        )
        self.parts[BodyParts.RIGHT_ARM].update(
            landmarks[PoseLandmark.RIGHT_SHOULDER],
            landmarks[PoseLandmark.RIGHT_ELBOW],
            landmarks[PoseLandmark.RIGHT_WRIST]
        )
        self.parts[BodyParts.LEFT_LEG].update(
            landmarks[PoseLandmark.LEFT_HIP],
            landmarks[PoseLandmark.LEFT_KNEE],
            landmarks[PoseLandmark.LEFT_ANKLE]
        )
        self.parts[BodyParts.RIGHT_LEG].update(
            landmarks[PoseLandmark.RIGHT_HIP],
            landmarks[PoseLandmark.RIGHT_KNEE],
            landmarks[PoseLandmark.RIGHT_ANKLE]
        )
        self.parts[BodyParts.TORSO].update(
            landmarks[PoseLandmark.LEFT_SHOULDER],
            landmarks[PoseLandmark.RIGHT_SHOULDER],
            landmarks[PoseLandmark.LEFT_HIP],
            landmarks[PoseLandmark.RIGHT_HIP]
        )
        self.parts[BodyParts.HEAD].update(
            landmarks[PoseLandmark.NOSE],
            landmarks[PoseLandmark.LEFT_EYE],
            landmarks[PoseLandmark.RIGHT_EYE],
        )


    def hips_center(self) -> Vec2:
        left_hip = self.parts[BodyParts.TORSO].left_hip
        right_hip = self.parts[BodyParts.TORSO].right_hip
        return left_hip.center_between(right_hip)

    def shoulders_center(self):
        left_shoulder = self.parts[BodyParts.TORSO].left_shoulder
        right_shoulder = self.parts[BodyParts.TORSO].right_shoulder
        return left_shoulder.center_between(right_shoulder)

    def face_center(self):
        return self.parts[BodyParts.HEAD].nose

    def left_palm(self):
        return self.parts[BodyParts.LEFT_ARM].wrist

    def right_palm(self):
        return self.parts[BodyParts.RIGHT_ARM].wrist

    def knees_center(self):
        left_knee = self.parts[BodyParts.LEFT_LEG].knee
        right_knee = self.parts[BodyParts.RIGHT_LEG].knee
        return left_knee.center_between(right_knee)

    def left_shoulder_angle(self):
        return 180 + Vec2.angle(self.parts[BodyParts.LEFT_ARM].first.vector, self.parts[BodyParts.TORSO].left.vector)

    def right_shoulder_angle(self):
        return 180 + Vec2.angle(self.parts[BodyParts.TORSO].right.vector, self.parts[BodyParts.RIGHT_ARM].first.vector)

    def left_elbow_angle(self):
        return 180 - Vec2.angle(self.parts[BodyParts.LEFT_ARM].first.vector, self.parts[BodyParts.LEFT_ARM].second.vector)

    def right_elbow_angle(self):
        return 180 - Vec2.angle(self.parts[BodyParts.RIGHT_ARM].second.vector, self.parts[BodyParts.RIGHT_ARM].first.vector)

    def left_hip_angle(self):
        return 180 - Vec2.angle(self.parts[BodyParts.TORSO].left.vector, self.parts[BodyParts.LEFT_LEG].first.vector)

    def right_hip_angle(self):
        return 180 - Vec2.angle(self.parts[BodyParts.RIGHT_LEG].first.vector, self.parts[BodyParts.TORSO].right.vector)

    def left_knee_angle(self):
        return 180 - Vec2.angle(self.parts[BodyParts.LEFT_LEG].second.vector, self.parts[BodyParts.LEFT_LEG].first.vector)

    def right_knee_angle(self):
        return 180 - Vec2.angle(self.parts[BodyParts.RIGHT_LEG].first.vector, self.parts[BodyParts.RIGHT_LEG].second.vector)