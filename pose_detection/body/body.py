from body.body_parts import *



class Body:
    def __init__(self, pose_landmarks, width, height):
        self.landmarks = dict()
        for idx, landmark in enumerate(pose_landmarks):
            self.landmarks[idx] = Vec3(int(landmark.x * width), int(landmark.y * height), round(landmark.z, 3))

        self.body_parts = {
            BodyParts.LEFT_ARM: Arm(self.landmarks[PoseLandmark.LEFT_SHOULDER],
                                    self.landmarks[PoseLandmark.LEFT_ELBOW],
                                    self.landmarks[PoseLandmark.LEFT_WRIST]),
            BodyParts.RIGHT_ARM: Arm(self.landmarks[PoseLandmark.RIGHT_SHOULDER],
                                     self.landmarks[PoseLandmark.RIGHT_ELBOW],
                                     self.landmarks[PoseLandmark.RIGHT_WRIST]),
            BodyParts.LEFT_LEG: Leg(self.landmarks[PoseLandmark.LEFT_HIP],
                                    self.landmarks[PoseLandmark.LEFT_KNEE],
                                    self.landmarks[PoseLandmark.LEFT_ANKLE]),
            BodyParts.RIGHT_LEG: Leg(self.landmarks[PoseLandmark.RIGHT_HIP],
                                     self.landmarks[PoseLandmark.RIGHT_KNEE],
                                     self.landmarks[PoseLandmark.RIGHT_ANKLE]),
            BodyParts.TORSO: Torso(self.landmarks[PoseLandmark.LEFT_SHOULDER],
                                   self.landmarks[PoseLandmark.RIGHT_SHOULDER],
                                   self.landmarks[PoseLandmark.LEFT_HIP],
                                   self.landmarks[PoseLandmark.RIGHT_HIP]),
            BodyParts.HEAD: Head(self.landmarks[PoseLandmark.NOSE],
                                 self.landmarks[PoseLandmark.LEFT_EYE],
                                 self.landmarks[PoseLandmark.RIGHT_EYE])
        }

    def left_shoulder_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.TORSO].left.vector, self.body_parts[BodyParts.LEFT_ARM].first.vector)

    def right_shoulder_angle(self):
        return -Vec3.angle2(self.body_parts[BodyParts.TORSO].right.vector, self.body_parts[BodyParts.RIGHT_ARM].first.vector)

    def left_elbow_angle(self):
        return 180 - Vec3.angle2(self.body_parts[BodyParts.LEFT_ARM].first.vector, self.body_parts[BodyParts.LEFT_ARM].second.vector)

    def right_elbow_angle(self):
        return 180 - Vec3.angle2(self.body_parts[BodyParts.RIGHT_ARM].second.vector, self.body_parts[BodyParts.RIGHT_ARM].first.vector)

    def left_hip_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.TORSO].left.vector, self.body_parts[BodyParts.LEFT_LEG].first.vector)

    def right_hip_angle(self):
        return -Vec3.angle2(self.body_parts[BodyParts.TORSO].right.vector, self.body_parts[BodyParts.RIGHT_LEG].first.vector)

    def left_knee_angle(self):
        return 180 - Vec3.angle2(self.body_parts[BodyParts.LEFT_LEG].second.vector, self.body_parts[BodyParts.LEFT_LEG].first.vector)

    def right_knee_angle(self):
        return 180 - Vec3.angle2(self.body_parts[BodyParts.RIGHT_LEG].first.vector, self.body_parts[BodyParts.RIGHT_LEG].second.vector)

    def is_left_hand_straight(self):
        return abs(180 - self.left_elbow_angle()) < 40

    def is_right_hand_straight(self):
        return abs(180 - self.right_elbow_angle())  < 40

    def is_right_leg_straight(self):
        return abs(180 - self.right_knee_angle()) < 15

    def is_left_leg_straight(self):
        return abs(180 - self.left_knee_angle()) < 15