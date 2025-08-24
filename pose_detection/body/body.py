from body.body_parts import *



class Body:
    def __init__(self, pose_landmarks, width, height):
        landmarks_dict = dict()
        for idx, landmark in enumerate(pose_landmarks):
            landmarks_dict[idx] = Vec3(int(landmark.x * width), int(landmark.y * height), round(landmark.z, 3))

        self.body_parts = {
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

    def left_shoulder_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.TORSO].left.vector, self.body_parts[BodyParts.LEFT_ARM].first.vector)

    def right_shoulder_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.TORSO].right.vector, self.body_parts[BodyParts.RIGHT_ARM].first.vector)

    def left_elbow_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.LEFT_ARM].first.vector, self.body_parts[BodyParts.LEFT_ARM].second.vector)

    def right_elbow_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.RIGHT_ARM].first.vector, self.body_parts[BodyParts.RIGHT_ARM].second.vector)

    def left_hip_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.TORSO].left.vector, self.body_parts[BodyParts.LEFT_LEG].first.vector)

    def right_hip_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.TORSO].right.vector, self.body_parts[BodyParts.RIGHT_LEG].first.vector)

    def left_knee_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.LEFT_LEG].first.vector, self.body_parts[BodyParts.LEFT_LEG].second.vector)

    def right_knee_angle(self):
        return Vec3.angle2(self.body_parts[BodyParts.RIGHT_LEG].first.vector, self.body_parts[BodyParts.RIGHT_LEG].second.vector)

    def is_left_hand_straight(self):
        return abs(180 - self.left_elbow_angle()) < 40

    def is_right_hand_straight(self):
        return abs(180 - self.right_elbow_angle())  < 40

    def is_right_leg_straight(self):
        return abs(180 - self.right_knee_angle()) < 15

    def is_left_leg_straight(self):
        return abs(180 - self.left_knee_angle()) < 15