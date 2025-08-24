from enum import Enum

from mediapipe.python.solutions.pose import PoseLandmark

from body.math_utils import Vec3


class Arm:
    def __init__(self, shoulder: Vec3, elbow: Vec3, wrist: Vec3):
        self.first = BodyPart(shoulder, elbow)
        self.second = BodyPart(elbow, wrist)


class Leg:
    def __init__(self, hip: Vec3, knee: Vec3, ankle: Vec3):
        self.first = BodyPart(hip, knee)
        self.second = BodyPart(knee, ankle)


class Torso:
    def __init__(self, left_shoulder: Vec3, right_shoulder: Vec3, left_hip: Vec3, right_hip: Vec3):
        self.right = BodyPart(right_shoulder, right_hip)
        self.left = BodyPart(left_shoulder, left_hip)

class Head:
    def __init__(self, nose: Vec3, left_eye: Vec3, right_eye: Vec3):

        # Center of the head
        self.center = Vec3(
            (nose.x + left_eye.x + right_eye.x) / 3,
            (nose.y + left_eye.y + right_eye.y) / 3,
            (nose.z + left_eye.z + right_eye.z) / 3
        )

        # Vectors along the head plane
        u = left_eye - nose
        v = right_eye - nose

        # Normal vector perpendicular to head plane
        # self.vector = Vec3.cross2(u, v).normalize()

def build_body_parts(pose_landmarks, width, height):
    landmarks_dict = dict()
    for idx, landmark in enumerate(pose_landmarks):
        landmarks_dict[idx] = Vec3(int(landmark.x * width), int(landmark.y * height), round(landmark.z, 3))

    body_parts = {
        BodyParts.LEFT_ARM: Arm(landmarks_dict[PoseLandmark.LEFT_SHOULDER],
                                landmarks_dict[PoseLandmark.LEFT_ELBOW],
                                landmarks_dict[PoseLandmark.LEFT_WRIST]),
        BodyParts.RIGHT_ARM: Arm(landmarks_dict[PoseLandmark.RIGHT_SHOULDER],
                                 landmarks_dict[PoseLandmark.RIGHT_ELBOW],
                                 landmarks_dict[PoseLandmark.RIGHT_WRIST]),
        BodyParts.LEFT_LEG: Leg(landmarks_dict[PoseLandmark.LEFT_HIP],
                                landmarks_dict[PoseLandmark.LEFT_KNEE],
                                landmarks_dict[PoseLandmark.LEFT_ANKLE]),
        BodyParts.RIGHT_LEG: Leg(landmarks_dict[PoseLandmark.RIGHT_HIP],
                                 landmarks_dict[PoseLandmark.RIGHT_KNEE],
                                 landmarks_dict[PoseLandmark.RIGHT_ANKLE]),
        BodyParts.TORSO: Torso(landmarks_dict[PoseLandmark.LEFT_SHOULDER],
                               landmarks_dict[PoseLandmark.RIGHT_SHOULDER],
                               landmarks_dict[PoseLandmark.LEFT_HIP],
                               landmarks_dict[PoseLandmark.RIGHT_HIP]),
        BodyParts.HEAD: Head(landmarks_dict[PoseLandmark.NOSE],
                             landmarks_dict[PoseLandmark.LEFT_EYE],
                             landmarks_dict[PoseLandmark.RIGHT_EYE])
    }

    return body_parts


class BodyParts(Enum):
    LEFT_ARM = "left_arm"
    RIGHT_ARM = "right_arm"
    LEFT_LEG = "left_leg"
    RIGHT_LEG = "right_leg"
    TORSO = "torso"
    HEAD = "head"


class BodyPart:
    def __init__(self, start, end):
        self.vector = (Vec3(end.x, start.y, end.z) - Vec3(start.x, end.y, start.z)).normalize()
        self.center = Vec3(
            int((start.x + end.x) / 2),
            int((start.y + end.y) / 2),
            (start.z + end.z) / 2
        )
