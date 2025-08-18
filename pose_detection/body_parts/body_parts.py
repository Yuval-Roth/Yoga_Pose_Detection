from mediapipe.python.solutions.pose import PoseLandmark

from . import *


class Arm:
    def __init__(self, shoulder: Vec3, elbow: Vec3, wrist: Vec3):
        self.upper = BodyPart(shoulder, elbow)
        self.lower = BodyPart(elbow, wrist)


class Leg:
    def __init__(self, hip: Vec3, knee: Vec3, ankle: Vec3):
        self.upper = BodyPart(hip, knee)
        self.lower = BodyPart(knee, ankle)


class Torso:
    def __init__(self, left_shoulder: Vec3, right_shoulder: Vec3, left_hip: Vec3, right_hip: Vec3):

        # Center of torso
        self.center = Vec3(
            (left_shoulder.x + right_shoulder.x + left_hip.x + right_hip.x) / 4,
            (left_shoulder.y + right_shoulder.y + left_hip.y + right_hip.y) / 4,
            (left_shoulder.z + right_shoulder.z + left_hip.z + right_hip.z) / 4
        )

        # Two vectors along the torso plane
        u = right_shoulder - left_shoulder
        v = left_hip - left_shoulder

        # Normal vector perpendicular to torso plane
        self.vector = Vec3.cross(u, v).normalize()

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
        self.vector = Vec3.cross(u, v).normalize()

def build_body_parts(pose_landmarks):
    landmarks_dict = dict()
    for idx, landmark in enumerate(pose_landmarks.landmark):
        landmarks_dict[idx] = Vec3(landmark.x * 256, landmark.y * 256, landmark.z * 256)

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









