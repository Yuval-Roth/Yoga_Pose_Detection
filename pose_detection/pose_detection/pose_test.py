from abc import abstractmethod, ABC
from body.body import Body
from pose_detection.pose_rules import PoseRule, GenericPoseRule


class PoseTest(ABC):
    def __init__(
            self,
            left_shoulder_angle_rule: PoseRule,
            right_shoulder_angle_rule: PoseRule,
            left_elbow_angle_rule: PoseRule,
            right_elbow_angle_rule: PoseRule,
            left_hip_angle_rule: PoseRule,
            right_hip_angle_rule: PoseRule,
            left_knee_angle_rule: PoseRule,
            right_knee_angle_rule: PoseRule,
            **generic_rules: PoseRule
    ):
        self.left_shoulder_angle_rule = left_shoulder_angle_rule
        self.right_shoulder_angle_rule = right_shoulder_angle_rule
        self.left_elbow_angle_rule = left_elbow_angle_rule
        self.right_elbow_angle_rule = right_elbow_angle_rule
        self.left_hip_angle_rule = left_hip_angle_rule
        self.right_hip_angle_rule = right_hip_angle_rule
        self.left_knee_angle_rule = left_knee_angle_rule
        self.right_knee_angle_rule = right_knee_angle_rule
        self.generic_rules = generic_rules

    def is_satisfied(self, body: Body) -> bool:
        satisfied = True

        if not self.left_shoulder_angle_rule.is_satisfied(body.left_shoulder_angle()):
            satisfied = False
        if not self.right_shoulder_angle_rule.is_satisfied(body.right_shoulder_angle()):
            satisfied = False
        if not self.left_elbow_angle_rule.is_satisfied(body.left_elbow_angle()):
            satisfied = False
        if not self.right_elbow_angle_rule.is_satisfied(body.right_elbow_angle()):
            satisfied = False
        if not self.left_hip_angle_rule.is_satisfied(body.left_hip_angle()):
            satisfied = False
        if not self.right_hip_angle_rule.is_satisfied(body.right_hip_angle()):
            satisfied = False
        if not self.left_knee_angle_rule.is_satisfied(body.left_knee_angle()):
            satisfied = False
        if not self.right_knee_angle_rule.is_satisfied(body.right_knee_angle()):
            satisfied = False
        for rule in self.generic_rules.values():
            if not rule.is_satisfied(body):
                satisfied = False
        return satisfied












